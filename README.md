<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# in-toto

in-toto Attestation Framework (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/in-toto](https://lmodel.github.io/in-toto)

## What it models

The schema models the [in-toto Attestation Framework](https://github.com/in-toto/attestation) at release [v1.2.0](https://github.com/in-toto/attestation/releases/tag/v1.2.0) of March 18, 2026, the format in which a supply chain step makes a verifiable claim about the artifacts it touched. The schema holds the statement (`InTotoStatement`), the resource descriptor and digest set that name an artifact, the predicate types with the thirteen the in-toto project has vetted, and eight of the vetted predicates.

`in_toto_core` holds the statement layer and imports only the LinkML types, so that [lmodel/slsa](https://github.com/lmodel/slsa) can import it alone.

[src/in_toto_linkml/schema/attestation/](src/in_toto_linkml/schema/attestation) holds the release's specification pages and protocol buffer definitions, matched by git object hash, and `tests/test_upstream.py` holds the schema to them. A weekly workflow opens an issue when in-toto/attestation releases again, changes a copied file, or the copy drifts.

## Mappings

The framework states no mappings, so the SPDX, DCAT and EARL ones are this project's own.

* **Type URIs**: `InTotoStatement` and each predicate class name the type URI their statements carry in `exact_mappings`, and each value of `InTotoVettedPredicate` means that URI.
* **SPDX 3.0.1 and DCAT**: close mappings for annotations, download locations, media types, package URLs and build times, and related ones for digests and vulnerabilities. `tests/test_schema_rules.py` checks each term against the lmodel/spdx release.
* **EARL 1.0**: the Test Result values `PASSED` and `FAILED` mean EARL's `passed` and `failed`. `WARNED` means none, because EARL has no such outcome.
* **Names**: a class or field whose name differs from the framework's carries the framework's name as an alias, such as `_type` on `statement_type`.

## Not modelled here

* The envelope that signs a statement and the bundle that collects signed statements. Both carry a statement unchanged.
* An attestation's JSON as it is published. The schema's keys are in snake case and its open-keyed objects are lists, so a statement is written in them before it validates, as [docs/index.md](docs/index.md) says.
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

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle. Its domain schema, `.lokf/in-toto.yaml`, is the copy `just lokf-adapt` writes from `src/in_toto_linkml/schema/in_toto_linkml.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the source, never the copy. A release carries the copy as `schema-<tag>-in-toto.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

The copy roots one class on `Concept`, so a concept may name it as its `type`. In Obsidian, add it to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins:

```text
InTotoPredicateType
```

A concept writes the type URI in `predicate_type_uri`, and the vetted predicate it is in `vetted_as`. Statements, resource descriptors and predicates are records about one artifact, which a concept cites rather than holds.

`media_type` and `algorithm` carry the IRIs LOKF gives those keys, because the framework's fields mean the same. The statement's `predicate` means something else, so the copy calls it `in_toto_linkml_predicate`. The copy shares `subject` and `value` with the oscal and spdx copies, and the in-toto layer with slsa v0.7.0, which defines that layer in its own namespace, so a host imports one of the two. `tests/test_schema_rules.py` fails on any other shared name.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)), and the knowledge bundle in `.lokf/knowledge/` is under CC BY 4.0.

The in-toto Attestation Framework is the in-toto project's, under the Apache License 2.0. The schema's descriptions are this project's own words, and the specification copy keeps the project's licence beside it: see [NOTICE](NOTICE). This is not an official in-toto project, and its use implies no endorsement by the in-toto project.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
