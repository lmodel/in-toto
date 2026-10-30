<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# in-toto

in-toto Attestation Framework (LinkML)

> **Two ways in.** This README is one; the other is a docent, a museum's name
> for a guide. Install
> [`ktl-docent`](https://github.com/noelmcloughlin/knowledge-trust-ladder) into
> whatever agent you already use, by a route from
> [the install page](https://w3id.org/ktl/docs/install/), and ask it anything
> about this project. It answers from `.lokf/knowledge/`,
> the checked part of what the project knows, and says how far each answer has
> been trusted (still a draft, checked by automation only, or confirmed by a
> named person). It opens the source for exact values, and records what it
> could not answer so the gap gets filled. The same docent serves a person at a
> prompt, an agent reading this file, or a chatbot that can load a skill.
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt`
> says how to weigh it.

## Documentation Website

[https://lmodel.github.io/in-toto](https://lmodel.github.io/in-toto)

## What it models

The [in-toto Attestation Framework](https://github.com/in-toto/attestation) at release [v1.2.0](https://github.com/in-toto/attestation/releases/tag/v1.2.0) of March 18, 2026, the format in which a supply chain step makes a verifiable claim about the artifacts it touched:

* **The statement** (`InTotoStatement`): the middle layer of an attestation, which binds it to its subjects, each a resource descriptor with a digest (`InTotoStatementSubject`), and names the type of its predicate.
* **The resource descriptor** (`InTotoResourceDescriptor`) and **the digest set** (`InTotoDigestSet`, with `InTotoAdditionalDigest` and `InTotoAnnotation`): how an attestation names an artifact, by URI, digest or content.
* **Predicate types** (`InTotoPredicateType`): a type of predicate, named by the URI a statement's `predicate_type` holds, and the thirteen the in-toto project has vetted (`InTotoVettedPredicate`).
* **Eight vetted predicates**: Test Result (`InTotoTestResult`), Simple Verification Result (`InTotoSimpleVerificationResult`), SCAI Attribute Report (`InTotoScaiAttributeReport`), Link (`InTotoLink`), Reference (`InTotoReference`), Release (`InTotoRelease`), Runtime Trace (`InTotoRuntimeTrace`) and VULNS (`InTotoVulns`), each with the classes it holds.

`in_toto_core` holds the statement layer and imports only the LinkML types, so that [lmodel/slsa](https://github.com/lmodel/slsa), which models SLSA Provenance and the SLSA Verification Summary, can import it alone. The class and slot names are the ones slsa gave them.

The schema header's `version` is the framework's release, 1.2.0, and its `source` is the release's tree. [src/in_toto_linkml/schema/attestation/](src/in_toto_linkml/schema/attestation) holds the release's specification pages and protocol buffer definitions, matched to it by git object hash. `tests/test_upstream.py` holds every field of each copied definition to a slot, the list of vetted predicates to the predicates page, each vetted type URI to the page that gives it, and the pages' complete examples to the schema. A weekly workflow opens an issue when in-toto/attestation releases again, changes a copied file, or the copy drifts.

v1.2.0 is the latest release. Release tags number the schema's versions.

## Influences

None beyond the in-toto specification: the schema renders one framework, and its layout, its release asset and its governance files follow lmodel/slsa.

## Mappings

The schema crosses to the framework's own identifiers and borrows from no other vocabulary.

* **Predicate types**: each predicate class names the type URI its statements carry in `exact_mappings`, and each value of `InTotoVettedPredicate` means that URI, under the `in_toto:` prefix for the in-toto project's own predicates.
* **LOKF**: `media_type` carries DCAT's `mediaType` and `algorithm` SPDX 2's `algorithm`, the IRIs LOKF gives the two keys, because the framework's fields mean the same.

## Not modelled here

* The envelope that signs a statement and the bundle that collects signed statements. Both carry a statement unchanged.
* SLSA Provenance and the SLSA Verification Summary, which lmodel/slsa models.
* The bodies of the CycloneDX, SPDX 2 and SPDX 3 predicates, each a whole bill of materials in another specification's format. The schema names their type URIs only; lmodel/spdx models SPDX 3.
* The older predicate versions and the superseded VULNS v0.1 page, and the policy field a verifier may add to a Simple Verification Result.
* The rules no pattern can check, which [docs/index.md](docs/index.md) lists.

## Repository Structure

* [docs/](docs/): the website's pages, with the generated schema pages in [elements/](docs/elements/)
* [examples/](examples/): usage examples
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the upstream watch
* [src/in_toto_linkml/schema/](src/in_toto_linkml/schema): the LinkML schema, `in_toto_core.yaml`, `in_toto_predicates.yaml` and the umbrella `in_toto_linkml.yaml` (edit these), and the specification copy
* [src/in_toto_linkml/datamodel/](src/in_toto_linkml/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data in [data/](tests/data) and the neighbours' adapt copies in [neighbours/](tests/neighbours)
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle, in the Linked Open Knowledge Format (LOKF). Its domain schema is `.lokf/in-toto.yaml`, which `lokf adapt` writes from `src/in_toto_linkml/schema/in_toto_linkml.yaml`. Edit the source, never the copy. A release carries the copy as `schema-<tag>-in-toto.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

`just lokf-adapt` rewrites the copy, and `just lokf-adapt-check` says when it is stale. `project.justfile` names the class the copy roots on `Concept`, and a concept may name it as its `type`. In Obsidian, add it to the KTL Registrar and KTL Curator plugins' *Known LOKF types* setting:

```text
InTotoPredicateType
```

A concept writes the type URI in `predicate_type_uri`, and the vetted predicate it is in `vetted_as`. A name and a description are the concept's own `title` and `description`. Statements, resource descriptors and predicates are records about one artifact, which a concept cites rather than holds.

A host imports the copy beside LOKF's schema, `lokf.yaml`, and beside other adapt copies. LinkML merges them into one namespace, where the last definition of a name wins silently. So no class, enum or type shares a name with LOKF's. A slot shares a name with LOKF's only where it carries LOKF's meaning and Internationalized Resource Identifier (IRI), as `media_type` and `algorithm` do. The statement's `predicate` means something else, so the copy calls it `in_toto_linkml_predicate`. With the released neighbours, the copy shares `subject` and `value` with the oscal and spdx copies, keys slsa v0.7.0 shares with them too. It shares the in-toto layer with slsa v0.7.0 itself, which defines that layer in its own namespace until its next release imports it from here, so a host takes one of the two. `tests/test_schema_rules.py` fails on any other shared name.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)).

The knowledge bundle in `.lokf/knowledge/` is under the Creative Commons Attribution 4.0 International licence (CC BY 4.0), as its `index.md` declares.

The in-toto Attestation Framework is the in-toto project's, under the Apache License 2.0. The schema's descriptions are this project's own words. The specification copy in [src/in_toto_linkml/schema/attestation/](src/in_toto_linkml/schema/attestation) keeps the project's licence beside it: see [NOTICE](NOTICE).

This is not an official in-toto project, and its use implies no endorsement by the in-toto project.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
