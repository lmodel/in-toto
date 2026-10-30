---
type: InTotoPredicateType
id: https://w3id.org/lmodel/in-toto/knowledge/predicate-types/spdx2
title: SPDX2
description: "The vetted in-toto predicate type SPDX2, `https://spdx.dev/Document/v2.3`: an SPDX 2 bill of materials for software artifacts. The schema names it by type URI only, since its body is another specification's document."
predicate_type_uri: https://spdx.dev/Document/v2.3
vetted_as: SPDX2
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
    title: the value SPDX2 of InTotoVettedPredicate
generated:
  by: process:ktl-librarian
  at: "2026-10-30T16:14:35Z"
status: draft
---

# SPDX2

The predicates page lists SPDX2 among the vetted predicate types.[^predicates-readme] A statement of this type records an SPDX 2 bill of materials for software artifacts. Its body is a whole bill of materials in another specification's format, so the schema names it as `SPDX2` in `InTotoVettedPredicate`, with the type URI `https://spdx.dev/Document/v2.3`, and models no class for it.[^in_toto_predicates.yaml]

[^predicates-readme]: src/in_toto_linkml/schema/attestation/spec/predicates/README.md, Vetted Predicates
[^in_toto_predicates.yaml]: src/in_toto_linkml/schema/in_toto_predicates.yaml, InTotoVettedPredicate
