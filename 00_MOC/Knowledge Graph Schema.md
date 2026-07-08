---
title: "Knowledge Graph Schema"
type: schema
status: active
tags:
  - schema
  - embodied-ai
---

# Knowledge Graph Schema

Every imported resource is represented as a lightweight graph node with stable fields. These fields let resources from different repositories land in the same research map.

## Node Fields

```yaml
title: ""
type: paper | survey | code | dataset | simulator | benchmark | course | product | lab | note
area: perception | navigation | interaction | agent | vla | world-model | sim2real | platform | foundation
task: objectnav | vln | manipulation | rearrangement | tactile | grounding | planning
method: rl | imitation-learning | diffusion | flow-matching | llm | vlm | vla | world-model
modality: vision | language | action | tactile | audio | proprioception | multimodal
embodiment: mobile-robot | manipulator | humanoid | dexterous-hand | legged | virtual-agent
source_repo: hcplab | zchoi | milkclouds | changanvr | awesome-touch
zotero_key: ""
status: inbox | to-read | reading | read | core | archived
paper_url: ""
code_url: ""
project_url: ""
```

## Type Rules

- `paper` and `survey`: add to Zotero when metadata is available.
- `dataset`, `simulator`, `benchmark`: add to Zotero only if there is a formal paper; always index in Obsidian.
- `code`, `course`, `product`, `lab`: index in Obsidian; add to Zotero only if it will be cited formally.
- `note`: use for internal maps, concept notes, and repository-level entries.

## Area Rules

- `foundation`: mathematical, ML, robotics, RL, diffusion, flow matching, control fundamentals.
- `platform`: robots, simulators, datasets, benchmarks, hardware infrastructure.
- `perception`: grounding, mapping, SLAM, 2D/3D perception, active perception.
- `navigation`: PointGoal, ObjectGoal, ImageGoal, VLN, EQA, audio-visual navigation, exploration.
- `interaction`: manipulation, rearrangement, dexterous control, tactile interaction, HRI.
- `agent`: task planning, action planning, memory, tool use, multi-agent systems.
- `vla`: robot foundation models that connect vision, language, and action.
- `world-model`: temporal prediction, simulation, physical reasoning, real2sim2real.
- `sim2real`: adaptation, transfer, robustness, deployment.

## Repository Mapping

| Source repo | Role | Primary landing areas |
| --- | --- | --- |
| `hcplab` | Backbone taxonomy | survey, platform, perception, interaction, agent, sim2real |
| `zchoi` | Frontier robotics and agents | vla, agent, world-model, platform, benchmark |
| `milkclouds` | VLA learning route | vla, foundation, agent |
| `changanvr` | Embodied vision/navigation | navigation, perception, sim2real, benchmark |
| `awesome-touch` | Tactile/contact-rich AI | interaction, perception, platform, vla |

## Update Invariant

Repository updates may add rows, change statuses, or add cross-links. They should not change the top-level area map unless a resource repeatedly fails to fit this schema after using multiple fields.
