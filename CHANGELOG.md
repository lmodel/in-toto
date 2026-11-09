# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change bumps the minor version. See [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers).

## [Unreleased]

### Security

- **The sidecar copies and the skills pin are at Knowledge Trust Ladder [v0.62.0](https://github.com/noelmcloughlin/knowledge-trust-ladder/compare/v0.60.0...v0.62.0).** The release changed `.github/workflows/knowledge-registrar.yaml`, `.github/workflows/knowledge-librarian.yaml`, `.github/workflows/knowledge-release.yaml`, `.github/workflows/knowledge-sync.yaml`, `.lokf/scripts/knowledge-librarian.sh`, `.lokf/scripts/knowledge-conventions.sh`, `.lokf/scripts/knowledge-conventions.py`, `.lokf/scripts/knowledge-preflight.sh`, `.lokf/scripts/knowledge-provenance.sh`, `.lokf/scripts/knowledge-apply.py`, `.lokf/scripts/knowledge-report.sh`, `.lokf/scripts/knowledge-sync.sh`, `.lokf/justfile`, `website/scripts/sync.mjs` and `.github/workflows/knowledge-website.yaml` here.

## [0.4.0] - 2026-11-07

### Added

- **The schema as RDF Turtle and the merged schema**, in `project/rdf/` and `project/linkml/`, from `just gen-rdf` and `just gen-merged-schema`.

### Changed

- **The bundle's schema files sit in `.lokf/schema/`**: `lokf.yaml` and the `lokf adapt` copy `in-toto.yaml`, as KTL v0.62.0 lays them out.

## [0.3.1] - 2026-11-02

### Security

- **The sidecar copies and the skills pin are at Knowledge Trust Ladder [v0.60.0](https://github.com/noelmcloughlin/knowledge-trust-ladder/compare/v0.59.0...v0.60.0).** The release changed `.github/workflows/knowledge-registrar.yaml`, `.github/workflows/knowledge-librarian.yaml`, `.github/workflows/knowledge-release.yaml`, `.github/workflows/knowledge-sync.yaml`, `.lokf/scripts/knowledge-preflight.sh`, `.lokf/.gitignore`, `.lokf/justfile`, `website/package-lock.json`, `website/package.json`, `website/scripts/config.mjs`, `website/scripts/sync.mjs` and `.github/workflows/knowledge-website.yaml` here.

## [0.3.0] - 2026-11-01

### Added

- **EARL outcomes and BLAKE2b's SPDX lengths.** The Test Result values `PASSED` and `FAILED` mean W3C EARL 1.0's `passed` and `failed`, and `blake2b` relates to SPDX's three BLAKE2b individuals, since the framework allows any length from 32 to 64 bytes.

## [0.2.1] - 2026-11-01

### Fixed

- **The Pydantic model imports.** The two URI types leave `base: URI` commented out, with a link to [linkml#3491](https://github.com/linkml/linkml/issues/3491), because `gen-pydantic` wrote it as an annotation it never imported. They now take `str` from `uri`, and a test imports the model.

## [0.2.0] - 2026-11-01

### Added

- **Mappings to SPDX 3.0.1 and DCAT, and the statement's own type URI.** Close and related mappings link annotations, download locations, media types, package URLs, build times, digests and vulnerability results to the SPDX terms lmodel/spdx renders, and a test holds each to that release.
- **The framework's names as aliases**: the message name on each class and the JSON key on each field whose name differs, held to the protocol buffer definitions by a test.
- **A language, keywords, and disjoint predicate kinds.** Each module states `in_language` and `keywords`, and the classes that extend `InTotoPredicate` are mutually disjoint in the generated ontology.

## [0.1.1] - 2026-10-30

### Fixed

- **The comment on the statement's `predicate` slot names each adapt copy's rename.** It said every copy beside LOKF calls the slot `in_toto_linkml_predicate`, but `lokf adapt` prefixes the adapted schema's name, so lmodel/slsa's copy calls it `slsa_predicate`.

## [0.1.0] - 2026-10-30

### Added

- **A LinkML schema of the in-toto Attestation Framework at release v1.2.0.** The core module holds the statement, the resource descriptor, the digest set and the framework's URI and timestamp types, with the names lmodel/slsa gave the layer, so slsa can import it; the predicates module holds the thirteen vetted predicate types and the eight vetted predicates slsa does not model.
- **A copy of the framework's specification pages and protocol buffer definitions at v1.2.0, and a weekly upstream watch.** Tests hold every field of the copied definitions to a slot, and the watch reports a new release, a changed or dropped file, or a drifted copy.
- **`.lokf/in-toto.yaml`, the schema's `lokf adapt` copy, rooted on the predicate type.** The knowledge release attaches it as `schema-<tag>-in-toto.yaml`, and tests hold its names apart from those of the Linked Open Knowledge Format (LOKF) and the released neighbours' copies, except for the layer slsa v0.7.0 still defines.
- **An example of each class and a counter-example for each constraint**, held to the validator by `just test`.
- **The repository's Knowledge Trust Ladder (KTL) knowledge bundle and its sidecar automation**, from the KTL v0.59.0 templates with the lokf floor at 0.9.0, and a knowledge website in place of the template's mkdocs site.
- **`.github/release/package-lock.json`, which pins semantic-release and every package it pulls in.** The release job installs from it with `npm ci`, and Dependabot keeps it current.

### Changed

- **`media_type` and `algorithm` carry LOKF's IRIs, and the statement's `predicate` is a slot of its own.** slsa v0.7.0 gave the first two IRIs of its own for what LOKF's mean. The adapt copy renames `predicate` to `in_toto_linkml_predicate`, apart from LOKF's relation type, so a slsa v0.7.0 document keeps its `predicate` key.
- **The Python package and schema are named `in_toto_linkml`, and the Python project `in-toto-linkml`**, because the in-toto reference implementation installs `in_toto`. PyPI publishing stays off.
