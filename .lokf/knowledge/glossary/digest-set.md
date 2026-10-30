---
type: GlossaryTerm
id: https://w3id.org/lmodel/in-toto/knowledge/glossary/digest-set
genre: reference
title: Digest set
description: In the in-toto Attestation Framework, a set of digests over one artifact, keyed by algorithm, from which a consumer picks one it trusts. The schema renders it as `InTotoDigestSet`.
definition: A set of digests over one artifact, keyed by algorithm.
resource: src/in_toto_linkml/schema/attestation/spec/v1/digest_set.md
definedBy:
  - https://w3id.org/lmodel/in-toto/knowledge/references/attestation-framework
relatedTo:
  - https://w3id.org/lmodel/in-toto/knowledge/datasets/in-toto-linkml-schema
sources:
  - id: digest_set
    resource: src/in_toto_linkml/schema/attestation/spec/v1/digest_set.md
    title: the supported algorithms and their encodings
  - id: in_toto_core
    resource: src/in_toto_linkml/schema/in_toto_core.yaml
    title: the class InTotoDigestSet
generated:
  by: process:ktl-librarian
  at: "2026-10-30T16:14:35Z"
status: draft
---

# Digest set

The specification's digest set holds one or more digests of one artifact, each under the name of its algorithm, and lists the algorithms it defines with their encodings.[^digest_set] The schema renders it as `InTotoDigestSet`, with one attribute per named algorithm and its length as a pattern, and `additional_digests` for any other algorithm, each an `InTotoAdditionalDigest`.[^in_toto_core]

[^digest_set]: src/in_toto_linkml/schema/attestation/spec/v1/digest_set.md, the algorithms
[^in_toto_core]: src/in_toto_linkml/schema/in_toto_core.yaml, InTotoDigestSet and InTotoAdditionalDigest
