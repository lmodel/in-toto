---
type: Service
id: https://w3id.org/lmodel/in-toto/knowledge/workflows/codeql
genre: reference
title: CodeQL (codeql.yml)
description: "The CodeQL workflow, `.github/workflows/codeql.yml`: on a push to main, every pull request, every Wednesday at 03:41 UTC and by hand, its one job scans the Python, the JavaScript/TypeScript and the GitHub Actions workflows with CodeQL in build-mode none, across a three-language matrix, and uploads each finding to code scanning."
resource: .github/workflows/codeql.yml
sources:
  - id: codeql.yml
    resource: .github/workflows/codeql.yml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-11-23T15:41:41Z"
  revision: "574c8bf47b6c820855dee5d9c57339a8c82184cf"
status: draft
---

# CodeQL (codeql.yml)

`.github/workflows/codeql.yml` is the workflow named "CodeQL". It runs on a push to `main`, on every pull request, every Wednesday at 03:41 UTC and by hand.[^codeql.yml] Its one job, `analyze`, holds `contents: read` and `security-events: write`, and runs across a matrix of three languages: `actions`, `javascript-typescript` and `python`. Each is scanned with `build-mode: none`, so CodeQL reads the source without building or running it, and a finding becomes a code scanning alert.

[^codeql.yml]: .github/workflows/codeql.yml, the header comment, the on key and the jobs
