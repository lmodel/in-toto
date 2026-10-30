# About

The schema renders the in-toto Attestation Framework at release v1.2.0, from
the specification pages and protocol buffer definitions copied to
`src/in_toto_linkml/schema/attestation/`. The descriptions are this
project's own words.

## Modules

`in_toto_core` holds the statement, the resource descriptor, the digest set
and the base of every predicate, and imports only the LinkML types.
`in_toto_predicates` imports the core and holds the predicate types and the
eight vetted predicates. The umbrella `in_toto_linkml` adds only the document
root. lmodel/slsa imports the core alone and models SLSA's own predicates on
the same base.

## Names

The classes carry the `InToto` prefix and live under `in_toto_linkml:`
(`https://w3id.org/lmodel/in-toto/`). The core keeps the class and slot names
lmodel/slsa gave the layer, which follow the attestation's JSON in snake case:
`statement_type` for `_type`, `resource_uri` for `uri` and `dir_hash` for
`dirHash`, for example.

Three names differ from the JSON so that the adapt copy can sit beside LOKF's
schema. The statement's predicate is `statement_predicate`, because LOKF's
`predicate` is a relation's type. `media_type` carries DCAT's `mediaType` and
`algorithm` SPDX 2's `algorithm`, the IRIs LOKF gives the same keys, because
the framework's fields mean the same.

The predicates' fields carry a prefix of their predicate's, such as
`scai_attribute` and `svr_verifier`, or a noun of their own, such as
`test_run_url` and `scan_results`. So no key is shared with LOKF or with
another neighbour's copy, and two predicates never give one key two meanings.

## Left out

- The envelope that signs a statement and the bundle that collects signed
  statements.
- SLSA Provenance and the SLSA Verification Summary, which lmodel/slsa
  models, and the bodies of the CycloneDX, SPDX 2 and SPDX 3 predicates. The
  schema names their type URIs in `InTotoVettedPredicate`.
- The older predicate versions, VULNS v0.1, and the policy field a verifier
  may add to a Simple Verification Result.
- JSON objects whose keys the framework leaves to the producer, such as a
  link's byproducts, are lists of `InTotoObjectEntry`, a key with its values,
  as slsa's annotations are. A list of such objects, such as a runtime trace's
  processes, holds each object as its JSON text.
