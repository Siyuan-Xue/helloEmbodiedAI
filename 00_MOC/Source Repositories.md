---
title: "Source Repositories"
type: source-map
status: active
tags:
  - source
  - embodied-ai
---

# Source Repositories

The repositories are raw input streams. The vault architecture lives in [[00_MOC/Embodied AI Atlas|Embodied AI Atlas]] and [[00_MOC/Knowledge Graph Schema|Knowledge Graph Schema]].

| Source | Local key | Role | Primary target |
| --- | --- | --- | --- |
| [HCPLab-SYSU/Embodied_AI_Paper_List](https://github.com/HCPLab-SYSU/Embodied_AI_Paper_List) | `hcplab` | Backbone paper taxonomy | surveys, simulators, perception, interaction, agents, sim-to-real, datasets |
| [zchoi/Awesome-Embodied-Robotics-and-Agent](https://github.com/zchoi/Awesome-Embodied-Robotics-and-Agent) | `zchoi` | Frontier robotics and agent tracker | VLA, planning, self-evolving agents, world models, benchmarks |
| [MilkClouds/awesome-vla-study](https://github.com/MilkClouds/awesome-vla-study) | `milkclouds` | VLA study sequence | VLA roadmap, robot foundation models |
| [ChanganVR/awesome-embodied-vision](https://github.com/ChanganVR/awesome-embodied-vision) | `changanvr` | Embodied vision and navigation | PointGoal, ObjectGoal, ImageGoal, VLN, EQA, exploration |
| [linchangyi1/Awesome-Touch](https://github.com/linchangyi1/Awesome-Touch) | `awesome-touch` | Tactile/contact-rich AI | tactile sensing, manipulation, sensors, products, labs |

## Local Storage

- Preferred git mirror path: `90_Sources/repos/`.
- README snapshot path: `90_Sources/snapshots/`.
- Generated registry path: [[90_Sources/Resource Registry.generated|Resource Registry.generated]].
- Curated registry and instructions: [[90_Sources/Resource Registry]].
- Update log: [[90_Sources/Repository Update Log]].

## Current Sync State

GitHub cloning and raw README download were attempted on 2026-07-08, but the network connection failed from this environment. The vault has been built to tolerate that: the update script can fill the generated registry as soon as network access is available or README snapshots are placed in `90_Sources/snapshots/`.

## Update Command

```bash
python3 scripts/update_sources.py
```

Offline dry run:

```bash
python3 scripts/update_sources.py --no-network
```
