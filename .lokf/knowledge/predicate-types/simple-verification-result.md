---
type: InTotoPredicateType
id: https://w3id.org/lmodel/in-toto/knowledge/predicate-types/simple-verification-result
title: Simple Verification Result
description: "The vetted in-toto predicate type Simple Verification Result, `https://in-toto.io/attestation/svr/v0.1`: that a verifier evaluated the subjects against one or more policies, and which properties passed. The schema models it as `InTotoSimpleVerificationResult`."
predicate_type_uri: https://in-toto.io/attestation/svr/v0.1
vetted_as: SIMPLE_VERIFICATION_RESULT
predicate_version: "0.1"
predicate_specification: https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/svr.md
resource: src/in_toto_linkml/schema/attestation/spec/predicates/svr.md
definedBy:
  - https://w3id.org/lmodel/in-toto/knowledge/references/vetted-predicates
relatedTo:
  - https://w3id.org/lmodel/in-toto/knowledge/glossary/predicate-type
sources:
  - id: predicates-readme
    resource: src/in_toto_linkml/schema/attestation/spec/predicates/README.md
    title: the Vetted Predicates section
  - id: svr
    resource: src/in_toto_linkml/schema/attestation/spec/predicates/svr.md
    title: the type URI, the version and the schema
  - id: in_toto_predicates.yaml
    resource: src/in_toto_linkml/schema/in_toto_predicates.yaml
    title: the value SIMPLE_VERIFICATION_RESULT of InTotoVettedPredicate
generated:
  by: process:ktl-librarian
  at: "2026-10-30T16:14:35Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T21:20:44Z"
---

# Simple Verification Result

The predicates page lists Simple Verification Result among the vetted predicate types.[^predicates-readme] A statement of this type records that a verifier evaluated the subjects against one or more policies, and which properties passed. Its page gives the type URI and version 0.1, and its statements carry `https://in-toto.io/attestation/svr/v0.1`.[^svr] The schema models it as `InTotoSimpleVerificationResult`, and names it as `SIMPLE_VERIFICATION_RESULT` in `InTotoVettedPredicate`.[^in_toto_predicates.yaml]

[^predicates-readme]: src/in_toto_linkml/schema/attestation/spec/predicates/README.md, Vetted Predicates
[^svr]: src/in_toto_linkml/schema/attestation/spec/predicates/svr.md, the type URI, the version and the schema
[^in_toto_predicates.yaml]: src/in_toto_linkml/schema/in_toto_predicates.yaml, InTotoVettedPredicate
