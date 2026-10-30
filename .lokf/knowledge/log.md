# Change Log

## 2026-10-30

* **Prose**: reworded 18 concept bodies in plain English. No fact, link, number or frontmatter changed.
* **Changed**: sentences this run lengthened are split, with no fact changed.
* **Changed**: the statement's predicate is `predicate` again, a slot the adapt copy renames `in_toto_linkml_predicate`, as `docs/about.md` now says.
* **Changed**: `InTotoStatement` holds the optional `predicate`, no longer `statement_predicate`.
* **Changed**: the core now holds the framework's three field types and the statement's `predicate` slot, and the timestamp type left the predicates module; the adapt copy renames `predicate`.
* **Changed**: the copy holds 31 files, with the pages of CycloneDX, SPDX 2, SPDX 3, SLSA Provenance and the Verification Summary, which give their type URIs.
* **Changed**: the counts of examples and counter-examples, the ten examples taken from the specification's pages, and the tests that hold them and the vetted type URIs to the pages.
* **Changed**: the page now says a file is written in the schema's keys, that the URI types check a lowercase scheme and authority, and that Pydantic checks no type's pattern.
* **Changed**: the watch now copies the five predicate pages it used to leave out, and the tests hold each vetted value to its page.
* **Changed**: the README now says the schema does not take an attestation's published JSON.
* **Added**: Build and test (main.yaml), from `.github/workflows/main.yaml`.
* **Added**: Lint & docs (lint-and-docs.yaml), from `.github/workflows/lint-and-docs.yaml`.
* **Added**: Semantic release (semantic-release.yml), from `.github/workflows/semantic-release.yml`.
* **Added**: Knowledge Librarian (knowledge-librarian.yaml), from `.github/workflows/knowledge-librarian.yaml`.
* **Added**: Knowledge Registrar (knowledge-registrar.yaml), from `.github/workflows/knowledge-registrar.yaml`.
* **Added**: Knowledge Release (knowledge-release.yaml), from `.github/workflows/knowledge-release.yaml`.
* **Added**: Knowledge sync (knowledge-sync.yaml), from `.github/workflows/knowledge-sync.yaml`.
* **Added**: Knowledge website (knowledge-website.yaml), from `.github/workflows/knowledge-website.yaml`.
* **Added**: Security policy, from `SECURITY.md`.
* **Added**: Cut a release, from `.releaserc.json`.
* **Added**: Upstream watch (upstream-watch.yaml), from `.github/workflows/upstream-watch.yaml`.
* **Added**: AI covenant, from `AI_COVENANT.md`.
* **Added**: License and attribution, from `NOTICE`.
* **Added**: Regenerate and test after a schema change, from `CONTRIBUTING.md`.
* **Added**: Update the upstream pins, from `scripts/check_upstream_release.py`.
* **Added**: Validate data against the schema, from `docs/index.md`.
* **Added**: Knowledge sources map, from `.`.
* **Added**: Documentation site, from `website`.
* **Added**: in-toto LinkML schema, from `src/in_toto_linkml/schema/in_toto_linkml.yaml`.
* **Added**: The in-toto specification copy, from `src/in_toto_linkml/schema/attestation`.
* **Added**: Generated artefacts, from `project`.
* **Added**: Test data and tests, from `tests`.
* **Added**: The in-toto Attestation Framework, from `src/in_toto_linkml/schema/attestation/spec/v1/README.md`.
* **Added**: The vetted predicates, from `src/in_toto_linkml/schema/attestation/spec/predicates/README.md`.
* **Added**: Scope, influences and mappings, from `README.md`.
* **Added**: Element names and the shared namespace, from `docs/about.md`.
* **Added**: Statement, from `src/in_toto_linkml/schema/attestation/spec/v1/statement.md`.
* **Added**: Resource descriptor, from `src/in_toto_linkml/schema/attestation/spec/v1/resource_descriptor.md`.
* **Added**: Digest set, from `src/in_toto_linkml/schema/attestation/spec/v1/digest_set.md`.
* **Added**: Predicate, from `src/in_toto_linkml/schema/attestation/spec/v1/predicate.md`.
* **Added**: Predicate type, from `src/in_toto_linkml/schema/attestation/spec/v1/field_types.md`.
* **Added**: Test Result, from `src/in_toto_linkml/schema/attestation/spec/predicates/test-result.md`.
* **Added**: Simple Verification Result, from `src/in_toto_linkml/schema/attestation/spec/predicates/svr.md`.
* **Added**: SCAI Report, from `src/in_toto_linkml/schema/attestation/spec/predicates/scai.md`.
* **Added**: Link, from `src/in_toto_linkml/schema/attestation/spec/predicates/link.md`.
* **Added**: Reference, from `src/in_toto_linkml/schema/attestation/spec/predicates/reference.md`.
* **Added**: Release, from `src/in_toto_linkml/schema/attestation/spec/predicates/release.md`.
* **Added**: Runtime Traces, from `src/in_toto_linkml/schema/attestation/spec/predicates/runtime-trace.md`.
* **Added**: VULNS, from `src/in_toto_linkml/schema/attestation/spec/predicates/vulns_02.md`.
* **Added**: SLSA Provenance, from `src/in_toto_linkml/schema/in_toto_predicates.yaml`.
* **Added**: SLSA Verification Summary, from `src/in_toto_linkml/schema/in_toto_predicates.yaml`.
* **Added**: CycloneDX, from `src/in_toto_linkml/schema/in_toto_predicates.yaml`.
* **Added**: SPDX2, from `src/in_toto_linkml/schema/in_toto_predicates.yaml`.
* **Added**: SPDX3, from `src/in_toto_linkml/schema/in_toto_predicates.yaml`.
* **Removal**: the sidecar's placeholder service, which the bootstrap replaces with the repository's own concepts.
* **Initialization**: Scaffolded the LOKF bundle for in-toto with placeholder
  services. Real concepts to follow.
