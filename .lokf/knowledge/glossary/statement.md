---
type: GlossaryTerm
id: https://w3id.org/lmodel/in-toto/knowledge/glossary/statement
genre: reference
title: Statement
description: In the in-toto Attestation Framework, the middle layer of an attestation, which binds it to its subjects and names the type of its predicate. The schema renders it as `InTotoStatement`.
definition: The layer of an attestation that binds it to its subjects and names its predicate's type.
resource: src/in_toto_linkml/schema/attestation/spec/v1/statement.md
definedBy:
  - https://w3id.org/lmodel/in-toto/knowledge/references/attestation-framework
relatedTo:
  - https://w3id.org/lmodel/in-toto/knowledge/datasets/in-toto-linkml-schema
sources:
  - id: statement
    resource: src/in_toto_linkml/schema/attestation/spec/v1/statement.md
    title: the schema and the fields
  - id: in_toto_core
    resource: src/in_toto_linkml/schema/in_toto_core.yaml
    title: the class InTotoStatement
generated:
  by: process:ktl-librarian
  at: "2026-10-30T21:20:44Z"
status: draft
---

# Statement

The specification calls the statement the middle layer of the attestation, which binds it to a particular subject and identifies the type of its predicate. Its subjects must each carry a digest, and are assumed not to change.[^statement] The schema renders it as `InTotoStatement`, with `statement_type`, `subject`, `predicate_type` and the optional `predicate`, which the adapt copy renames `in_toto_linkml_predicate`.[^in_toto_core]

[^statement]: src/in_toto_linkml/schema/attestation/spec/v1/statement.md, the schema and the fields
[^in_toto_core]: src/in_toto_linkml/schema/in_toto_core.yaml, InTotoStatement
