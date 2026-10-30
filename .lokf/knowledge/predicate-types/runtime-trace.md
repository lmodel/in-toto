---
type: InTotoPredicateType
id: https://w3id.org/lmodel/in-toto/knowledge/predicate-types/runtime-trace
title: Runtime Traces
description: "The vetted in-toto predicate type Runtime Traces, `https://in-toto.io/attestation/runtime-trace/v0.1`: what a monitor traced while a supply chain step ran. The schema models it as `InTotoRuntimeTrace`."
predicate_type_uri: https://in-toto.io/attestation/runtime-trace/v0.1
vetted_as: RUNTIME_TRACE
predicate_version: 0.1.0
predicate_specification: https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/runtime-trace.md
resource: src/in_toto_linkml/schema/attestation/spec/predicates/runtime-trace.md
definedBy:
  - https://w3id.org/lmodel/in-toto/knowledge/references/vetted-predicates
relatedTo:
  - https://w3id.org/lmodel/in-toto/knowledge/glossary/predicate-type
sources:
  - id: predicates-readme
    resource: src/in_toto_linkml/schema/attestation/spec/predicates/README.md
    title: the Vetted Predicates section
  - id: runtime-trace
    resource: src/in_toto_linkml/schema/attestation/spec/predicates/runtime-trace.md
    title: the type URI, the version and the schema
  - id: in_toto_predicates.yaml
    resource: src/in_toto_linkml/schema/in_toto_predicates.yaml
    title: the value RUNTIME_TRACE of InTotoVettedPredicate
generated:
  by: process:ktl-librarian
  at: "2026-10-30T16:14:35Z"
status: draft
---

# Runtime Traces

The predicates page lists Runtime Traces among the vetted predicate types.[^predicates-readme] A statement of this type records what a monitor traced while a supply chain step ran. Its page gives the type URI and version 0.1.0, and its statements carry `https://in-toto.io/attestation/runtime-trace/v0.1`.[^runtime-trace] The schema models it as `InTotoRuntimeTrace`, and names it as `RUNTIME_TRACE` in `InTotoVettedPredicate`.[^in_toto_predicates.yaml]

[^predicates-readme]: src/in_toto_linkml/schema/attestation/spec/predicates/README.md, Vetted Predicates
[^runtime-trace]: src/in_toto_linkml/schema/attestation/spec/predicates/runtime-trace.md, the type URI, the version and the schema
[^in_toto_predicates.yaml]: src/in_toto_linkml/schema/in_toto_predicates.yaml, InTotoVettedPredicate
