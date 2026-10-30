---
type: InTotoPredicateType
id: https://w3id.org/lmodel/in-toto/knowledge/predicate-types/release
title: Release
description: "The vetted in-toto predicate type Release, `https://in-toto.io/attestation/release/v0.1`: that the subjects are the artifacts of one release name and version of a package. The schema models it as `InTotoRelease`."
predicate_type_uri: https://in-toto.io/attestation/release/v0.1
vetted_as: RELEASE
predicate_version: "0.2"
predicate_specification: https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/release.md
resource: src/in_toto_linkml/schema/attestation/spec/predicates/release.md
definedBy:
  - https://w3id.org/lmodel/in-toto/knowledge/references/vetted-predicates
relatedTo:
  - https://w3id.org/lmodel/in-toto/knowledge/glossary/predicate-type
sources:
  - id: predicates-readme
    resource: src/in_toto_linkml/schema/attestation/spec/predicates/README.md
    title: the Vetted Predicates section
  - id: release
    resource: src/in_toto_linkml/schema/attestation/spec/predicates/release.md
    title: the type URI, the version and the schema
  - id: in_toto_predicates.yaml
    resource: src/in_toto_linkml/schema/in_toto_predicates.yaml
    title: the value RELEASE of InTotoVettedPredicate
generated:
  by: process:ktl-librarian
  at: "2026-10-30T16:14:35Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T21:20:44Z"
---

# Release

The predicates page lists Release among the vetted predicate types.[^predicates-readme] A statement of this type records that the subjects are the artifacts of one release name and version of a package. Its page is at version 0.2, which renamed `releaseId` to `packageId`, and its examples keep the type URI `https://in-toto.io/attestation/release/v0.1`.[^release] The schema models it as `InTotoRelease`, and names it as `RELEASE` in `InTotoVettedPredicate`.[^in_toto_predicates.yaml]

[^predicates-readme]: src/in_toto_linkml/schema/attestation/spec/predicates/README.md, Vetted Predicates
[^release]: src/in_toto_linkml/schema/attestation/spec/predicates/release.md, the type URI, the version and the schema
[^in_toto_predicates.yaml]: src/in_toto_linkml/schema/in_toto_predicates.yaml, InTotoVettedPredicate
