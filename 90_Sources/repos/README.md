---
title: "Source Git Mirrors"
type: source-note
status: active
tags:
  - source
  - git
---

# Source Git Mirrors

This directory is reserved for local git mirrors of source repositories.

Expected clone targets:

- `HCPLab-SYSU--Embodied_AI_Paper_List`
- `zchoi--Awesome-Embodied-Robotics-and-Agent`
- `MilkClouds--awesome-vla-study`
- `ChanganVR--awesome-embodied-vision`
- `linchangyi1--Awesome-Touch`

Run from the vault root:

```bash
python3 scripts/update_sources.py
```

If network access is unavailable, place README snapshots in `90_Sources/snapshots/` and run:

```bash
python3 scripts/update_sources.py --no-network
```
