---
type: InTotoPredicateType
id: https://w3id.org/lmodel/in-toto/knowledge/predicate-types/slsa-verification-summary
title: SLSA Verification Summary
description: "The vetted in-toto predicate type SLSA Verification Summary, `https://slsa.dev/verification_summary/v1`: a SLSA verification decision about a software artifact. lmodel/slsa models it."
predicate_type_uri: https://slsa.dev/verification_summary/v1
vetted_as: SLSA_VERIFICATION_SUMMARY
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
    title: the value SLSA_VERIFICATION_SUMMARY of InTotoVettedPredicate
generated:
  by: process:ktl-librarian
  at: "2026-10-30T16:14:35Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T21:20:44Z"
---

# SLSA Verification Summary

The predicates page lists SLSA Verification Summary among the vetted predicate types.[^predicates-readme] A statement of this type records a SLSA verification decision about a software artifact. lmodel/slsa models it, and this schema names it as `SLSA_VERIFICATION_SUMMARY` in `InTotoVettedPredicate`, with the type URI `https://slsa.dev/verification_summary/v1`.[^in_toto_predicates.yaml]

[^predicates-readme]: src/in_toto_linkml/schema/attestation/spec/predicates/README.md, Vetted Predicates
[^in_toto_predicates.yaml]: src/in_toto_linkml/schema/in_toto_predicates.yaml, InTotoVettedPredicate
