---
type: Dataset
id: https://w3id.org/lmodel/in-toto/knowledge/datasets/test-data
genre: reference
title: Test data and tests
description: "The schema's tests: 42 valid examples and 54 counter-examples under `tests/data/`, one example waiting under `problem/valid/`, `tests/test_data.py`, which holds each to the validator, `tests/test_upstream.py`, which holds the schema to the specification copy, `tests/test_watch.py`, which runs the upstream watch against stubbed answers, and `tests/test_schema_rules.py`, which holds the adapt copy apart from LOKF and the eight neighbours' copies in `tests/neighbours/`."
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
  at: "2026-10-30T16:14:35Z"
status: draft
---

# Test data and tests

`tests/data/valid/` holds 42 examples and `tests/data/invalid/` 54 counter-examples, each named `ClassName-suffix.yaml` for the class it holds.[^data] `tests/test_data.py` loads each valid example into the generated dataclasses and validates it against the schema. It checks that each counter-example fails at the place its first line names, as `# Fails at: <JSON pointer>`, and that every class but the abstract predicate base has an example.[^test_data.py] There is a statement for each of the eight predicates. `tests/data/problem/valid/` holds a scan that found nothing, with an empty result list, which the validator accepts and the dataclasses read as a missing field.

`tests/test_upstream.py` checks the copy against the watch's pins, every field of each copied protocol buffer message against a slot, the header's pins, the vetted list against the predicates page, and each predicate's type URI against its page.[^test_upstream.py] `tests/test_watch.py` runs the upstream watch against stubbed GitHub answers: a newer release, a dropped or changed file, a network failure, a truncated tree, an added predicate page, a moved tag, and a token that never follows a redirect.[^test_watch.py]

`tests/test_schema_rules.py` checks that the digest set's rules name every algorithm, and that every predicate is a kind of statement predicate. It holds the eight neighbours' copies in `tests/neighbours/` to their releases' checksums, and the adapt copy apart from LOKF's names and theirs, except for the in-toto layer slsa v0.7.0 still defines and the keys `subject` and `value`, which the oscal and spdx copies share. It also checks that the copy roots only the predicate type and that every mapping uses a bound prefix.[^test_schema_rules.py]

[^data]: tests/data, valid, invalid and problem/valid
[^test_data.py]: tests/test_data.py, the valid, invalid and coverage tests
[^test_upstream.py]: tests/test_upstream.py, the copy and schema tests
[^test_watch.py]: tests/test_watch.py, the stubbed watch tests
[^test_schema_rules.py]: tests/test_schema_rules.py, the rule, neighbour and mapping tests
