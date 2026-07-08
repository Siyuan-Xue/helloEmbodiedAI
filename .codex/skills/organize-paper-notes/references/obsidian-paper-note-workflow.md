# Obsidian Paper Note Workflow

## Goal

Transform a rough paper note into a polished Obsidian literature note set, then register the paper in the current vault graph. The workflow is based on the Embodied AI survey cleanup: a mixed Chinese/English single-file note became a main paper index plus section modules, vocabulary, graph links, and a registry row.

## 1. Ground In The Vault

Inspect these files first:

- `99_Templates/Paper Note.md`: copy its frontmatter shape and core sections.
- `00_MOC/Knowledge Graph Schema.md`: use its controlled vocabulary for graph fields.
- `90_Sources/Resource Registry.md`: follow the existing table format for curated entries.
- `10_Areas/*.md`: link the paper to relevant area pages.
- `20_Concepts/*.md`: link only existing concept notes that clearly match the paper.

Do not assume the vault layout is unchanged; verify paths before editing.

## 2. Locate The Required Paper PDF

The paper PDF is required source material for this workflow.

Default discovery rule:

- Identify the rough Markdown note selected by the user.
- Look in the same directory for a `.pdf` with the same stem as the note.
- Example: `Paper Title.md` should have `Paper Title.pdf` beside it while the note is being organized.

If the exact same-stem PDF is missing:

- Look for obvious same-title variants only when the match is unambiguous, such as punctuation-normalized filenames.
- If no clear match exists, ask the user to add the paper PDF to the same directory and stop before editing.

When the PDF exists:

- Use the PDF plugin / `PDF:pdf` workflow to read or extract enough paper context.
- Use the PDF to verify terminology, section order, formula meaning, metadata, and vocabulary context.
- Do not use the PDF to expand the user's notes with content they did not record.

After note cleanup and vault registration are complete:

- Ask the user whether to delete the source PDF from the vault.
- Do not delete the PDF without explicit user confirmation.
- Explain that PDFs should not remain in this vault after organization; the vault stores refined notes and graph placement, not source PDFs.

## 3. Define Scope

Use the user's note as the source of truth for content scope.

Allowed uses of the paper/PDF:

- Verify technical terminology.
- Confirm section order for reorganizing the user's notes.
- Clarify formulas already present in the notes.
- Check metadata such as title, authors, year, DOI, arXiv ID, paper URL, project URL, or source repository.
- Understand vocabulary context.

Do not add datasets, methods, citations, examples, claims, or subsections merely because they appear in the paper.

## 4. Clean And Restructure The Note

For the rough note:

- Fix grammar, spelling, rough phrasing, informal fragments, and copied PDF line-wrap artifacts.
- Translate Chinese explanations into idiomatic English, unless the user asks for bilingual output.
- Normalize headings into a readable hierarchy.
- Convert formulas to Obsidian-compatible LaTeX blocks.
- Convert repeated comparisons into compact tables when this makes the note clearer.
- Use callouts sparingly for central summaries or scope boundaries.

For long notes:

- Keep `30_Literature_Notes/<Paper Title>.md` as the main index.
- Create `30_Literature_Notes/<Paper Title - Short Suffix>/` beside it.
- Split modules according to the user's existing note flow, usually matching the paper's major sections.
- Add a `Module Map` in the main note linking to each module.

For short notes:

- Keep one polished note under `30_Literature_Notes`.
- Still include graph metadata and graph links.

## 5. Metadata Rules

Use the current `Paper Note.md` template as the field baseline.

Recommended defaults:

```yaml
type: paper-note
source_type: paper
status: refined
priority: ""
zotero_key: ""
zotero_select: ""
zotero_pdf: ""
```

Set `source_type: survey` for survey papers. Fill known values for:

- `title`
- `aliases`
- `authors`
- `year`
- `venue`
- `doi`
- `arxiv_id`
- `areas`
- `tasks`
- `methods`
- `modalities`
- `embodiments`
- `source_repos`
- `paper_url`
- `code_url`
- `project_url`

Use YAML lists for multi-value fields. Leave unknown fields blank rather than guessing.

Do not add Zotero workflow instructions. Keep Zotero-related fields blank unless the user provides exact values.

## 6. Graph Registration

Add a `Graph Links` section to the paper note.

Include:

- The top-level atlas or roadmap when relevant.
- Relevant `10_Areas` pages selected from `areas`.
- Existing `20_Concepts` pages when they directly match the note.
- Related paper notes only when the relationship is explicit in the user's notes or already present in the vault.

Do not create new `10_Areas` pages. Do not create new `20_Concepts` pages unless the user asks.

## 7. Resource Registry

Update `90_Sources/Resource Registry.md` only when the paper has enough metadata for a curated row.

Follow the existing table shape:

```markdown
| ID | Title | Type | Area | Source | Status | Destination |
| --- | --- | --- | --- | --- | --- | --- |
```

Rules:

- Use a stable lowercase ID, such as `paper-short-title`.
- Use a wikilink to the paper note in `Title`.
- Use `paper` or `survey` in `Type`.
- Use slash-separated values in `Area`.
- Use known `source_repos` values in `Source`; use `local` if no source repo is known.
- Use the paper note's `priority` or `status` for `Status`.
- Use `Obsidian paper note` or a concise vault destination phrase.
- Avoid duplicate IDs; if an ID already exists, update that row instead of adding another.

## 8. Vocabulary

If the source note contains a vocabulary list:

- Move it into a `Vocabulary.md` module for modular notes, or a `Vocabulary` section for single-note output.
- Use actual Oxford or Cambridge Dictionary entries when the user requests dictionary-backed definitions.
- Keep dictionary quotations short.
- Include word, part of speech, dictionary definition, optional Chinese gloss, paper-context meaning, example, and source link.
- If web access is unavailable, mark dictionary definitions as pending instead of inventing wording.

Chinese glosses are allowed in vocabulary only when requested.

## 9. Validation Checklist

Before final response:

- Every section maps back to user-recorded content.
- The main note and module links resolve.
- `Graph Links` point to existing MOC, area, and concept notes.
- `90_Sources/Resource Registry.md` has no duplicate row ID.
- Zotero fields are blank unless user-provided values exist.
- There are no empty headings or TODO placeholders.
- Chinese text remains only where intentionally allowed.
- LaTeX block delimiters are balanced.
- Any source PDF left in the vault is reported and the user is asked whether to delete it.
- No PDF is deleted unless the user explicitly confirms.
