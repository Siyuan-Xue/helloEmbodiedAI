---
title: "Source README Snapshots"
type: source-note
status: active
tags:
  - source
  - snapshots
---

# Source README Snapshots

This directory stores fallback README snapshots when full git mirrors are unavailable.

Expected filenames:

- `HCPLab-SYSU--Embodied_AI_Paper_List.README.md`
- `zchoi--Awesome-Embodied-Robotics-and-Agent.README.md`
- `MilkClouds--awesome-vla-study.README.md`
- `ChanganVR--awesome-embodied-vision.README.md`
- `linchangyi1--Awesome-Touch.README.md`

After adding or updating snapshots, run:

```bash
python3 scripts/update_sources.py --no-network
```
