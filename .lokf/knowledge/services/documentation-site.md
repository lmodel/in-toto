---
type: Service
id: https://w3id.org/lmodel/in-toto/knowledge/services/documentation-site
genre: reference
title: Documentation site
description: "The Hugo site in `website/`, for <https://lmodel.github.io/in-toto>: the README as its home page, the pages of `docs/`, the schema's element pages, a page per concept of this bundle with its trust label, and the bundle's exports, built and published by Knowledge website."
resource: website
endpoint: https://lmodel.github.io/in-toto
documentation: website/README.md
sources:
  - id: site.toml
    resource: website/site.toml
    title: the site's address, title and redirects
  - id: website-readme.md
    resource: website/README.md
    title: what each page is built from
generated:
  by: process:ktl-librarian
  at: "2026-11-15T03:05:06Z"
status: draft
---

# Documentation site

`website/` holds a Hugo site. `website/site.toml` names the repository `lmodel/in-toto`, the site `https://lmodel.github.io` with the base path `/in-toto`, and the title `in-toto`. It sends `/about` to `docs/about.md`. The other options take the site's defaults, such as the Knowledge Trust Ladder logo.[^site.toml]

The site shows the README as its home page, the pages of `docs/`, a page per release of the changelog, a page per concept of the bundle with its trust label, and a page per class, slot, enumeration and type of the schema, written by LinkML's `gen-doc`. Each page of the schema is also at `elements/<Name>/`, where the schema's w3id rules point.[^website-readme.md]

`scripts/build.sh`, run in `website/`, writes the site to `dist/` with its search index and then checks every link between its pages. Hugo and Pagefind come from PyPI through uv, so the build needs bash, git and uv. `scripts/build.sh serve` serves the site at `http://localhost:1313/in-toto/` and rebuilds it as you edit.[^website-readme.md] [Knowledge website](../workflows/knowledge-website.md) builds the site on each change to its sources and publishes it once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.

[^site.toml]: website/site.toml, the site's address, title and redirects
[^website-readme.md]: website/README.md, the build and its sources
