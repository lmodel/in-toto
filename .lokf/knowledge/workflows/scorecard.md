---
type: Service
id: https://w3id.org/lmodel/in-toto/knowledge/workflows/scorecard
genre: reference
title: Scorecard (scorecard.yml)
description: "The Scorecard workflow, `.github/workflows/scorecard.yml`: on a push to main, every Tuesday at 05:17 UTC and by hand on the default branch only, its one job runs the OpenSSF Scorecard, publishes the result the README's badge shows, and uploads the same findings to code scanning."
resource: .github/workflows/scorecard.yml
sources:
  - id: scorecard.yml
    resource: .github/workflows/scorecard.yml
    title: the header comment, the on key and the jobs
generated:
  by: process:ktl-librarian
  at: "2026-11-23T15:41:41Z"
  revision: "574c8bf47b6c820855dee5d9c57339a8c82184cf"
status: draft
---

# Scorecard (scorecard.yml)

`.github/workflows/scorecard.yml` is the workflow named "Scorecard". It runs on a push to `main`, every Tuesday at 05:17 UTC and by hand, and a manual run refuses any branch but the default one, since the OpenSSF API accepts a published result only from it.[^scorecard.yml] Its one job, `analysis`, holds `security-events: write` and `id-token: write`. It runs the Scorecard action, which publishes the result the README's badge shows, then uploads the same findings to code scanning.

[^scorecard.yml]: .github/workflows/scorecard.yml, the header comment, the on key and the jobs
