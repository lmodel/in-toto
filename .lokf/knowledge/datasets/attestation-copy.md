---
type: Dataset
id: https://w3id.org/lmodel/in-toto/knowledge/datasets/attestation-copy
genre: reference
title: The in-toto specification copy
description: The specification pages and protocol buffer definitions of the in-toto Attestation Framework at release v1.2.0, 31 files copied with the in-toto project's licence into `src/in_toto_linkml/schema/attestation/` and matched to that release by git object hash. The tests hold every field of the copied definitions to a slot of the schema, and each vetted type URI to the page that gives it.
resource: src/in_toto_linkml/schema/attestation
license: https://spdx.org/licenses/Apache-2.0
derivedFrom:
  - https://w3id.org/lmodel/in-toto/knowledge/references/attestation-framework
sources:
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: PINNED_TAG, PINNED_COMMIT, PINNED_BLOBS and LEFT_OUT
  - id: notice
    resource: NOTICE
    title: The in-toto Attestation Framework
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: the copy, field, vetted-list and page-example tests
generated:
  by: process:ktl-librarian
  at: "2026-10-30T21:22:17Z"
status: draft
---

# The in-toto specification copy

`src/in_toto_linkml/schema/attestation/` holds 31 files from in-toto/attestation at the tag `v1.2.0`, commit `df02077bf972`, each at the path it has there:

- the `LICENSE`;
- seven pages of `spec/v1/`;
- the predicates page and the pages of all thirteen vetted predicates under `spec/predicates/`;
- the statement and resource descriptor definitions under `protos/in_toto_attestation/v1/`;
- the definitions of seven of the predicates under `protos/in_toto_attestation/predicates/`.

Runtime Trace publishes no definition. `scripts/check_upstream_release.py` pins each file's git object hash.[^check_upstream_release.py]

The script leaves out, on purpose, the envelope and bundle pages, the SLSA Provenance and Verification Summary definitions, the superseded VULNS v0.1 page and older predicate versions, and the authors' template. NOTICE says that the files are the in-toto project's under the Apache License 2.0, and that the tests read them and nothing changes them.[^notice]

`tests/test_upstream.py` checks that the copy holds exactly the pinned files with their hashes. It reads each copied protocol buffer message and checks that every field maps to a slot of the class that renders it, with the Simple Verification Result's optional `policy` left out on purpose. It also checks that `InTotoVettedPredicate` holds the predicates page's list, and that each predicate's type URI is the one its page's examples carry. It checks that each vetted value means a type URI its page gives, and that the ten examples taken from the pages hold the pages' values.[^test_upstream.py]

[^check_upstream_release.py]: scripts/check_upstream_release.py, the pins and LEFT_OUT
[^notice]: NOTICE, The in-toto Attestation Framework
[^test_upstream.py]: tests/test_upstream.py, the copy, field, vetted-list and page-example tests
