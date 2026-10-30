---
type: Explanation
id: https://w3id.org/lmodel/in-toto/knowledge/explanations/element-names
genre: explanation
title: Element names and the shared namespace
description: "How the schema names its elements so that its adapt copy can sit beside LOKF's schema and the neighbours' copies: classes with the `InToto` prefix, the core's names as lmodel/slsa gave them, the statement's `predicate`, which the copy renames `in_toto_linkml_predicate`, `media_type` and `algorithm` with LOKF's IRIs, and the predicates' keys prefixed or named apart, which `tests/test_schema_rules.py` checks."
resource: docs/about.md
about:
  - https://w3id.org/lmodel/in-toto/knowledge/datasets/in-toto-linkml-schema
sources:
  - id: about.md
    resource: docs/about.md
    title: the Names section
  - id: readme.md
    resource: README.md
    title: the Knowledge Trust Ladder (KTL) section
  - id: linkmllint.yaml
    resource: .linkmllint.yaml
    title: the comment and the one changed rule
generated:
  by: process:ktl-librarian
  at: "2026-10-30T21:22:17Z"
status: draft
---

# Element names and the shared namespace

Every class carries the `InToto` prefix and lives under `in_toto_linkml:`, `https://w3id.org/lmodel/in-toto/`. The core keeps the class and slot names lmodel/slsa gave the layer, which follow the attestation's JSON in snake case, such as `statement_type` for `_type` and `resource_uri` for `uri`.[^about.md]

Three keys are also LOKF's, so the adapt copy treats them apart. `media_type` carries DCAT's `mediaType`, and `algorithm` carries SPDX 2's `algorithm`: the IRIs LOKF gives the same keys. The statement's `predicate` keeps in-toto's name and its own IRI. It is a slot of its own, so `lokf adapt` renames it `in_toto_linkml_predicate` in the copy, because LOKF's `predicate` is the type of a relation. The predicates' keys carry their predicate's prefix, such as `scai_attribute`, or a noun of their own, such as `test_run_url`, so two predicates never give one key two meanings.

The README says that a host imports the copy beside `lokf.yaml` and other copies, which LinkML merges into one namespace. The copy shares `subject` and `value` with the oscal and spdx copies, as slsa v0.7.0 does. It also shares the in-toto layer with slsa v0.7.0, which defines that layer until its next release imports it from here.[^readme.md]

`.linkmllint.yaml` changes one rule: enum values are upper case, as the framework's `PASSED`, `WARNED` and `FAILED` are.[^linkmllint.yaml]

[^about.md]: docs/about.md, Names
[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
[^linkmllint.yaml]: .linkmllint.yaml, the comment and standard_naming
