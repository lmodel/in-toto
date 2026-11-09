---
type: Dataset
id: https://w3id.org/lmodel/in-toto/knowledge/datasets/generated-artefacts
genre: reference
title: Generated artefacts
description: "What the LinkML generators, `lokf adapt`, `gen-rdf` and `gen-merged-schema` write from the schema: `project/` (JSON Schema, OWL, SHACL, ShEx, JSON-LD, GraphQL, protobuf, SQL, TypeScript, Excel, Java, RDF Turtle and the merged schema), the Python dataclasses and Pydantic models in `src/in_toto_linkml/datamodel/`, `docs/schema/` and `docs/elements/`, and `.lokf/schema/in-toto.yaml`. None is edited by hand."
resource: project
isPartOf:
  - https://w3id.org/lmodel/in-toto/knowledge/datasets/in-toto-linkml-schema
sources:
  - id: justfile
    resource: justfile
    title: the gen-project, gen-doc and test recipes
  - id: generators.yaml
    resource: .linkml/generators.yaml
    title: the generators' settings
  - id: project
    resource: project
    title: the generated folders
  - resource: src/in_toto_linkml/datamodel
    title: the Python models
  - resource: docs/schema
    title: the YAML gen-doc writes
  - id: pre-commit-config.yaml
    resource: .pre-commit-config.yaml
    title: the exclude pattern
  - id: project.justfile
    resource: project.justfile
    title: the gen-rdf and gen-merged-schema recipes
generated:
  by: process:ktl-librarian
  at: "2026-11-09T13:45:23Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T21:20:44Z"
---

# Generated artefacts

Every file here is generated from the schema's modules under `src/in_toto_linkml/schema/`, so a change starts in the schema and the recipes rewrite the rest.

`just gen-project` runs `gen-project` with `.linkml/generators.yaml` into `project/`, moves the Python dataclasses into `src/in_toto_linkml/datamodel/`, and writes the Pydantic models beside them. It then runs `gen-java`, `gen-typescript` and `gen-owl` separately, because some generators ignore the configuration or cannot create their folders, as its comment says.[^justfile] `.linkml/generators.yaml` leaves out the Markdown generator and merges imports for the others.[^generators.yaml] `project/` holds a folder each for Excel, GraphQL, Java, JSON-LD, JSON Schema, the merged schema, OWL, the prefix map, protobuf, RDF Turtle, SHACL, ShEx, SQL and TypeScript.[^project] The Java folder holds one class per schema class, 32 in all.

`project.justfile` also runs `gen-rdf` and `gen-merged-schema`, two recipes `gen-project` does not, which write `project/rdf/in_toto_linkml.ttl` and `project/linkml/in_toto_linkml.merged.linkml.yaml`: the schema as RDF Turtle, and one LinkML file with every import merged.[^project.justfile]

`just gen-doc` writes `docs/schema/in_toto_linkml.yaml` and the element pages under `docs/elements/`, which git ignores and the website builds. `just lokf-adapt` writes `.lokf/schema/in-toto.yaml`.

The pre-commit hooks leave alone these folders, the specification copy, the neighbours' copies and the sidecar's scripts, because no hook may rewrite a file the repository does not write by hand.[^pre-commit-config.yaml]

[^justfile]: justfile, the gen-project and gen-doc recipes
[^generators.yaml]: .linkml/generators.yaml, excludes and generator_args
[^project]: project, its folders
[^project.justfile]: project.justfile, the gen-rdf and gen-merged-schema recipes
[^pre-commit-config.yaml]: .pre-commit-config.yaml, the exclude pattern and its comment
