---
type: InTotoPredicateType
id: https://w3id.org/lmodel/in-toto/knowledge/predicate-types/vulns
title: VULNS
description: "The vetted in-toto predicate type VULNS, `https://in-toto.io/attestation/vulns/v0.2`: the result of a vulnerability scan of the subjects. The schema models it as `InTotoVulns`."
predicate_type_uri: https://in-toto.io/attestation/vulns/v0.2
vetted_as: VULNS
predicate_version: "0.2"
predicate_specification: https://github.com/in-toto/attestation/blob/v1.2.0/spec/predicates/vulns_02.md
resource: src/in_toto_linkml/schema/attestation/spec/predicates/vulns_02.md
definedBy:
  - https://w3id.org/lmodel/in-toto/knowledge/references/vetted-predicates
relatedTo:
  - https://w3id.org/lmodel/in-toto/knowledge/glossary/predicate-type
sources:
  - id: predicates-readme
    resource: src/in_toto_linkml/schema/attestation/spec/predicates/README.md
    title: the Vetted Predicates section
  - id: vulns_02
    resource: src/in_toto_linkml/schema/attestation/spec/predicates/vulns_02.md
    title: the type URI, the version and the schema
  - id: in_toto_predicates.yaml
    resource: src/in_toto_linkml/schema/in_toto_predicates.yaml
    title: the value VULNS of InTotoVettedPredicate
generated:
  by: process:ktl-librarian
  at: "2026-10-30T16:14:35Z"
status: draft
---

# VULNS

The predicates page lists VULNS among the vetted predicate types.[^predicates-readme] A statement of this type records the result of a vulnerability scan of the subjects. Its page gives the type URI and version 0.2, and its statements carry `https://in-toto.io/attestation/vulns/v0.2`.[^vulns_02] The schema models it as `InTotoVulns`, and names it as `VULNS` in `InTotoVettedPredicate`.[^in_toto_predicates.yaml]

[^predicates-readme]: src/in_toto_linkml/schema/attestation/spec/predicates/README.md, Vetted Predicates
[^vulns_02]: src/in_toto_linkml/schema/attestation/spec/predicates/vulns_02.md, the type URI, the version and the schema
[^in_toto_predicates.yaml]: src/in_toto_linkml/schema/in_toto_predicates.yaml, InTotoVettedPredicate
