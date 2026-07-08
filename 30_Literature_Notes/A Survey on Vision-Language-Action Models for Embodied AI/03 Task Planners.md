---
title: "Task Planners"
aliases:
  - "VLA Task Planners"
tags:
  - paper-note
  - embodied-ai
  - vla
  - planning
source: "[[30_Literature_Notes/A Survey on Vision-Language-Action Models for Embodied AI|VLA Survey Notes]]"
---

# Task Planners

## Planner Frame

Task planners operate above low-level control policies. Their role is to decompose a complex user instruction into subtasks that low-level policies can execute:

$$
\hat{p} \sim \pi_\phi(p \mid \ell, s_t)
$$

This makes VLA systems more capable on long-horizon tasks, because the planner handles task decomposition while the control policy focuses on physical execution.

## Monolithic Task Planners

Monolithic task planners use a single LLM or multimodal LLM to generate task plans through a tailored framework or finetuning on embodied datasets.

### End-to-End Task Planners

End-to-end planners use Internet-scale model knowledge for embodied planning. The draft treats them as similar in spirit to large VLAs, because one integrated model performs high-level reasoning and plan generation.

### End-to-End Planners With 3D Vision

Some planners incorporate 3D vision. Since most current multimodal LLMs take images as their visual input, these systems usually require architectural changes to handle 3D inputs such as point clouds or other spatial representations.

### Grounded Task Planners

Grounded task planning generates high-level actions while considering whether those actions can actually be executed by low-level control policies.

## Modular Task Planners

Modular task planners assemble off-the-shelf LLMs, VLMs, object detectors, and control policies. This makes them closer to a tool-use architecture.

### Language-Based Task Planners

Language-based planners use natural language descriptions as the exchange medium for multimodal information. This makes LLM and VLM integration smoother because both components communicate in language space.

### Code-Based Task Planners

Code-based planners use the code-generation ability of LLMs to produce executable programs. Object detectors, VLMs, and control policies can then be called through APIs.

## Strengths and Limitations

| Planner type | Strength | Limitation |
| --- | --- | --- |
| Monolithic grounded planners | Focus on generating executable plans. | Training large embodied models is expensive. |
| End-to-end models | Can be finetuned on specialized embodied data for stronger task performance. | Training and deployment costs are substantial. |
| Modular planners | Easier to deploy because they reuse existing LLMs and VLMs. | Need careful integration across components. |
| Language-based planners | Integrate naturally with LLMs and VLMs in language space. | Often require extra alignment from generated plans to admissible low-level instructions. |
| Code-based planners | Offer debugging and stronger controllability. | Require API wrappers, clear documentation, and strong underlying programming ability. |

## Takeaway

The planner section clarifies the high-level side of VLA systems. Low-level policies predict robot actions, while task planners translate broad user goals into executable subgoals.
