---
title: "Zotero Workflow"
type: workflow
status: active
tags:
  - zotero
  - literature
  - embodied-ai
---

# Zotero Workflow

Zotero is the literature asset database. Obsidian is the research understanding graph.

First-time walkthrough:

- [[00_MOC/Zotero First Paper Setup]]

## What Goes in Zotero

- Formal papers, surveys, books, theses, arXiv papers, proceedings papers.
- PDF attachments, metadata, citation keys, DOI/arXiv IDs, and bibliographic notes.
- Datasets, benchmarks, and simulators when they have a formal paper.
- Original PDF highlights and annotation evidence.

## What Stays in Obsidian

- Concept maps, learning routes, research questions, and personal synthesis.
- Core paper notes after reading.
- Non-paper resources: codebases, products, labs, sensors, courses, demos, project pages.
- The source repository registry and update history.

## Collection Design

```text
Embodied AI
  00 Surveys
  01 Foundations
  02 Platforms Simulators Datasets
  03 Perception Grounding Mapping
  04 Navigation Embodied Vision
  05 Interaction Manipulation Tactile
  06 Agents Planning
  07 VLA Robot Foundation Models
  08 World Models Sim2Real Evaluation
```

## Tag Design

- Source tags: `source:hcplab`, `source:zchoi`, `source:milkclouds`, `source:changanvr`, `source:awesome-touch`
- Topic tags: `topic:vla`, `topic:vln`, `topic:tactile`, `topic:sim2real`, `topic:world-model`
- Status tags: `status:to-read`, `status:reading`, `status:read`, `priority:core`

## Obsidian Link Rule

Every refined paper note should include:

```yaml
zotero_key: ""
paper_url: ""
source_repos: []
```

Use Zotero for "what the paper is" and Obsidian for "what the paper means in the research graph."
