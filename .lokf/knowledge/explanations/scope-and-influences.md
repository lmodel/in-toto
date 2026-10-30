---
type: Explanation
id: https://w3id.org/lmodel/in-toto/knowledge/explanations/scope-and-influences
genre: explanation
title: Scope, influences and mappings
description: "What the schema renders and what it leaves out: the statement layer and eight vetted predicates of the in-toto Attestation Framework at v1.2.0, with lmodel/slsa as its one influence on layout and names. It maps each predicate to its type URI, and models neither the envelope, the bundle, SLSA's two predicates nor the bill-of-materials predicates' bodies."
resource: README.md
about:
  - https://w3id.org/lmodel/in-toto/knowledge/datasets/in-toto-linkml-schema
sources:
  - id: readme.md
    resource: README.md
    title: What it models, Influences, Mappings and Not modelled here
  - id: about.md
    resource: docs/about.md
    title: Modules and Left out
generated:
  by: process:ktl-librarian
  at: "2026-10-30T16:14:35Z"
status: draft
---

# Scope, influences and mappings

The README says that the schema renders the in-toto Attestation Framework at release v1.2.0: the statement, the resource descriptor and the digest set, the predicate types, and eight vetted predicates.[^readme.md] Its one influence is lmodel/slsa, whose module layout, release asset and governance files it follows, and whose names for the statement layer it keeps, so that slsa can import the core module alone.[^about.md]

It maps each predicate to the type URI its statements carry, in `exact_mappings`, and gives `media_type` and `algorithm` the IRIs LOKF gives the same keys. It borrows from no other vocabulary.

It leaves out the envelope that signs a statement and the bundle that collects them, SLSA Provenance and the SLSA Verification Summary, which slsa models, and the bodies of the CycloneDX, SPDX 2 and SPDX 3 predicates, which it names by type URI only. It also leaves out the older predicate versions, VULNS v0.1, and the policy field a verifier may add to a Simple Verification Result.

[^readme.md]: README.md, What it models, Influences, Mappings and Not modelled here
[^about.md]: docs/about.md, Modules and Left out
