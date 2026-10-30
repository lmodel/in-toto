---
type: Playbook
id: https://w3id.org/lmodel/in-toto/knowledge/playbooks/regenerate-and-test
genre: how-to
title: Regenerate and test after a schema change
description: "How to change the schema and check it: `uv sync --group dev`, edit the modules under `src/in_toto_linkml/schema/`, then `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and the pre-commit hooks before a pull request."
resource: CONTRIBUTING.md
about:
  - https://w3id.org/lmodel/in-toto/knowledge/datasets/in-toto-linkml-schema
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: the Development setup and Before opening a pull request sections
  - id: justfile
    resource: justfile
    title: the lint, gen-project, gen-doc and test recipes
  - id: project.justfile
    resource: project.justfile
    title: the lokf-adapt recipes
generated:
  by: process:ktl-librarian
  at: "2026-10-30T16:14:35Z"
status: draft
---

# Regenerate and test after a schema change

1. Install the toolchain once: Python 3.10 or later, `uv` and `just`, then `uv sync --group dev` in the clone.[^contributing.md]
2. Edit the modules under `src/in_toto_linkml/schema/`: `in_toto_core.yaml`, `in_toto_predicates.yaml` and the umbrella `in_toto_linkml.yaml`. They are the files to write by hand. `project/`, `src/in_toto_linkml/datamodel/`, `docs/schema/` and `.lokf/in-toto.yaml` are generated from them. Say in the pull request which page of the specification a new or changed element renders.
3. Run `just lint`, which runs `linkml-lint --ignore-warnings` under `.linkmllint.yaml`.[^justfile]
4. Run `just gen-project` and `just gen-doc`, then `just lokf-adapt`, which rewrites the adapt copy rooted on the predicate type.[^project.justfile] Commit the output.
5. Add an example under `tests/data/valid/` for a new class and a counter-example under `tests/data/invalid/` for a new constraint, named `ClassName-suffix.yaml`, then run `just test`.
6. Run the pre-commit hooks on what you staged (`uvx pre-commit run`), and write a changelog entry under `## [Unreleased]` when the change alters behaviour.

CI runs the same: `main.yaml` runs `just lint`, `just test` and `just lokf-adapt-check`, and fails when the adapt copy is stale.

[^contributing.md]: CONTRIBUTING.md, Development setup and Before opening a pull request
[^justfile]: justfile, the lint recipe
[^project.justfile]: project.justfile, lokf-adapt and lokf-adapt-check
