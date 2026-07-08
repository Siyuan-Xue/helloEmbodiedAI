---
title: "Zotero First Paper Setup"
type: workflow
status: active
tags:
  - zotero
  - workflow
  - embodied-ai
---

# Zotero First Paper Setup

Use this workflow for the first paper already represented in this vault:

[[30_Literature_Notes/Aligning Cyber Space with Physical World — Embodied AI Survey|Aligning Cyber Space with Physical World]]

## 1. Install Zotero

Install both:

- Zotero desktop app
- Zotero Connector for your browser

Download page: https://www.zotero.org/download/

The Connector is important because it saves bibliographic metadata from pages such as arXiv, publisher pages, Google Scholar, and library catalogs.

## 2. Create Collections

In Zotero desktop:

1. In the left sidebar, right-click `My Library`.
2. Choose `New Collection...`.
3. Create `Embodied AI`.
4. Right-click `Embodied AI`.
5. Choose `New Subcollection...`.
6. Create `00 Surveys`.

For this paper, the target collection is:

```text
My Library
└─ Embodied AI
   └─ 00 Surveys
```

## 3. Import This Paper

Open this arXiv page in your browser:

https://arxiv.org/abs/2407.06886

Then:

1. Make sure Zotero desktop is open.
2. Click the Zotero Connector icon in the browser toolbar.
3. In the save popup, choose collection `Embodied AI/00 Surveys`.
4. Let Zotero save the item and PDF if it can.

Prefer importing from the arXiv abstract page, not from the PDF page. The abstract page usually gives Zotero cleaner metadata.

## 4. If You Already Have the PDF File

If Zotero imported the item but did not attach the PDF:

1. Find the paper item in Zotero.
2. Drag your local PDF file onto that item.
3. Make sure the PDF appears indented under the paper item.

Do not leave the PDF as a standalone item. It should be a child attachment of the bibliographic item.

After verifying the PDF opens inside Zotero, you can delete the original downloaded PDF from Downloads/Desktop to avoid duplicate files.

## 5. Add Tags

Select the paper item in Zotero and add these tags:

```text
source:hcplab
topic:world-model
topic:sim2real
status:read
priority:core
```

Use collections for broad shelves and tags for cross-cutting labels.

## 6. Check Metadata

For this paper, Zotero should contain:

```text
Title: Aligning Cyber Space with Physical World: A Comprehensive Survey on Embodied AI
Year: 2024
arXiv: 2407.06886
Authors: Yang Liu; Weixing Chen; Yongjie Bai; Xiaodan Liang; Guanbin Li; Wen Gao; Liang Lin
```

If metadata is missing or obviously wrong, edit it in Zotero's right sidebar.

## 7. Citekey

Without Better BibTeX, you can leave Obsidian's `zotero_key` blank for now.

If you install Better BibTeX, use or pin a citekey like:

```text
liu2024aligning
```

Then fill this back into the Obsidian paper note:

```yaml
zotero_key: "liu2024aligning"
```

## 8. Division of Labor

Zotero stores:

- PDF
- metadata
- tags
- citation key
- PDF highlights and annotations

Obsidian stores:

- graph placement
- reading synthesis
- concept links
- roadmap position
- `zotero_key`

Do not create a duplicate PDF library inside this vault.
