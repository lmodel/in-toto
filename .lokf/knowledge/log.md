# Change Log

## 2026-11-23

* **Added**: `workflows/codeql.md`, for `.github/workflows/codeql.yml`, which had no concept.
* **Added**: `workflows/scorecard.md`, for `.github/workflows/scorecard.yml`, which had no concept.
* **Changed**: `policies/security-policy.md` now cites, as a typed relation, every workflow its table of surfaces names, including `codeql.yml` and `scorecard.yml`.
* **Changed**: `policies/ai-covenant.md` now cites `workflows/knowledge-librarian.md` as a typed relation, the workflow its Repository-Owned Agent Automation section names.
* **Changed**: step 4 now says the GitHub release's body is the promoted changelog section, the fix `changelog-release.mjs` carries since commit 3adc887 (the CHANGELOG's 0.4.3 entry).
* **Changed**: the scrape map now counts eleven files under `.github/workflows/`, since `codeql.yml` and `scorecard.yml` each gained a concept this run.

## 2026-11-15

* **Changed**: sources and text follow the move of `.github/release` to `.release`.
* **Changed**: The concepts that state the project's Python floor or its test matrix say 3.11, since the project no longer supports Python 3.10.
* **Changed**: The generated artefacts no longer say the website builds `docs/elements/`, since the Hugo site writes its own schema pages.
* **Changed**: The knowledge website workflow, the documentation site and the security policy describe the Hugo build that replaced the Astro one.
* **Changed**: The concepts that cite the knowledge website describe the Hugo site that replaced the Astro one, set by `website/site.toml`.

## 2026-11-06

* **Changed**: `lokf.yaml` and `in-toto.yaml` moved into `.lokf/schema/`, where KTL v0.62.0 keeps a sidecar's schema files, and the concepts that name them follow.

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
