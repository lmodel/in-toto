---
type: InTotoPredicateType
id: https://w3id.org/lmodel/in-toto/knowledge/predicate-types/cyclonedx
title: CycloneDX
description: "The vetted in-toto predicate type CycloneDX, `https://cyclonedx.org/bom/v1.4`: a CycloneDX bill of materials for software artifacts. The schema names it by type URI only, since its body is another specification's document."
predicate_type_uri: https://cyclonedx.org/bom/v1.4
vetted_as: CYCLONEDX
resource: src/in_toto_linkml/schema/in_toto_predicates.yaml
definedBy:
  - https://w3id.org/lmodel/in-toto/knowledge/references/vetted-predicates
relatedTo:
  - https://w3id.org/lmodel/in-toto/knowledge/glossary/predicate-type
sources:
  - id: predicates-readme
    resource: src/in_toto_linkml/schema/attestation/spec/predicates/README.md
    title: the Vetted Predicates section
  - id: in_toto_predicates.yaml
    resource: src/in_toto_linkml/schema/in_toto_predicates.yaml
    title: the value CYCLONEDX of InTotoVettedPredicate
generated:
  by: process:ktl-librarian
  at: "2026-10-30T16:14:35Z"
status: draft
---

# CycloneDX

The predicates page lists CycloneDX among the vetted predicate types.[^predicates-readme] A statement of this type records a CycloneDX bill of materials for software artifacts. Its body is a whole bill of materials in another specification's format, so the schema names it as `CYCLONEDX` in `InTotoVettedPredicate`, with the type URI `https://cyclonedx.org/bom/v1.4`, and models no class for it.[^in_toto_predicates.yaml]

[^predicates-readme]: src/in_toto_linkml/schema/attestation/spec/predicates/README.md, Vetted Predicates
[^in_toto_predicates.yaml]: src/in_toto_linkml/schema/in_toto_predicates.yaml, InTotoVettedPredicate
