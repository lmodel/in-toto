---
type: GlossaryTerm
id: https://w3id.org/lmodel/in-toto/knowledge/glossary/predicate-type
genre: reference
title: Predicate type
description: In the in-toto Attestation Framework, a type of predicate, named by a URI that a statement's predicateType holds and that changes with an incompatible change. The schema renders it as `InTotoPredicateType`, the class its adapt copy roots on `Concept`.
definition: A type of predicate, named by a URI that includes its major version.
resource: src/in_toto_linkml/schema/attestation/spec/v1/field_types.md
definedBy:
  - https://w3id.org/lmodel/in-toto/knowledge/references/attestation-framework
relatedTo:
  - https://w3id.org/lmodel/in-toto/knowledge/datasets/in-toto-linkml-schema
sources:
  - id: field_types
    resource: src/in_toto_linkml/schema/attestation/spec/v1/field_types.md
    title: TypeURI
  - id: in_toto_predicates
    resource: src/in_toto_linkml/schema/in_toto_predicates.yaml
    title: the class InTotoPredicateType
generated:
  by: process:ktl-librarian
  at: "2026-10-30T16:14:35Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T21:20:44Z"
---

# Predicate type

A statement names its predicate's type with a TypeURI, a case-normalized URI that should resolve to a description and include a version number. The specification adds that type URIs are not registered, since URIs' own namespacing prevents collisions.[^field_types] The schema renders a predicate type as `InTotoPredicateType`, with `predicate_type_uri`, `predicate_version`, `predicate_specification` and `vetted_as`, and its adapt copy roots this class on `Concept`, so a concept can be a predicate type.[^in_toto_predicates] The bundle describes the vetted ones under [predicate types](../predicate-types/index.md).

[^field_types]: src/in_toto_linkml/schema/attestation/spec/v1/field_types.md, TypeURI
[^in_toto_predicates]: src/in_toto_linkml/schema/in_toto_predicates.yaml, InTotoPredicateType
