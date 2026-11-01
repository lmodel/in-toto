# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change bumps the minor version. See [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers).

## [Unreleased]

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
