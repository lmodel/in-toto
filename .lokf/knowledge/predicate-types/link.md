---
type: InTotoPredicateType
id: https://w3id.org/lmodel/in-toto/knowledge/predicate-types/link
title: Link
description: "The vetted in-toto predicate type Link, `https://in-toto.io/attestation/link/v0.3`: one step of an in-toto layout, its command and its materials, for migration from in-toto 0.9. The schema models it as `InTotoLink`."
predicate_type_uri: https://in-toto.io/attestation/link/v0.3
vetted_as: LINK
predicate_version: "0.3"
predicate_specification: https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/link.md
resource: src/in_toto_linkml/schema/attestation/spec/predicates/link.md
definedBy:
  - https://w3id.org/lmodel/in-toto/knowledge/references/vetted-predicates
relatedTo:
  - https://w3id.org/lmodel/in-toto/knowledge/glossary/predicate-type
sources:
  - id: predicates-readme
    resource: src/in_toto_linkml/schema/attestation/spec/predicates/README.md
    title: the Vetted Predicates section
  - id: link
    resource: src/in_toto_linkml/schema/attestation/spec/predicates/link.md
    title: the type URI, the version and the schema
  - id: in_toto_predicates.yaml
    resource: src/in_toto_linkml/schema/in_toto_predicates.yaml
    title: the value LINK of InTotoVettedPredicate
generated:
  by: process:ktl-librarian
  at: "2026-10-30T16:14:35Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T21:20:44Z"
---

# Link

The predicates page lists Link among the vetted predicate types.[^predicates-readme] A statement of this type records one step of an in-toto layout, its command and its materials, for migration from in-toto 0.9. Its page gives the type URI and version 0.3, and its statements carry `https://in-toto.io/attestation/link/v0.3`.[^link] The schema models it as `InTotoLink`, and names it as `LINK` in `InTotoVettedPredicate`.[^in_toto_predicates.yaml]

[^predicates-readme]: src/in_toto_linkml/schema/attestation/spec/predicates/README.md, Vetted Predicates
[^link]: src/in_toto_linkml/schema/attestation/spec/predicates/link.md, the type URI, the version and the schema
[^in_toto_predicates.yaml]: src/in_toto_linkml/schema/in_toto_predicates.yaml, InTotoVettedPredicate
