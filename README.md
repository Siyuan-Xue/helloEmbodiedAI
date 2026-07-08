# helloEmbodiedAI

An Obsidian research vault for studying Embodied AI. The vault is organized as a lightweight knowledge graph: papers, concepts, source repositories, datasets, simulators, benchmarks, and research areas are linked through stable metadata and wiki links.

## Purpose

This repository helps answer three recurring research questions:

- Where does a paper or resource fit in the Embodied AI landscape?
- Which concepts, areas, repositories, and follow-up readings does it connect to?
- What did I understand from reading it, beyond raw PDF highlights or bibliographic metadata?

PDFs and original paper annotations should live outside this vault. This repo stores curated notes, graph placement, research synthesis, templates, and lightweight source registries.

## Vault Architecture

```text
helloEmbodiedAI/
├── 00_MOC/                 # Maps of content, workflows, schema, and roadmap
├── 10_Areas/               # Research area pages
├── 20_Concepts/            # Reusable concept notes
├── 30_Literature_Notes/    # Refined paper notes and modular paper folders
├── 40_Resources/           # Resource hubs: datasets, simulators, benchmarks, code, hardware
├── 90_Sources/             # Source repository registry and generated snapshots
├── 99_Templates/           # Obsidian note templates
├── scripts/                # Utility scripts for source updates
└── .codex/skills/          # Project-level Codex skills for this vault
```

Key entry points:

- `00_MOC/Embodied AI Atlas.md`: top-level map of the vault.
- `00_MOC/Research Roadmap.md`: staged learning path.
- `00_MOC/Knowledge Graph Schema.md`: controlled fields for graph nodes.
- `90_Sources/Resource Registry.md`: curated registry for papers and resources.
- `99_Templates/Paper Note.md`: baseline metadata and section template for paper notes.

## Research Areas

The current graph is organized by research objects and capabilities rather than by source repository:

- Foundations
- Platforms, Robots, Simulators, Datasets
- Perception and Grounding
- Navigation and Embodied Vision
- Interaction, Manipulation, Tactile
- Agents, Planning, Memory
- VLA / Robot Foundation Models
- World Models, Sim-to-Real, Evaluation

New resources should usually fit by combining `area`, `task`, `method`, `modality`, and `embodiment` fields rather than by creating a new top-level area.

## Paper Note Workflow

Refined paper notes live in `30_Literature_Notes/`.

For a short paper note, keep one polished Markdown file. For a long or survey-style note, use:

```text
30_Literature_Notes/
├── Paper Title.md
└── Paper Title - Short Suffix/
    ├── 00 Module.md
    ├── 01 Module.md
    └── Vocabulary.md
```

Each refined paper note should:

- Use `99_Templates/Paper Note.md` as the metadata baseline.
- Set `type: paper-note`.
- Use `source_type: paper` or `source_type: survey`.
- Fill known fields such as `authors`, `year`, `arxiv_id`, `areas`, `tasks`, `methods`, `modalities`, `embodiments`, `source_repos`, and URLs.
- Leave Zotero-related fields blank unless exact values are available.
- Include `Graph Links` to relevant MOC pages, area pages, and existing concept notes.
- Add or update a row in `90_Sources/Resource Registry.md` when enough metadata exists.

The project-level Codex skill `.codex/skills/organize-paper-notes` captures the full workflow for turning rough reading notes into polished, registered Obsidian notes.

## Source Updates

External source lists are tracked through `90_Sources/`.

To refresh generated source registries:

```bash
python3 scripts/update_sources.py
```

The script is intentionally conservative:

- It writes generated output to `90_Sources/Resource Registry.generated.md`.
- It writes update logs to `90_Sources/Repository Update Log.generated.md`.
- It does not edit curated notes or area maps.

Review generated output before promoting anything into `90_Sources/Resource Registry.md`, area pages, concept pages, or long-form notes.

## Using With Obsidian

1. Clone this repository.
2. Open the folder as an Obsidian vault.
3. Start from `00_MOC/Embodied AI Atlas.md`.
4. Use `00_MOC/Research Roadmap.md` for a staged learning path.
5. Use `99_Templates/` when creating new paper, concept, or resource notes.

The `.gitignore` keeps local UI state and bulky research artifacts out of git, including `.obsidian/workspace*.json`, `.DS_Store`, PDFs, archives, caches, and temporary files.

## Project-Level Codex Skill

This vault includes a reusable Codex skill:

```text
.codex/skills/organize-paper-notes
```

Use it when you want Codex to:

- Clean rough single-file paper notes.
- Preserve only user-recorded learning content.
- Read the same-directory same-name PDF as required source material.
- Normalize Markdown, YAML metadata, formulas, vocabulary, and graph links.
- Register the note in the current vault architecture.
- Ask whether to delete the source PDF after organization.

Run its validator on a paper note set with:

```bash
python3 .codex/skills/organize-paper-notes/scripts/validate_note_set.py 30_Literature_Notes/<note-or-folder>
```

## Git Hygiene

Tracked content is intended to be lightweight and text-first. Do not commit paper PDFs, local workspace state, large archives, cache directories, or generated runtime artifacts.
