---
title: "Resource Registry"
type: registry
status: active
tags:
  - registry
  - embodied-ai
---

# Resource Registry

This is the curated entry point for imported resources. Machine-generated imports should land in [[90_Sources/Resource Registry.generated|Resource Registry.generated]] first, then be reviewed here or promoted to an area/resource page.

## Import Pipeline

1. Update source repositories or README snapshots.
2. Run `python3 scripts/update_sources.py`.
3. Review [[90_Sources/Resource Registry.generated]].
4. Promote valuable resources into Zotero, area pages, or long-form Obsidian notes.

## Seed Nodes

| ID | Title | Type | Area | Source | Status | Destination |
| --- | --- | --- | --- | --- | --- | --- |
| `paper-aligning-cyber-space` | [[30_Literature_Notes/Aligning Cyber Space with Physical World — Embodied AI Survey|Aligning Cyber Space with Physical World]] | survey | perception/interaction/agent/sim2real/world-model/platform | hcplab | core | Zotero collection `Embodied AI/00 Surveys` + Obsidian paper note |
| `paper-vla-models-survey` | [[30_Literature_Notes/A Survey on Vision-Language-Action Models for Embodied AI|A Survey on Vision-Language-Action Models for Embodied AI]] | survey | vla/agent/interaction/perception/world-model/platform | local | core | Obsidian paper note |
| `source-hcplab` | [HCPLab-SYSU/Embodied_AI_Paper_List](https://github.com/HCPLab-SYSU/Embodied_AI_Paper_List) | note | platform/perception/interaction/agent/sim2real | hcplab | inbox | source stream |
| `source-zchoi` | [zchoi/Awesome-Embodied-Robotics-and-Agent](https://github.com/zchoi/Awesome-Embodied-Robotics-and-Agent) | note | agent/vla/world-model/platform | zchoi | inbox | source stream |
| `source-milkclouds` | [MilkClouds/awesome-vla-study](https://github.com/MilkClouds/awesome-vla-study) | note | vla/foundation/agent | milkclouds | inbox | source stream |
| `source-changanvr` | [ChanganVR/awesome-embodied-vision](https://github.com/ChanganVR/awesome-embodied-vision) | note | navigation/perception/sim2real | changanvr | inbox | source stream |
| `source-awesome-touch` | [linchangyi1/Awesome-Touch](https://github.com/linchangyi1/Awesome-Touch) | note | interaction/perception/platform/vla | awesome-touch | inbox | source stream |

## Promotion Rules

- Promote to Zotero when `type` is `paper` or `survey`.
- Promote to Zotero and Obsidian resource hub when `type` is `dataset`, `simulator`, or `benchmark` with a formal paper.
- Keep `code`, `product`, `lab`, and `course` in Obsidian unless they need formal citation.
- Promote to a long-form note only after reading, reproducing, or using the resource in an argument.
