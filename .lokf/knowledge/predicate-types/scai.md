---
type: InTotoPredicateType
id: https://w3id.org/lmodel/in-toto/knowledge/predicate-types/scai
title: SCAI Report
description: "The vetted in-toto predicate type SCAI Report, `https://in-toto.io/attestation/scai/v0.3`: assertions about functional attributes of the subjects or their producer, each with its evidence. The schema models it as `InTotoScaiAttributeReport`."
predicate_type_uri: https://in-toto.io/attestation/scai/v0.3
vetted_as: SCAI
predicate_version: "0.3"
predicate_specification: https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/scai.md
resource: src/in_toto_linkml/schema/attestation/spec/predicates/scai.md
definedBy:
  - https://w3id.org/lmodel/in-toto/knowledge/references/vetted-predicates
relatedTo:
  - https://w3id.org/lmodel/in-toto/knowledge/glossary/predicate-type
sources:
  - id: predicates-readme
    resource: src/in_toto_linkml/schema/attestation/spec/predicates/README.md
    title: the Vetted Predicates section
  - id: scai
    resource: src/in_toto_linkml/schema/attestation/spec/predicates/scai.md
    title: the type URI, the version and the schema
  - id: in_toto_predicates.yaml
    resource: src/in_toto_linkml/schema/in_toto_predicates.yaml
    title: the value SCAI of InTotoVettedPredicate
generated:
  by: process:ktl-librarian
  at: "2026-10-30T16:14:35Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T21:20:44Z"
---

# SCAI Report

The predicates page lists SCAI Report among the vetted predicate types.[^predicates-readme] A statement of this type records assertions about functional attributes of the subjects or their producer, each with its evidence. Its page gives the type URI and version 0.3, and its statements carry `https://in-toto.io/attestation/scai/v0.3`.[^scai] The schema models it as `InTotoScaiAttributeReport`, and names it as `SCAI` in `InTotoVettedPredicate`.[^in_toto_predicates.yaml]

[^predicates-readme]: src/in_toto_linkml/schema/attestation/spec/predicates/README.md, Vetted Predicates
[^scai]: src/in_toto_linkml/schema/attestation/spec/predicates/scai.md, the type URI, the version and the schema
[^in_toto_predicates.yaml]: src/in_toto_linkml/schema/in_toto_predicates.yaml, InTotoVettedPredicate
