---
type: Policy
id: https://w3id.org/lmodel/in-toto/knowledge/policies/license-and-attribution
genre: reference
title: License and attribution
description: "The repository's licences: Apache 2.0 for the schema and the code, the in-toto project's Apache 2.0 for the specification copy, MIT for the copier template's scaffolding, and Apache 2.0 for the KTL sidecar and website templates."
resource: NOTICE
sources:
  - id: notice
    resource: NOTICE
    title: every section
  - id: license
    resource: LICENSE
    title: the Apache License 2.0
  - id: attestation-license
    resource: src/in_toto_linkml/schema/attestation/LICENSE
    title: the in-toto project's licence notice
  - id: readme.md
    resource: README.md
    title: the License section
  - resource: website/NOTICE
    title: the part adapted from the LOKF toolkit's site
generated:
  by: process:ktl-librarian
  at: "2026-10-30T16:14:35Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T21:20:44Z"
---

# License and attribution

The schema and the code are under the Apache License, Version 2.0.[^license] NOTICE lists the third-party work the repository carries.[^notice]

- The schema, the generated models and `project/` render the in-toto Attestation Framework in the project's own words, with the framework's specification as the source of the definitions. NOTICE says that they are not the in-toto project's, and that their use implies no endorsement by it.
- The specification pages and protocol buffer definitions in `src/in_toto_linkml/schema/attestation/` are the in-toto project's, copied from release v1.2.0 with the project's `LICENSE` beside them. That file holds the Apache License 2.0 notice of the in-toto Developers, from 2021.[^attestation-license] NOTICE adds that GitHub's licence detection does not recognise the file, which was read on 2026-10-30.
- The justfile, configuration and documentation scaffolding derive from linkml-project-copier, under the MIT License, whose text NOTICE carries.
- The sidecar's scripts and workflows are copies of the ktl-sidecar templates, and the site under `website/` derives from the ktl-website templates, all under the Apache License 2.0. `website/NOTICE` lists the part adapted from the LOKF toolkit's site.

The README says that the knowledge bundle in `.lokf/knowledge/` is under the Creative Commons Attribution 4.0 International licence (CC BY 4.0), as its `index.md` declares. It adds that this is not an official in-toto project.[^readme.md]

[^license]: LICENSE, the Apache License 2.0
[^notice]: NOTICE, every section
[^attestation-license]: src/in_toto_linkml/schema/attestation/LICENSE, the notice
[^readme.md]: README.md, the License section
