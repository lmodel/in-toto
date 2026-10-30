---
type: Dataset
id: https://w3id.org/lmodel/in-toto/knowledge/datasets/in-toto-linkml-schema
genre: reference
title: in-toto LinkML schema
description: "The LinkML schema of the in-toto Attestation Framework, `src/in_toto_linkml/schema/in_toto_linkml.yaml` (schema id `https://w3id.org/lmodel/in-toto`, version 1.2.0) with its modules `in_toto_core` and `in_toto_predicates`: 32 classes, two enums and three types. Its `lokf adapt` copy `.lokf/in-toto.yaml`, rooted on the predicate type, is the bundle's domain schema."
resource: src/in_toto_linkml/schema/in_toto_linkml.yaml
version: 1.2.0
license: https://spdx.org/licenses/Apache-2.0
derivedFrom:
  - https://w3id.org/lmodel/in-toto/knowledge/datasets/attestation-copy
sources:
  - id: in_toto_linkml.yaml
    resource: src/in_toto_linkml/schema/in_toto_linkml.yaml
    title: the header and the document root
  - id: in_toto_core.yaml
    resource: src/in_toto_linkml/schema/in_toto_core.yaml
    title: the header, the three types, the three slots and the seven classes
  - id: in_toto_predicates.yaml
    resource: src/in_toto_linkml/schema/in_toto_predicates.yaml
    title: the header, the classes and the two enums
  - id: project.justfile
    resource: project.justfile
    title: the lokf-adapt recipes and their roots
  - id: in-toto.yaml
    resource: .lokf/in-toto.yaml
    title: the adapt copy's header, prefixes, imports and notes
  - id: lokf-justfile
    resource: .lokf/justfile
    title: the schema := line
generated:
  by: process:ktl-librarian
  at: "2026-10-30T21:22:17Z"
status: draft
---

# in-toto LinkML schema

`src/in_toto_linkml/schema/in_toto_linkml.yaml` is the umbrella schema `in_toto_linkml`, id `https://w3id.org/lmodel/in-toto`, version 1.2.0, under the Apache License 2.0. Its `version` is the in-toto/attestation release it renders, and its `source` is that release's tree. Its annotations pin the tag `v1.2.0` and the commit `df02077bf972`, which the upstream watch reads too. It imports the LinkML types and the two modules, and adds only the document root, `InTotoDocument`, which holds statements and predicate types.[^in_toto_linkml.yaml]

`in_toto_core` imports only the LinkML types. It defines the framework's field types: `in_toto_resource_uri` and `in_toto_type_uri`, each a URI whose scheme and authority are lowercase, and `in_toto_timestamp`, a UTC time in RFC 3339 form. It defines the slots `resource_uri`, `digest` and `predicate`, the statement's predicate, and seven classes: `InTotoDigestSet` with its 24 named algorithms and `additional_digests`, `InTotoAdditionalDigest`, `InTotoAnnotation`, `InTotoResourceDescriptor`, `InTotoStatementSubject`, `InTotoStatement` and the abstract `InTotoPredicate`, whose `predicate_kind` names a predicate's class. A resource descriptor needs a URI, a digest or content, and a statement's subjects each need a digest. `media_type` carries `dcat:mediaType` and `algorithm` `spdx:algorithm`, the IRIs LOKF gives the same keys.[^in_toto_core.yaml]

`in_toto_predicates` imports the core. It defines the class `InTotoPredicateType` for a predicate type named by its URI, `InTotoObjectEntry` for a key of an object the framework leaves open, and the eight vetted predicates with the 15 classes they hold. Each predicate names the type URI its statements carry in `exact_mappings`, under the `in_toto:` prefix. Its two enums are `InTotoTestResultValue`, `PASSED`, `WARNED` or `FAILED`, and `InTotoVettedPredicate`, the thirteen vetted types.[^in_toto_predicates.yaml]

## Domain schema

`project.justfile` runs `lokf adapt` with one root, `InTotoPredicateType`, and writes `.lokf/in-toto.yaml`. `just lokf-adapt-check` fails when the copy is stale.[^project.justfile] The copy, `https://w3id.org/lmodel/in-toto-lokf`, folds the two modules into one file, keeps their prefixes, imports `linkml:types` and `lokf`, and re-roots the predicate type on `Concept`. It renames the statement's `predicate` to `in_toto_linkml_predicate`, apart from LOKF's.[^in-toto.yaml] The sidecar's justfile names it on its `schema :=` line, so `just lokf-validate` and `just lokf-check-refs` read it.[^lokf-justfile]

[^in_toto_linkml.yaml]: src/in_toto_linkml/schema/in_toto_linkml.yaml, the header and InTotoDocument
[^in_toto_core.yaml]: src/in_toto_linkml/schema/in_toto_core.yaml, the types, the slots and the classes
[^in_toto_predicates.yaml]: src/in_toto_linkml/schema/in_toto_predicates.yaml, the classes and the enums
[^project.justfile]: project.justfile, lokf_adapt_roots, lokf-adapt and lokf-adapt-check
[^in-toto.yaml]: .lokf/in-toto.yaml, the header comment, prefixes, imports and notes
[^lokf-justfile]: .lokf/justfile, the schema := line
