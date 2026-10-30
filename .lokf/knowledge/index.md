---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/lmodel/in-toto/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: in-toto Knowledge Bundle
description: in-toto Attestation Framework (LinkML)
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Person
  id: https://w3id.org/lmodel/in-toto/knowledge/person/noel-mcloughlin
  name: Noel McLoughlin
---

# in-toto Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for in-toto. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# Services

* [Documentation site](services/documentation-site.md) - The Astro Starlight site in `website/`, for <https://lmodel.github.io/in-toto>: the README as its home page, the pages of `docs/`, the schema's element pages, a page per concept of this bundle with its trust label, and the bundle's exports, built and published by Knowledge website.

# Workflows

* [Build and test (main.yaml)](workflows/main.md) - The Build and test workflow, `.github/workflows/main.yaml`: on a push to main and on every pull request, its test job runs `just test` on Python 3.10 to 3.14, and on 3.13 also `just lint` and `just lokf-adapt-check`, the check that `.lokf/in-toto.yaml` is current.
* [Lint & docs (lint-and-docs.yaml)](workflows/lint-and-docs.md) - The Lint & docs workflow, `.github/workflows/lint-and-docs.yaml`: on a push to main, every pull request, a Monday 06:00 UTC schedule and by hand, four jobs run ShellCheck, actionlint, the word budgets of CONTRIBUTING.md (1000) and SECURITY.md (900), and markdownlint, lychee and codespell over the Markdown.
* [Semantic release (semantic-release.yml)](workflows/semantic-release.md) - The Semantic release workflow, `.github/workflows/semantic-release.yml`: on a pull request into main, its plan job checks that the commits, the changelog and the title would release and previews the release; on a push to main, its release job in the release Environment tags vX.Y.Z, publishes the GitHub release and dispatches Knowledge Release.
* [Knowledge Librarian (knowledge-librarian.yaml)](workflows/knowledge-librarian.md) - The Knowledge Librarian workflow, `.github/workflows/knowledge-librarian.yaml`: every Monday at 05:00 UTC and by hand, once `KNOWLEDGE_LIBRARIAN_ENABLED` is true, it runs an agent with the ktl-librarian skill (pinned by `TRUST_LADDER_SKILLS_REF` at v0.59.0) in a read-only job and opens a review pull request from a separate job that runs no agent.
* [Knowledge Registrar (knowledge-registrar.yaml)](workflows/knowledge-registrar.md) - The Knowledge Registrar workflow, `.github/workflows/knowledge-registrar.yaml`: the gate on the knowledge bundle, run on pull requests that touch `.lokf/` or `knowledge_bundle/`, every Monday at 06:00 UTC and by hand; it validates the bundle and its relation targets against the domain schema, runs the conventions script, and checks that each new confirmation by a person is backed by an approval or a signed commit.
* [Knowledge Release (knowledge-release.yaml)](workflows/knowledge-release.md) - The Knowledge Release workflow, `.github/workflows/knowledge-release.yaml`: dispatched with a release's tag, or started by a published release once `KNOWLEDGE_RELEASE_ENABLED` is true, it attaches the bundle zip, the domain schema as `schema-<tag>-in-toto.yaml` with its checksum, and the Copilot skills to the release, when the bundle or the schema changed or `force` is set.
* [Knowledge sync (knowledge-sync.yaml)](workflows/knowledge-sync.md) - The Knowledge sync workflow, `.github/workflows/knowledge-sync.yaml`: every Monday at 04:10 UTC and by hand, it moves the sidecar's copies and the skills pin to the newest Knowledge Trust Ladder release through one pull request, opened with the `KNOWLEDGE_SYNC_TOKEN` secret, and holds the workflow changes for a person to approve.
* [Knowledge website (knowledge-website.yaml)](workflows/knowledge-website.md) - The Knowledge website workflow, `.github/workflows/knowledge-website.yaml`: on pushes and pull requests that touch the site's sources, every Monday at 05:23 UTC and by hand, its build job builds `website/` and checks its links read-only, and its deploy job publishes the default branch's build to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is true.
* [Upstream watch (upstream-watch.yaml)](workflows/upstream-watch.md) - The Upstream watch workflow, `.github/workflows/upstream-watch.yaml`: every Monday at 07:00 UTC and by hand, its attestation-copy job runs `scripts/check_upstream_release.py` against in-toto/attestation's releases, and on a finding opens or updates the issue titled Upstream watch: the in-toto Attestation Framework has changed.

# Policies

* [Security policy](policies/security-policy.md) - How to report a vulnerability (GitHub's private vulnerability reporting), which release receives fixes (the latest), what executes in the repository and what holds each surface, the ruleset on `main`, and the two repository settings that are not yet in force.
* [AI covenant](policies/ai-covenant.md) - The repository's rules for work done with artificial intelligence (AI): you own what you submit, an element under the schema renders the in-toto specification in the project's own words and cites its page, the specification copy is never edited, and the scheduled librarian proposes changes only through reviewed pull requests.
* [License and attribution](policies/license-and-attribution.md) - The repository's licences: Apache 2.0 for the schema and the code, the in-toto project's Apache 2.0 for the specification copy, MIT for the copier template's scaffolding, and Apache 2.0 for the KTL sidecar and website templates.

# Playbooks

* [Cut a release](playbooks/release.md) - How a release is made: Conventional Commits on `main`, an `## [Unreleased]` changelog section, the `v0.0.0` baseline tag that keeps the first release at 0.1.0, and `semantic-release.yml`, which tags the release and dispatches Knowledge Release to attach `schema-<tag>-in-toto.yaml` once `KNOWLEDGE_RELEASE_ENABLED` is true.
* [Regenerate and test after a schema change](playbooks/regenerate-and-test.md) - How to change the schema and check it: `uv sync --group dev`, edit the modules under `src/in_toto_linkml/schema/`, then `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and the pre-commit hooks before a pull request.
* [Update the upstream pins](playbooks/update-upstream-pins.md) - What to do when the weekly upstream watch reports that in-toto/attestation released again, changed or dropped a pinned file, or moved the pinned tag, that the copy drifted, or that a check could not finish: replace the copy whole from one release, move the pins in `scripts/check_upstream_release.py` and the schema header, and run the tests.
* [Validate data against the schema](playbooks/validate-data.md) - How to validate in-toto data with `linkml-validate` before loading it into the generated Python models, which check less: the dataclasses check no pattern and read an empty required list as a missing one, the Pydantic models miss the timestamp's pattern, and neither checks a class's conditions. No check covers a repeated key, a mismatched predicate type or URI normalization.
* [Knowledge sources map](playbooks/knowledge-sources.md) - The librarian's scrape map: every repository location this bundle derives concepts from, the concepts each yields, how to re-check each on a refresh run, and the paths left out on purpose.

# Datasets

* [in-toto LinkML schema](datasets/in-toto-linkml-schema.md) - The LinkML schema of the in-toto Attestation Framework, `src/in_toto_linkml/schema/in_toto_linkml.yaml` (schema id `https://w3id.org/lmodel/in-toto`, version 1.2.0) with its modules `in_toto_core` and `in_toto_predicates`: 32 classes, two enums and one type. Its `lokf adapt` copy `.lokf/in-toto.yaml`, rooted on the predicate type, is the bundle's domain schema.
* [The in-toto specification copy](datasets/attestation-copy.md) - The specification pages and protocol buffer definitions of the in-toto Attestation Framework at release v1.2.0, 26 files copied with the in-toto project's licence into `src/in_toto_linkml/schema/attestation/` and matched to that release by git object hash. The tests hold every field of the copied definitions to a slot of the schema.
* [Generated artefacts](datasets/generated-artefacts.md) - What the LinkML generators and `lokf adapt` write from the schema: `project/` (JSON Schema, OWL, SHACL, ShEx, JSON-LD, GraphQL, protobuf, SQL, TypeScript, Excel and Java), the Python dataclasses and Pydantic models in `src/in_toto_linkml/datamodel/`, `docs/schema/` and `docs/elements/`, and `.lokf/in-toto.yaml`. None is edited by hand.
* [Test data and tests](datasets/test-data.md) - The schema's tests: 42 valid examples and 54 counter-examples under `tests/data/`, one example waiting under `problem/valid/`, `tests/test_data.py`, which holds each to the validator, `tests/test_upstream.py`, which holds the schema to the specification copy, `tests/test_watch.py`, which runs the upstream watch against stubbed answers, and `tests/test_schema_rules.py`, which holds the adapt copy apart from LOKF and the eight neighbours' copies in `tests/neighbours/`.

# References

* [The in-toto Attestation Framework](references/attestation-framework.md) - The in-toto Attestation Framework, release v1.2.0 of March 18, 2026, at <https://github.com/in-toto/attestation>: a specification for verifiable claims about how software is produced, in four layers, of which the schema renders the statement and the predicate.
* [The vetted predicates](references/vetted-predicates.md) - The in-toto project's list of vetted predicate types at release v1.2.0, thirteen in all, which `InTotoVettedPredicate` renders and the bundle describes one by one under predicate-types.

# Explanations

* [Scope, influences and mappings](explanations/scope-and-influences.md) - What the schema renders and what it leaves out: the statement layer and eight vetted predicates of the in-toto Attestation Framework at v1.2.0, with lmodel/slsa as its one influence on layout and names. It maps each predicate to its type URI, and models neither the envelope, the bundle, SLSA's two predicates nor the bill-of-materials predicates' bodies.
* [Element names and the shared namespace](explanations/element-names.md) - How the schema names its elements so that its adapt copy can sit beside LOKF's schema and the neighbours' copies: classes with the `InToto` prefix, the core's names as lmodel/slsa gave them, `statement_predicate` for the statement's predicate, `media_type` and `algorithm` with LOKF's IRIs, and the predicates' keys prefixed or named apart, which `tests/test_schema_rules.py` checks.

# Glossary

* [Statement](glossary/statement.md) - In the in-toto Attestation Framework, the middle layer of an attestation, which binds it to its subjects and names the type of its predicate. The schema renders it as `InTotoStatement`.
* [Resource descriptor](glossary/resource-descriptor.md) - In the in-toto Attestation Framework, a description of an artifact or other resource by URI, digest or content, with optional metadata. The schema renders it as `InTotoResourceDescriptor`.
* [Digest set](glossary/digest-set.md) - In the in-toto Attestation Framework, a set of digests over one artifact, keyed by algorithm, from which a consumer picks one it trusts. The schema renders it as `InTotoDigestSet`.
* [Predicate](glossary/predicate.md) - In the in-toto Attestation Framework, the innermost layer of an attestation: metadata about the statement's subjects, whose meaning its predicate type names. The schema's predicates extend `InTotoPredicate`.
* [Predicate type](glossary/predicate-type.md) - In the in-toto Attestation Framework, a type of predicate, named by a URI that a statement's predicateType holds and that changes with an incompatible change. The schema renders it as `InTotoPredicateType`, the class its adapt copy roots on `Concept`.

# Predicate-types

* [Test Result](predicate-types/test-result.md) - The vetted in-toto predicate type Test Result, `https://in-toto.io/attestation/test-result/v0.1`: the results of one run of a test suite against the subjects: the result, the configuration, and the tests that passed, warned and failed. The schema models it as `InTotoTestResult`.
* [Simple Verification Result](predicate-types/simple-verification-result.md) - The vetted in-toto predicate type Simple Verification Result, `https://in-toto.io/attestation/svr/v0.1`: that a verifier evaluated the subjects against one or more policies, and which properties passed. The schema models it as `InTotoSimpleVerificationResult`.
* [SCAI Report](predicate-types/scai.md) - The vetted in-toto predicate type SCAI Report, `https://in-toto.io/attestation/scai/v0.3`: assertions about functional attributes of the subjects or their producer, each with its evidence. The schema models it as `InTotoScaiAttributeReport`.
* [Link](predicate-types/link.md) - The vetted in-toto predicate type Link, `https://in-toto.io/attestation/link/v0.3`: one step of an in-toto layout, its command and its materials, for migration from in-toto 0.9. The schema models it as `InTotoLink`.
* [Reference](predicate-types/reference.md) - The vetted in-toto predicate type Reference, `https://in-toto.io/attestation/reference/v0.1`: references from the subjects, as a whole, to documents about them. The schema models it as `InTotoReference`.
* [Release](predicate-types/release.md) - The vetted in-toto predicate type Release, `https://in-toto.io/attestation/release/v0.1`: that the subjects are the artifacts of one release name and version of a package. The schema models it as `InTotoRelease`.
* [Runtime Traces](predicate-types/runtime-trace.md) - The vetted in-toto predicate type Runtime Traces, `https://in-toto.io/attestation/runtime-trace/v0.1`: what a monitor traced while a supply chain step ran. The schema models it as `InTotoRuntimeTrace`.
* [VULNS](predicate-types/vulns.md) - The vetted in-toto predicate type VULNS, `https://in-toto.io/attestation/vulns/v0.2`: the result of a vulnerability scan of the subjects. The schema models it as `InTotoVulns`.
* [SLSA Provenance](predicate-types/slsa-provenance.md) - The vetted in-toto predicate type SLSA Provenance, `https://slsa.dev/provenance/v1`: how an artifact or set of artifacts was produced. lmodel/slsa models it.
* [SLSA Verification Summary](predicate-types/slsa-verification-summary.md) - The vetted in-toto predicate type SLSA Verification Summary, `https://slsa.dev/verification_summary/v1`: a SLSA verification decision about a software artifact. lmodel/slsa models it.
* [CycloneDX](predicate-types/cyclonedx.md) - The vetted in-toto predicate type CycloneDX, `https://cyclonedx.org/bom/v1.4`: a CycloneDX bill of materials for software artifacts. The schema names it by type URI only, since its body is another specification's document.
* [SPDX2](predicate-types/spdx2.md) - The vetted in-toto predicate type SPDX2, `https://spdx.dev/Document/v2.3`: an SPDX 2 bill of materials for software artifacts. The schema names it by type URI only, since its body is another specification's document.
* [SPDX3](predicate-types/spdx3.md) - The vetted in-toto predicate type SPDX3, `https://spdx.dev/Document/v3`: an SPDX 3 bill of materials for software artifacts. The schema names it by type URI only, since its body is another specification's document.
