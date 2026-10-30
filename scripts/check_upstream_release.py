#!/usr/bin/env python3
"""Check the in-toto specification copy against in-toto/attestation's releases.

Three things can go wrong with ``src/in_toto_linkml/schema/attestation/``
without any change in this repository:

- the in-toto project releases a newer version of the framework, so the
  schema falls behind;
- the pinned tag is moved to another commit;
- the copied files drift from the files they were taken from.

The release, the commit its tag names and each copied file's git object hash
are pinned below. This script asks the GitHub API for in-toto/attestation's
latest release, the commit the pinned tag names and the repository's file
tree at the pinned commit and at the latest release, one listing each. It
compares every copied file with its blob by git object hash, so nothing is
downloaded but listings. It prints a Markdown report and exits 1 when a newer
release is out, a pinned file changed or is gone, a file differs, the pinned
tag moved, or a check could not finish. A specification page or predicate
definition the in-toto project adds beside the pinned ones is reported for
information only.

Set ``GITHUB_TOKEN`` to raise the API rate limit. Usage::

    python scripts/check_upstream_release.py [--report FILE]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.request
from functools import cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COPY = ROOT / "src" / "in_toto_linkml" / "schema" / "attestation"
API = "https://api.github.com/repos/in-toto/attestation"
USER_AGENT = "lmodel-in-toto-upstream-check"

# The release and the commit its tag names. Move them together when the copy
# is replaced from a newer release, with PINNED_BLOBS and the schema header.
PINNED_TAG = "v1.2.0"
PINNED_COMMIT = "df02077bf97218a8860a5c534eff1f1381f56984"

# Each copied file, by its path in in-toto/attestation and in the copy, and
# its git object hash at PINNED_COMMIT. tests/test_upstream.py checks the
# hashes offline.
PINNED_BLOBS = {
    "LICENSE": "702a3365c0666d8dd0658820ebaa157e7c2f5c27",
    "spec/v1/README.md": "6007b434f79637ad6aa39dd116ca11ba93f0d8ce",
    "spec/v1/CHANGELOG.md": "4121fa3c9fc7496ffcd3a4070c527a867098b617",
    "spec/v1/statement.md": "630f773cb530fe5989fe2dbc30e7f73239cd943a",
    "spec/v1/resource_descriptor.md": "3d87e11b65c3faca9630b2f25008d0ecdbd2a91d",
    "spec/v1/digest_set.md": "cddde316c3a97906d9914127f93503f71c0c9c1f",
    "spec/v1/field_types.md": "9abfc4cb05166fa0afccbee9f231718f72323461",
    "spec/v1/predicate.md": "e2fd7dc448f6f3638f8c9b477bdbf9751e885947",
    "spec/predicates/README.md": "1bd6d235b8aa9287e108f8cc7656e8cc42f6e3c6",
    "spec/predicates/link.md": "5ff3f9d5efd3f5abf4c57da35353d272830c65cb",
    "spec/predicates/reference.md": "80aa0ac7b55b9353450dcc566cba4f1af22bde0f",
    "spec/predicates/release.md": "60bda19694725ab517bc1299988e2acc5aa042fc",
    "spec/predicates/runtime-trace.md": "58e38f06c07d68559fe32c500d13c1402bdc3d59",
    "spec/predicates/scai.md": "1d749b74e8bf1b93962d04fbfcf82086c3298073",
    "spec/predicates/svr.md": "d7e46a60bb59c6b120b528d8a11bd67b8714ab96",
    "spec/predicates/test-result.md": "74d83c3021010757e56e96cf68bf7a6b11fb86e5",
    "spec/predicates/vulns_02.md": "e76ee55e1bae221434cac8ac5337a4c8fea5c72e",
    "protos/in_toto_attestation/v1/statement.proto": "6c55dc7b16d2140912666338e68c43a3075519a1",
    "protos/in_toto_attestation/v1/resource_descriptor.proto": "334b0e0f2ecfd6b41312700d3aa9597d44b332e5",
    "protos/in_toto_attestation/predicates/link/v0/link.proto": "388e0b627dc352c3a8fd7e28e0c56c40fd5d865c",
    "protos/in_toto_attestation/predicates/reference/v0/reference.proto": "ec5ac4295c6d289896d96e0bcdeba1251470fbcd",
    "protos/in_toto_attestation/predicates/release/v0.2/release.proto": "738f5711bba0c10af9ac3d2ca5321b0c60b45572",
    "protos/in_toto_attestation/predicates/scai/v0/scai.proto": "180d825cd2d62b381cb45336bbde781c3b6be19e",
    "protos/in_toto_attestation/predicates/svr/v0.1/svr.proto": "454cd7eaf66ff07ec9e8902d7ff8ce3aab65d935",
    "protos/in_toto_attestation/predicates/test_result/v0/test_result.proto": "54e53e58e4d173928e49ac4ff24c7e4fb19e4389",
    "protos/in_toto_attestation/predicates/vulns/v0.2/vulns.proto": "a4c2e69672b9c411466235f37b09b94ebe32baea",
}

# The folders whose new files are worth a reader's look: the framework's own
# pages, the predicate pages and the predicate definitions.
WATCHED = ("spec/v1/", "spec/predicates/", "protos/in_toto_attestation/")

# Files in WATCHED that the copy leaves out on purpose, so that only a file
# the in-toto project adds is reported. The envelope and the bundle wrap a
# statement and are outside the model. lmodel/slsa models SLSA Provenance and
# the Verification Summary. The CycloneDX, SPDX 2 and SPDX 3 predicates carry
# a whole bill of materials, which the schema names by type URI only. vuln.md
# and the older predicate versions are superseded by the copied ones, and the
# template is a page for authors.
LEFT_OUT = re.compile(
    r"^("
    r"spec/v1/(envelope|bundle)\.md"
    r"|spec/predicates/(provenance|vsa|cyclonedx|spdx2|spdx3|vuln)\.md"
    r"|spec/predicates/template/.*"
    r"|protos/in_toto_attestation/predicates/(provenance|vsa)/.*"
    r"|protos/in_toto_attestation/predicates/(release/v0\.1|vulns/v0\.1)/.*"
    r"|protos/in_toto_attestation/(Makefile|README\.md)"
    r")$"
)


def _get(url: str) -> bytes:
    req = urllib.request.Request(
        url,
        headers={"Accept": "application/vnd.github+json", "User-Agent": USER_AGENT},
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token and url.startswith(API):
        # urllib copies ordinary headers onto a redirect, so the token goes in
        # an unredirected one and reaches api.github.com alone.
        req.add_unredirected_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def _version_key(tag: str) -> tuple[int, ...]:
    """Numeric parts of a tag, padded so that v1.2 and v1.2.0 order alike."""
    parts = [int(x) for x in re.findall(r"\d+", tag)]
    return tuple(parts + [0] * (4 - len(parts)))


def _blob_sha(path: Path) -> str:
    """The git object hash of a file, as the trees API reports it."""
    data = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


@cache
def _tree(ref: str) -> dict[str, str]:
    """Every file of the repository at a ref, by path, with its object hash.
    A ref the repository does not hold gives an empty mapping. Each tree is
    asked for once, and no caller changes what it returns."""
    try:
        body = json.loads(_get(f"{API}/git/trees/{ref}?recursive=1"))
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return {}
        raise
    if body.get("truncated"):
        raise OSError(f"the tree at {ref} is too large for one listing")
    return {e["path"]: e["sha"] for e in body.get("tree", []) if e["type"] == "blob"}


def _tag_commit(tag: str) -> str | None:
    """The commit a tag names, read through the tag object when the tag is an
    annotated one, or None when the repository has no such tag."""
    try:
        target = json.loads(_get(f"{API}/git/ref/tags/{tag}"))["object"]
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return None
        raise
    while target["type"] == "tag":
        target = json.loads(_get(f"{API}/git/tags/{target['sha']}"))["object"]
    return target["sha"]


@cache
def _latest() -> str:
    """The tag of in-toto/attestation's latest release, asked once."""
    return json.loads(_get(f"{API}/releases/latest"))["tag_name"]


def _newer(tag: str) -> bool:
    return _version_key(tag) > _version_key(PINNED_TAG)


def _added(tree: dict[str, str]) -> list[str]:
    """The files of the watched folders that are neither copied nor left out
    on purpose."""
    return sorted(
        path
        for path in tree
        if path.startswith(WATCHED)
        and path not in PINNED_BLOBS
        and not LEFT_OUT.match(path)
    )


def check_release() -> tuple[list[str], bool]:
    """Report whether in-toto/attestation has a newer release than the pin."""
    latest = _latest()
    if _newer(latest):
        return [
            f"- **in-toto/attestation {latest} is out; the schema renders "
            f"{PINNED_TAG}.** Read its changelog and the pages it changes, decide "
            "whether the schema moves to it, and replace the copy from that release."
        ], True
    return [f"- Latest release: {latest}, the pinned one."], False


def check_copy() -> tuple[list[str], bool]:
    """Report whether the pinned tag still names the pinned commit, whether
    the copy is the files pinned there, and whether a newer release changes
    or drops any of them."""
    report = [
        f"- Pinned release: in-toto/attestation {PINNED_TAG}, commit "
        f"`{PINNED_COMMIT[:12]}`, copied to `src/in_toto_linkml/schema/attestation/`.",
    ]
    attention = False

    commit = _tag_commit(PINNED_TAG)
    if commit != PINNED_COMMIT:
        attention = True
        named = f"commit `{commit[:12]}`" if commit else "nothing"
        report.append(
            f"- **The tag {PINNED_TAG} now names {named}, not the pinned commit "
            f"`{PINNED_COMMIT[:12]}`.** Find out why it moved before trusting either."
        )

    pinned_tree = _tree(PINNED_COMMIT)
    matching, differing = 0, []
    for name, pinned_sha in sorted(PINNED_BLOBS.items()):
        path = COPY / name
        if not path.is_file():
            differing.append(f"`{name}` is missing from the copy")
        elif pinned_tree.get(name) != pinned_sha:
            differing.append(
                f"`{name}` at commit `{PINNED_COMMIT[:12]}` is not the pinned blob"
            )
        elif _blob_sha(path) != pinned_sha:
            differing.append(f"`{name}` differs from its file at {PINNED_TAG}")
        else:
            matching += 1
    extra = sorted(
        p.relative_to(COPY).as_posix()
        for p in COPY.rglob("*")
        if p.is_file() and p.relative_to(COPY).as_posix() not in PINNED_BLOBS
    )
    differing += [f"`{name}` is in the copy but not pinned" for name in extra]
    report.append(
        f"- {matching} of {len(PINNED_BLOBS)} copied files match the pinned commit byte for byte."
    )
    if differing:
        attention = True
        report.append(f"- **{len(differing)} problem(s) with the copy:**")
        report += [f"  - {d}" for d in differing]
    added = {PINNED_TAG: _added(pinned_tree)}

    latest = _latest()
    if _newer(latest):
        latest_tree = _tree(latest)
        dropped = sorted(n for n in PINNED_BLOBS if n not in latest_tree)
        changed = sorted(
            n
            for n, sha in PINNED_BLOBS.items()
            if n in latest_tree and latest_tree[n] != sha
        )
        for name in dropped:
            attention = True
            report.append(
                f"- **in-toto/attestation {latest} no longer holds `{name}`.** Find "
                "where the in-toto project now publishes it, and move the pins."
            )
        for name in changed:
            attention = True
            report.append(
                f"- **in-toto/attestation {latest} changes `{name}`.** Replace "
                f"`src/in_toto_linkml/schema/attestation/{name}` with the file at that "
                f"tag (https://github.com/in-toto/attestation/blob/{latest}/{name}), "
                "move the pins here and in the schema header, and run `just test`."
            )
        if not dropped and not changed:
            report.append(
                f"- Latest release: {latest}, which holds the pinned files unchanged."
            )
        added[latest] = _added(latest_tree)

    for ref, names in added.items():
        if names:
            report.append(
                f"- For information, in-toto/attestation at {ref} also holds "
                + ", ".join(f"`{n}`" for n in names)
                + ", which the copy neither holds nor leaves out on purpose."
            )
    return report, attention


# Each check, by the name the report gives it when it cannot finish.
CHECKS = (("release", check_release), ("copy", check_copy))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--report", type=Path, help="Also write the Markdown report to this file"
    )
    args = parser.parse_args(argv)
    lines, attention = [], False
    for label, check in CHECKS:
        try:
            found, needs = check()
        except (urllib.error.URLError, TimeoutError, OSError) as err:
            found, needs = [f"- **The {label} check could not finish: {err}.**"], True
        lines += found
        attention = attention or needs
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    return 1 if attention else 0


if __name__ == "__main__":
    sys.exit(main())
