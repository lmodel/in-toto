"""Checks the upstream watch's decisions against stubbed GitHub API answers.

scripts/check_upstream_release.py asks the GitHub API about
in-toto/attestation. These tests replace its one network call, `_get`, with
a table of answers, so they run offline. They show what the report says when
a release drops or changes a file, the network fails, the in-toto project
adds a predicate or the pinned tag moves.
"""

import importlib.util
import json
import urllib.error
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check_upstream_release.py"
NEWER = "v9.0.0"


@pytest.fixture
def watch():
    """A fresh copy of the script, so no test sees another's cached answers."""
    spec = importlib.util.spec_from_file_location("watch_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _tree(watch, extra=()):
    """A tree listing that holds the pinned files, a file left out on purpose
    and any `extra` (path, sha) pairs."""
    entries = [
        {"path": path, "type": "blob", "sha": sha}
        for path, sha in watch.PINNED_BLOBS.items()
    ]
    entries.append({"path": "spec/v1/envelope.md", "type": "blob", "sha": "0" * 40})
    entries.append({"path": "spec/predicates", "type": "tree", "sha": "5" * 40})
    entries += [{"path": p, "type": "blob", "sha": s} for p, s in extra]
    return {"tree": entries, "truncated": False}


def _answers(watch, latest):
    """What the API answers when nothing has changed since the pin, with
    `latest` as the latest release, keyed by the address the script asks."""
    api = watch.API
    answers = {
        f"{api}/releases/latest": {"tag_name": latest},
        f"{api}/git/ref/tags/{watch.PINNED_TAG}": {
            "object": {"type": "tag", "sha": "1" * 40}
        },
        f"{api}/git/tags/{'1' * 40}": {
            "object": {"type": "commit", "sha": watch.PINNED_COMMIT}
        },
    }
    for ref in {watch.PINNED_COMMIT, latest}:
        answers[f"{api}/git/trees/{ref}?recursive=1"] = _tree(watch)
    return answers


def _stub(watch, answers):
    """Make `_get` answer from the table: an exception is raised, a missing
    address is a 404, and anything else is returned as JSON."""

    def get(url):
        if url not in answers:
            raise urllib.error.HTTPError(url, 404, "Not Found", None, None)
        answer = answers[url]
        if isinstance(answer, Exception):
            raise answer
        return json.dumps(answer).encode()

    watch._get = get


def _run(watch, tmp_path):
    report = tmp_path / "report.md"
    code = watch.main(["--report", str(report)])
    return code, report.read_text(encoding="utf-8")


def test_nothing_changed(watch, tmp_path):
    """With the pinned release the latest and every blob as pinned, the watch
    reports the copy current and exits 0."""
    _stub(watch, _answers(watch, watch.PINNED_TAG))
    code, text = _run(watch, tmp_path)
    assert code == 0, text
    assert f"Latest release: {watch.PINNED_TAG}, the pinned one." in text
    count = len(watch.PINNED_BLOBS)
    assert f"{count} of {count} copied files match" in text
    assert "For information" not in text


def test_a_newer_release_is_reported(watch, tmp_path):
    """A newer release sets attention even when it holds the pinned files
    unchanged, since its other pages may move the framework."""
    _stub(watch, _answers(watch, NEWER))
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert f"**in-toto/attestation {NEWER} is out; the schema renders" in text
    assert f"Latest release: {NEWER}, which holds the pinned files unchanged." in text


def test_a_release_that_drops_and_changes_files(watch, tmp_path):
    """A newer release without a pinned file, or with a changed one, is
    reported as such, not as a crash."""
    answers = _answers(watch, NEWER)
    tree = answers[f"{watch.API}/git/trees/{NEWER}?recursive=1"]
    tree["tree"] = [
        {**e, "sha": "2" * 40} if e["path"] == "LICENSE" else e
        for e in tree["tree"]
        if e["path"] != "spec/predicates/svr.md"
    ]
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert (
        f"**in-toto/attestation {NEWER} no longer holds `spec/predicates/svr.md`.**"
        in text
    )
    assert f"**in-toto/attestation {NEWER} changes `LICENSE`.**" in text


def test_a_network_failure_still_writes_a_report(watch, tmp_path):
    """A check that cannot reach the API is reported as unfinished, sets
    attention, and leaves the other check to run."""
    answers = _answers(watch, watch.PINNED_TAG)
    answers[f"{watch.API}/git/trees/{watch.PINNED_COMMIT}?recursive=1"] = (
        urllib.error.URLError("Connection refused")
    )
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert (
        "**The copy check could not finish: <urlopen error Connection refused>.**"
        in text
    )
    assert f"Latest release: {watch.PINNED_TAG}, the pinned one." in text


def test_a_truncated_tree_is_reported_as_unfinished(watch, tmp_path):
    """A listing GitHub cut short cannot prove a file is gone, so the check
    stops instead of reporting it dropped."""
    answers = _answers(watch, watch.PINNED_TAG)
    answers[f"{watch.API}/git/trees/{watch.PINNED_COMMIT}?recursive=1"]["truncated"] = (
        True
    )
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The copy check could not finish: the tree at" in text


def test_a_predicate_the_project_adds_is_information_only(watch, tmp_path):
    """A file in a watched folder that the copy neither holds nor leaves out
    on purpose is reported, and is not a reason to fail."""
    answers = _answers(watch, watch.PINNED_TAG)
    answers[f"{watch.API}/git/trees/{watch.PINNED_COMMIT}?recursive=1"] = _tree(
        watch, [("spec/predicates/sbom-summary.md", "3" * 40)]
    )
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 0, text
    assert "For information" in text and "`spec/predicates/sbom-summary.md`" in text


def test_a_moved_tag(watch, tmp_path):
    """A pinned tag that names another commit sets attention."""
    answers = _answers(watch, watch.PINNED_TAG)
    answers[f"{watch.API}/git/tags/{'1' * 40}"] = {
        "object": {"type": "commit", "sha": "4" * 40}
    }
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert f"**The tag {watch.PINNED_TAG} now names commit `444444444444`" in text


def test_the_token_never_follows_a_redirect(watch, monkeypatch):
    """The token goes in an unredirected header, and only to the API."""
    seen = []

    class Answer:
        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

        def read(self):
            return b"{}"

    def urlopen(req, timeout):
        seen.append(req)
        return Answer()

    monkeypatch.setenv("GITHUB_TOKEN", "secret")
    monkeypatch.setattr(watch.urllib.request, "urlopen", urlopen)
    watch._get(f"{watch.API}/releases/latest")
    watch._get("https://example.org/elsewhere")
    assert seen[0].unredirected_hdrs == {"Authorization": "Bearer secret"}
    assert "Authorization" not in seen[0].headers
    assert seen[1].unredirected_hdrs == {}
