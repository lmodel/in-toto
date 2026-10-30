---
type: GlossaryTerm
id: https://w3id.org/lmodel/in-toto/knowledge/glossary/resource-descriptor
genre: reference
title: Resource descriptor
description: In the in-toto Attestation Framework, a description of an artifact or other resource by URI, digest or content, with optional metadata. The schema renders it as `InTotoResourceDescriptor`.
definition: A description of a resource by URI, digest or content, with optional metadata.
resource: src/in_toto_linkml/schema/attestation/spec/v1/resource_descriptor.md
definedBy:
  - https://w3id.org/lmodel/in-toto/knowledge/references/attestation-framework
relatedTo:
  - https://w3id.org/lmodel/in-toto/knowledge/datasets/in-toto-linkml-schema
sources:
  - id: resource_descriptor
    resource: src/in_toto_linkml/schema/attestation/spec/v1/resource_descriptor.md
    title: the fields
  - id: in_toto_core
    resource: src/in_toto_linkml/schema/in_toto_core.yaml
    title: the class InTotoResourceDescriptor
generated:
  by: process:ktl-librarian
  at: "2026-10-30T16:14:35Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T21:20:44Z"
---

# Resource descriptor

The specification's resource descriptor names a resource by `uri`, `digest` or `content`, at least one of the three, and may add a `name`, a `downloadLocation`, a `mediaType` and `annotations`.[^resource_descriptor] The schema renders it as `InTotoResourceDescriptor`, with `resource_name`, `resource_uri`, `digest`, `content`, `download_location`, `media_type` and `annotations`, and requires one of the three through a condition.[^in_toto_core]

[^resource_descriptor]: src/in_toto_linkml/schema/attestation/spec/v1/resource_descriptor.md, the fields
[^in_toto_core]: src/in_toto_linkml/schema/in_toto_core.yaml, InTotoResourceDescriptor
