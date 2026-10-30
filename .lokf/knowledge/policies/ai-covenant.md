---
type: Policy
id: https://w3id.org/lmodel/in-toto/knowledge/policies/ai-covenant
genre: reference
title: AI covenant
description: "The repository's rules for work done with artificial intelligence (AI): you own what you submit, an element under the schema renders the in-toto specification in the project's own words and cites its page, the specification copy is never edited, and the scheduled librarian proposes changes only through reviewed pull requests."
resource: AI_COVENANT.md
sources:
  - id: ai_covenant.md
    resource: AI_COVENANT.md
    title: the project note and the section on agent automation
generated:
  by: process:ktl-librarian
  at: "2026-10-30T16:14:35Z"
status: draft
---

# AI covenant

`AI_COVENANT.md` says that everything a contributor submits is theirs, whatever tools helped make it, and that they must understand, verify and defend it.[^ai_covenant.md] Its note for this project says that the repository models someone else's framework, the in-toto Attestation Framework. So the failure mode to guard against is a field, rule or predicate that an AI model produced and presented as what the framework says. Three rules follow:

- an element under `src/in_toto_linkml/schema/` says what the specification says, in the project's own words, with the specification page cited in the pull request;
- the specification copy under `src/in_toto_linkml/schema/attestation/` is upstream text, never edited, only replaced from one release;
- everything the schema defines lives under `in_toto_linkml:`, with the framework's own identifiers, such as its type URIs, appearing only as values.

The covenant forbids posting AI output as an independent voice in issues or discussions. It sets four rules for the scheduled librarian:

- a bot identity or the maintainer's, never both;
- every change as a pull request a person approves;
- a read-only job that hands a patch to a separate job that runs no agent;
- a recorded verdict only where a person said it.

AI co-authorship trailers in commits are discouraged.

[^ai_covenant.md]: AI_COVENANT.md, A note specific to this project and Repository-Owned Agent Automation
