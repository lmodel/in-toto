---
type: InTotoPredicateType
id: https://w3id.org/lmodel/in-toto/knowledge/predicate-types/spdx3
title: SPDX3
description: "The vetted in-toto predicate type SPDX3, `https://spdx.dev/Document/v3`: an SPDX 3 bill of materials for software artifacts. The schema names it by type URI only, since its body is another specification's document."
predicate_type_uri: https://spdx.dev/Document/v3
vetted_as: SPDX3
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
    title: the value SPDX3 of InTotoVettedPredicate
generated:
  by: process:ktl-librarian
  at: "2026-10-30T16:14:35Z"
status: draft
---

# SPDX3

The predicates page lists SPDX3 among the vetted predicate types.[^predicates-readme] A statement of this type records an SPDX 3 bill of materials for software artifacts. Its body is a whole bill of materials in another specification's format, so the schema names it as `SPDX3` in `InTotoVettedPredicate`, with the type URI `https://spdx.dev/Document/v3`, and models no class for it.[^in_toto_predicates.yaml]

[^predicates-readme]: src/in_toto_linkml/schema/attestation/spec/predicates/README.md, Vetted Predicates
[^in_toto_predicates.yaml]: src/in_toto_linkml/schema/in_toto_predicates.yaml, InTotoVettedPredicate
