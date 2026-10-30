---
type: Playbook
id: https://w3id.org/lmodel/in-toto/knowledge/playbooks/validate-data
genre: how-to
title: Validate data against the schema
description: "How to validate in-toto data with `linkml-validate` before loading it into the generated Python models, which check less: the dataclasses check no pattern and read an empty required list as a missing one, the Pydantic models miss the timestamp's pattern, and neither checks a class's conditions. No check covers a repeated key, a mismatched predicate type or URI normalization."
resource: docs/index.md
about:
  - https://w3id.org/lmodel/in-toto/knowledge/datasets/in-toto-linkml-schema
sources:
  - id: docs-index.md
    resource: docs/index.md
    title: the Validating data section
generated:
  by: process:ktl-librarian
  at: "2026-10-30T16:14:35Z"
status: draft
---

# Validate data against the schema

Run `linkml-validate -s src/in_toto_linkml/schema/in_toto_linkml.yaml -C InTotoStatement attestation.yaml`, naming the class the file holds. It checks the file against the JSON Schema the validator generates from the schema, and `tests/test_data.py` holds every example to the same check.[^docs-index.md]

Validate a file before loading it into either model in `src/in_toto_linkml/datamodel/`. The page says that the models LinkML 1.12.1 generates check less:

- the dataclasses check required fields and enum values, but no pattern, and read an empty required list, such as a scan's empty `scan_results`, as a missing one;
- the Pydantic models also check the patterns a field carries itself, such as the digest lengths and `release_purl`, but not the pattern of the `InTotoTimestamp` type;
- neither checks a class's `any_of` or `all_of` conditions, such as the digest set's one digest at least.

No check covers five rules:

- a key appears once in a list of annotations, additional digests or object entries;
- the subjects' names and URIs, and a link's materials' names, are unique;
- a statement's `predicate_type` is the type URI of the predicate its `predicate_kind` names;
- a URI is case-normalized as RFC 3986 asks, and a timestamp is a real date and time;
- a release's package URL carries no qualifiers or subpath unless its type needs them, and inline content stays under 1 KB.

[^docs-index.md]: docs/index.md, Validating data
