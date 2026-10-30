---
type: Playbook
id: https://w3id.org/lmodel/in-toto/knowledge/playbooks/update-upstream-pins
genre: how-to
title: Update the upstream pins
description: "What to do when the weekly upstream watch reports that in-toto/attestation released again, changed or dropped a pinned file, or moved the pinned tag, that the copy drifted, or that a check could not finish: replace the copy whole from one release, move the pins in `scripts/check_upstream_release.py` and the schema header, and run the tests."
resource: scripts/check_upstream_release.py
about:
  - https://w3id.org/lmodel/in-toto/knowledge/datasets/attestation-copy
sources:
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: the docstring, the pins and the report lines
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: the item on the specification copy
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: the pin, field and vetted-list tests
generated:
  by: process:ktl-librarian
  at: "2026-10-30T16:14:35Z"
status: draft
---

# Update the upstream pins

`scripts/check_upstream_release.py` runs every Monday in [Upstream watch](../workflows/upstream-watch.md) with the standard library alone. It asks the GitHub API for in-toto/attestation's latest release, the commit the pinned tag names, and the repository's file tree at the pinned commit and at the latest release. It exits 1, and the workflow opens or updates an issue, on each of these findings.[^check_upstream_release.py]

- **in-toto/attestation has a newer release** than v1.2.0. Read its changelog and the pages it changes, decide whether the schema moves to it, and replace the copy from that release.
- **A newer release changes a pinned file** or **no longer holds one**. Replace the file from that tag, or find where the in-toto project now publishes it.
- **The pinned tag names another commit** than the one pinned. Find out why it moved before trusting either.
- **A copied file differs from its pinned blob**, or the copy holds a file the script does not pin.
- **A check could not finish**, for example on a network error or a tree listing GitHub cut short. The report names the check and the error, and the other check still runs.

A file the in-toto project adds to `spec/v1/`, `spec/predicates/` or `protos/in_toto_attestation/` is reported for information and does not fail the run, unless the script leaves it out on purpose: the envelope and bundle pages, SLSA's two predicates, the three bill-of-materials predicates, the superseded versions and the template. `tests/test_watch.py` checks each of these reports against stubbed answers.

To replace the copy, take every pinned file from one release, at its path under `src/in_toto_linkml/schema/attestation/`. Never edit them.[^contributing.md] Then move `PINNED_TAG`, `PINNED_COMMIT` and `PINNED_BLOBS` in the script, and the header's `version`, `source` and the `attestation_tag` and `attestation_commit` annotations, and update NOTICE. Run `just gen-project`, `just gen-doc` and `just lokf-adapt`, since the header's values reach the generated files and the adapt copy. Then run `just test`. `tests/test_upstream.py` checks that the header and the script name the same pins, that each file has its pinned hash, that each field of a copied protocol buffer message maps to a slot, and that `InTotoVettedPredicate` holds the predicates page's list.[^test_upstream.py]

[^check_upstream_release.py]: scripts/check_upstream_release.py, the docstring, check_release, check_copy and main
[^contributing.md]: CONTRIBUTING.md, the item on the specification copy
[^test_upstream.py]: tests/test_upstream.py, the pin, field and vetted-list tests
