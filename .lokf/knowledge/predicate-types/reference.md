---
type: InTotoPredicateType
id: https://w3id.org/lmodel/in-toto/knowledge/predicate-types/reference
title: Reference
description: "The vetted in-toto predicate type Reference, `https://in-toto.io/attestation/reference/v0.1`: references from the subjects, as a whole, to documents about them. The schema models it as `InTotoReference`."
predicate_type_uri: https://in-toto.io/attestation/reference/v0.1
vetted_as: REFERENCE
predicate_version: v0.1.0
predicate_specification: https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/reference.md
resource: src/in_toto_linkml/schema/attestation/spec/predicates/reference.md
definedBy:
  - https://w3id.org/lmodel/in-toto/knowledge/references/vetted-predicates
relatedTo:
  - https://w3id.org/lmodel/in-toto/knowledge/glossary/predicate-type
sources:
  - id: predicates-readme
    resource: src/in_toto_linkml/schema/attestation/spec/predicates/README.md
    title: the Vetted Predicates section
  - id: reference
    resource: src/in_toto_linkml/schema/attestation/spec/predicates/reference.md
    title: the type URI, the version and the schema
  - id: in_toto_predicates.yaml
    resource: src/in_toto_linkml/schema/in_toto_predicates.yaml
    title: the value REFERENCE of InTotoVettedPredicate
generated:
  by: process:ktl-librarian
  at: "2026-10-30T16:14:35Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T21:20:44Z"
---

# Reference

The predicates page lists Reference among the vetted predicate types.[^predicates-readme] A statement of this type records references from the subjects, as a whole, to documents about them. Its page gives the type URI and version v0.1.0, and its statements carry `https://in-toto.io/attestation/reference/v0.1`.[^reference] The schema models it as `InTotoReference`, and names it as `REFERENCE` in `InTotoVettedPredicate`.[^in_toto_predicates.yaml]

[^predicates-readme]: src/in_toto_linkml/schema/attestation/spec/predicates/README.md, Vetted Predicates
[^reference]: src/in_toto_linkml/schema/attestation/spec/predicates/reference.md, the type URI, the version and the schema
[^in_toto_predicates.yaml]: src/in_toto_linkml/schema/in_toto_predicates.yaml, InTotoVettedPredicate
