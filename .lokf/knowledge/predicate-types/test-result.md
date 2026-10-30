---
type: InTotoPredicateType
id: https://w3id.org/lmodel/in-toto/knowledge/predicate-types/test-result
title: Test Result
description: "The vetted in-toto predicate type Test Result, `https://in-toto.io/attestation/test-result/v0.1`: the results of one run of a test suite against the subjects: the result, the configuration, and the tests that passed, warned and failed. The schema models it as `InTotoTestResult`."
predicate_type_uri: https://in-toto.io/attestation/test-result/v0.1
vetted_as: TEST_RESULT
predicate_version: 0.1.0
predicate_specification: https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/test-result.md
resource: src/in_toto_linkml/schema/attestation/spec/predicates/test-result.md
definedBy:
  - https://w3id.org/lmodel/in-toto/knowledge/references/vetted-predicates
relatedTo:
  - https://w3id.org/lmodel/in-toto/knowledge/glossary/predicate-type
sources:
  - id: predicates-readme
    resource: src/in_toto_linkml/schema/attestation/spec/predicates/README.md
    title: the Vetted Predicates section
  - id: test-result
    resource: src/in_toto_linkml/schema/attestation/spec/predicates/test-result.md
    title: the type URI, the version and the schema
  - id: in_toto_predicates.yaml
    resource: src/in_toto_linkml/schema/in_toto_predicates.yaml
    title: the value TEST_RESULT of InTotoVettedPredicate
generated:
  by: process:ktl-librarian
  at: "2026-10-30T16:14:35Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T21:20:44Z"
---

# Test Result

The predicates page lists Test Result among the vetted predicate types.[^predicates-readme] A statement of this type records the results of one run of a test suite against the subjects: the result, the configuration, and the tests that passed, warned and failed. Its page gives the type URI and version 0.1.0, and its statements carry `https://in-toto.io/attestation/test-result/v0.1`.[^test-result] The schema models it as `InTotoTestResult`, and names it as `TEST_RESULT` in `InTotoVettedPredicate`.[^in_toto_predicates.yaml]

[^predicates-readme]: src/in_toto_linkml/schema/attestation/spec/predicates/README.md, Vetted Predicates
[^test-result]: src/in_toto_linkml/schema/attestation/spec/predicates/test-result.md, the type URI, the version and the schema
[^in_toto_predicates.yaml]: src/in_toto_linkml/schema/in_toto_predicates.yaml, InTotoVettedPredicate
