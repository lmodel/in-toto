---
type: Reference
id: https://w3id.org/lmodel/in-toto/knowledge/references/attestation-framework
genre: reference
title: The in-toto Attestation Framework
description: "The in-toto Attestation Framework, release v1.2.0 of March 18, 2026, at <https://github.com/in-toto/attestation>: a specification for verifiable claims about how software is produced, in four layers, of which the schema renders the statement and the predicate."
resource: src/in_toto_linkml/schema/attestation/spec/v1/README.md
sources:
  - id: spec-readme
    resource: src/in_toto_linkml/schema/attestation/spec/v1/README.md
    title: the overview of the layers
  - id: statement.md
    resource: src/in_toto_linkml/schema/attestation/spec/v1/statement.md
    title: the fields of the statement
  - id: changelog
    resource: src/in_toto_linkml/schema/attestation/spec/v1/CHANGELOG.md
    title: the v1.1 and v1.2 entries
generated:
  by: process:ktl-librarian
  at: "2026-10-30T16:14:35Z"
status: draft
---

# The in-toto Attestation Framework

The in-toto project publishes the in-toto Attestation Framework at <https://github.com/in-toto/attestation>. Its v1 specification describes an attestation in layers: the predicate, the statement that binds it to its subjects, the envelope that signs the statement, and the bundle that collects attestations.[^spec-readme] The statement's `_type` is always `https://in-toto.io/Statement/v1`, its `subject` lists the artifacts it applies to, each with a digest and matched by digest alone, and its `predicateType` names the predicate's type by URI.[^statement.md]

Release v1.2.0 of March 18, 2026 is the one the schema renders. Its changelog says that v1.2 widened the envelope's allowed payload types, and that v1.1 clarified that subjects are immutable and that a non-cryptographic digest is acceptable.[^changelog] The schema leaves the envelope and the bundle out. [The in-toto specification copy](../datasets/attestation-copy.md) holds the pages it renders.

[^spec-readme]: src/in_toto_linkml/schema/attestation/spec/v1/README.md, the overview
[^statement.md]: src/in_toto_linkml/schema/attestation/spec/v1/statement.md, the fields
[^changelog]: src/in_toto_linkml/schema/attestation/spec/v1/CHANGELOG.md, v1.2 and v1.1
