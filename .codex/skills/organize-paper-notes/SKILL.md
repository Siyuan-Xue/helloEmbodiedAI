---
name: organize-paper-notes
description: Organize rough paper reading notes into polished Obsidian research notes for this vault. Use when Codex needs to clean a mixed-language or informal Markdown paper note, find and read the same-directory same-name PDF with the PDF plugin as required source material, split notes into modular literature notes, normalize metadata with the vault's Paper Note template and Knowledge Graph Schema, add graph links, update Resource Registry rows, handle vocabulary lists, or validate paper-note structure. If the PDF is missing, ask the user to add it before proceeding. Do not perform or recommend Zotero operations; leave Zotero-related fields blank unless the user explicitly provides values.
---

# Organize Paper Notes

Use this skill to turn a rough paper-reading note into a vault-native literature note set and register it in the current Obsidian graph.

## Core Rules

- Treat the user's existing note as the content boundary. Do not add paper content the user did not record.
- Require the paper source: find a PDF in the same directory with the same stem as the rough Markdown note. If it is missing, ask the user to add it and stop until it is available.
- Use the PDF plugin / `PDF:pdf` workflow to read the paper. Use the paper only to verify terminology, section order, formula meaning, metadata, and vocabulary context.
- Do not perform or recommend Zotero operations. Leave `zotero_key`, `zotero_select`, and `zotero_pdf` blank unless the user provides values.
- Preserve the user's learning focus while improving grammar, phrasing, Markdown structure, and Obsidian readability.
- Do not create new top-level areas or concept notes unless the user explicitly asks.
- After the refined notes and vault registration are complete, ask the user whether to delete the source PDF from the vault. Do not delete it without explicit confirmation.

## Required Vault Context

Before editing notes, inspect the current vault files:

- `99_Templates/Paper Note.md` for the paper-note frontmatter and section baseline.
- `00_MOC/Knowledge Graph Schema.md` for allowed `area`, `task`, `method`, `modality`, `embodiment`, `source_repo`, and `status` values.
- `90_Sources/Resource Registry.md` for the curated resource table format.
- Relevant `10_Areas/*.md` and existing `20_Concepts/*.md` files for graph links.

Read `references/obsidian-paper-note-workflow.md` when performing the full cleanup and registration workflow.

## Output Pattern

- Put refined paper notes under `30_Literature_Notes`.
- For short notes, keep one polished note.
- For long or multi-section notes, create a main index note plus a sibling module folder.
- Use YAML properties, clean headings, wikilinks, callouts when helpful, compact tables, and Obsidian-compatible LaTeX.
- Move vocabulary into a structured `Vocabulary.md` module when the source note has a word list.
- Update `90_Sources/Resource Registry.md` only when enough metadata exists for a clean curated row.

## Validation

After editing, run:

```bash
python3 .codex/skills/organize-paper-notes/scripts/validate_note_set.py 30_Literature_Notes/<note-or-folder>
```

Use the validator output to fix wikilinks, empty headings, placeholders, unintended Chinese text, duplicate registry IDs, and unmatched LaTeX block delimiters.

If the validator reports a remaining PDF, ask the user whether to delete it because paper PDFs should not remain in this vault after note organization.
