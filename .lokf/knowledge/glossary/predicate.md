---
type: GlossaryTerm
id: https://w3id.org/lmodel/in-toto/knowledge/glossary/predicate
genre: reference
title: Predicate
description: "In the in-toto Attestation Framework, the innermost layer of an attestation: metadata about the statement's subjects, whose meaning its predicate type names. The schema's predicates extend `InTotoPredicate`."
definition: The innermost layer of an attestation, metadata about the subjects whose meaning its type names.
resource: src/in_toto_linkml/schema/attestation/spec/v1/predicate.md
definedBy:
  - https://w3id.org/lmodel/in-toto/knowledge/references/attestation-framework
relatedTo:
  - https://w3id.org/lmodel/in-toto/knowledge/datasets/in-toto-linkml-schema
sources:
  - id: predicate
    resource: src/in_toto_linkml/schema/attestation/spec/v1/predicate.md
    title: the fields
  - id: in_toto_core
    resource: src/in_toto_linkml/schema/in_toto_core.yaml
    title: the class InTotoPredicate
generated:
  by: process:ktl-librarian
  at: "2026-10-30T16:14:35Z"
status: draft
---

# Predicate

The specification calls the predicate the innermost layer of the attestation, holding arbitrary metadata about the statement's subjects. Its `predicateType` says what it means, and its object holds parameters that depend on the type.[^predicate] In the schema every predicate extends the abstract `InTotoPredicate`, whose `predicate_kind` names the concrete class.[^in_toto_core]

[^predicate]: src/in_toto_linkml/schema/attestation/spec/v1/predicate.md, the fields
[^in_toto_core]: src/in_toto_linkml/schema/in_toto_core.yaml, InTotoPredicate
