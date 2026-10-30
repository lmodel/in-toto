---
type: Reference
id: https://w3id.org/lmodel/in-toto/knowledge/references/vetted-predicates
genre: reference
title: The vetted predicates
description: The in-toto project's list of vetted predicate types at release v1.2.0, thirteen in all, which `InTotoVettedPredicate` renders and the bundle describes one by one under predicate-types.
resource: src/in_toto_linkml/schema/attestation/spec/predicates/README.md
sources:
  - id: predicates-readme
    resource: src/in_toto_linkml/schema/attestation/spec/predicates/README.md
    title: the Vetted Predicates section
generated:
  by: process:ktl-librarian
  at: "2026-10-30T16:14:35Z"
status: draft
---

# The vetted predicates

The predicates page of in-toto/attestation encourages users to choose an existing predicate type, and lists the ones that have gone through the project's vetting process.[^predicates-readme] At release v1.2.0 they are thirteen: CycloneDX, Link, Reference, Release, Runtime Traces, SCAI Report, SLSA Provenance, SLSA Verification Summary, SPDX2, SPDX3, Simple Verification Result, Test Result and VULNS.

The schema names all thirteen in `InTotoVettedPredicate`, and models eight of their predicates. lmodel/slsa models the two SLSA ones, and the CycloneDX, SPDX 2 and SPDX 3 predicates carry a whole bill of materials in another format. The bundle describes each type under [predicate types](../predicate-types/index.md).

[^predicates-readme]: src/in_toto_linkml/schema/attestation/spec/predicates/README.md, Vetted Predicates
