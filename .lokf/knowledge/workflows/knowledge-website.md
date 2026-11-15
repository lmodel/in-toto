---
type: Service
id: https://w3id.org/lmodel/in-toto/knowledge/workflows/knowledge-website
genre: reference
title: Knowledge website (knowledge-website.yaml)
description: "The Knowledge website workflow, `.github/workflows/knowledge-website.yaml`: on pushes and pull requests that touch the site's sources, every Monday at 05:23 UTC and by hand, its build job builds `website/` and checks its links read-only, and its deploy job publishes the default branch's build to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is true."
resource: .github/workflows/knowledge-website.yaml
sources:
  - id: knowledge-website.yaml
    resource: .github/workflows/knowledge-website.yaml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-11-15T03:05:06Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T21:20:44Z"
---

# Knowledge website (knowledge-website.yaml)

`.github/workflows/knowledge-website.yaml` is the workflow named "Knowledge website", a copy of the ktl-website template. It runs every Monday at 05:23 UTC and by hand. It also runs on a push or a pull request that touches `website/`, `ktl-website/`, `.lokf/`, `knowledge_bundle/`, the README, `docs/`, `.assets/`, the changelog, `.linkml/`, a schema under `src/*/schema/`, this workflow or the knowledge federation workflow.[^knowledge-website.yaml] Its `build` job runs under a read-only token, and a push builds on the default branch only. It:

- checks the repository out with its full history;
- sets up uv;
- links the `just` the sidecar's lock pins, when the site builds its data with it;
- runs `website/scripts/build.sh`, which runs `lokf export` and `gen-doc`, builds the site with Hugo and Pagefind, cleans its raw HTML and checks its links;
- uploads `website/dist` as the Pages artifact.

Its `deploy` job holds `pages: write` and `id-token: write` in the `github-pages` Environment, and runs only for the default branch once the repository variable `KNOWLEDGE_WEBSITE_ENABLED` is `true`. [Documentation site](../services/documentation-site.md) describes what it publishes.

[^knowledge-website.yaml]: .github/workflows/knowledge-website.yaml, the header comment, the on key and the jobs
