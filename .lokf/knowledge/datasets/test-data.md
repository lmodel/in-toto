---
type: Dataset
id: https://w3id.org/lmodel/in-toto/knowledge/datasets/test-data
genre: reference
title: Test data and tests
description: "The schema's tests: 53 valid examples, ten of them the specification pages' own, and 57 counter-examples under `tests/data/`, one example waiting under `problem/valid/`, `tests/test_data.py`, which holds each to the validator, `tests/test_upstream.py`, which holds the schema to the specification copy, `tests/test_watch.py`, which runs the upstream watch against stubbed answers, and `tests/test_schema_rules.py`, which holds the adapt copy apart from LOKF and the eight neighbours' copies in `tests/neighbours/`."
resource: tests
sources:
  - id: test_data.py
    resource: tests/test_data.py
    title: the valid, invalid and coverage tests
  - id: data
    resource: tests/data
    title: the valid, invalid and problem folders
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: the copy and schema tests
  - id: test_watch.py
    resource: tests/test_watch.py
    title: the stubbed watch tests
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: the rule, neighbour and mapping tests
generated:
  by: process:ktl-librarian
  at: "2026-10-30T21:22:17Z"
status: draft
---

# Test data and tests

`tests/data/valid/` holds 53 examples and `tests/data/invalid/` 57 counter-examples, each named `ClassName-suffix.yaml` for the class it holds. Ten of the examples are the specification pages' own, in the schema's keys.[^data] `tests/test_data.py` loads each valid example into the generated dataclasses and validates it against the schema. It checks that each counter-example fails at the place its first line names, as `# Fails at: <JSON pointer>`, and that every class but the abstract predicate base has an example.[^test_data.py] There is a statement for each of the eight predicates. `tests/data/problem/valid/` holds a scan that found nothing, with an empty result list, which the validator accepts and the dataclasses read as a missing field.

`tests/test_upstream.py` checks the copy against the watch's pins, every field of each copied protocol buffer message against a slot, and the header's pins. It checks the vetted list against the predicates page, each predicate's type URI and each vetted value's meaning against its page, and each example taken from a page against that page's values.[^test_upstream.py] `tests/test_watch.py` runs the upstream watch against stubbed GitHub answers: a newer release, a dropped or changed file, a network failure, a truncated tree, an added predicate page, a moved tag, and a token that never follows a redirect.[^test_watch.py]

`tests/test_schema_rules.py` checks that the digest set's rules name every algorithm, and that every predicate is a kind of the statement's predicate. It holds the eight neighbours' copies in `tests/neighbours/` to their releases' checksums. It holds the adapt copy apart from LOKF's names and theirs, with two exceptions: the in-toto layer that slsa v0.7.0 still defines, and the keys `subject` and `value`, which the oscal and spdx copies share. It also checks that the copy roots only the predicate type and that every mapping uses a bound prefix.[^test_schema_rules.py]

[^data]: tests/data, valid, invalid and problem/valid
[^test_data.py]: tests/test_data.py, the valid, invalid and coverage tests
[^test_upstream.py]: tests/test_upstream.py, the copy and schema tests
[^test_watch.py]: tests/test_watch.py, the stubbed watch tests
[^test_schema_rules.py]: tests/test_schema_rules.py, the rule, neighbour and mapping tests
