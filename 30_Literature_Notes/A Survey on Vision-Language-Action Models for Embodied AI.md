---
title: "A Survey on Vision-Language-Action Models for Embodied AI"
aliases:
  - "VLA Survey"
  - "Vision-Language-Action Models for Embodied AI"
tags:
  - paper-note
  - embodied-ai
  - vla
  - robot-foundation-models
type: paper-note
source_type: survey
authors:
  - Yueen Ma
  - Zixing Song
  - Yuzheng Zhuang
  - Jianye Hao
  - Irwin King
year: 2025
venue: "IEEE Transactions on Neural Networks and Learning Systems"
doi: "10.1109/TNNLS.2025.3650584"
arxiv_id: "2405.14093"
status: refined
priority: core
areas:
  - vla
  - agent
  - interaction
  - perception
  - world-model
  - platform
tasks:
  - manipulation
  - planning
  - grounding
methods:
  - rl
  - imitation-learning
  - diffusion
  - llm
  - vlm
  - vla
  - world-model
modalities:
  - vision
  - language
  - action
  - audio
  - multimodal
embodiments:
  - manipulator
  - mobile-robot
source_repos: []
zotero_key: ""
zotero_select: ""
zotero_pdf: ""
paper_url: "https://arxiv.org/abs/2405.14093"
code_url: ""
project_url: "https://github.com/yueen-ma/Awesome-VLA"
created: 2026-07-08
---

# A Survey on Vision-Language-Action Models for Embodied AI

> [!note] Scope
> These notes preserve the concepts recorded in the draft. The PDF was used only to verify metadata, terminology, formulas, and section order.

## One-Sentence Claim

Vision-Language-Action (VLA) models are a central embodied AI architecture because they connect language instructions, visual perception, and robot action generation in one policy or planning stack.

## Problem

Unlike conversational AI, embodied AI must control physical embodiments that interact with the environment. Language-conditioned robotic tasks therefore require a policy that can understand instructions, perceive the scene, and generate appropriate actions. Compared with earlier deep reinforcement learning policies, VLAs aim for stronger versatility, dexterity, and generalization in complex environments.

## Method

The survey organizes VLA research into three major lines:

1. Components of VLA models, including reinforcement learning, pretrained visual representations, video representations, dynamics learning, world models, reasoning, and policy steering.
2. Low-level control policies that integrate perception modules with action decoders to execute language instructions.
3. High-level task planners that decompose long-horizon user instructions into subtasks for low-level policies.

## Evidence

The draft emphasizes the architectural role of vision encoders, language encoders, and action decoders; the progression from non-Transformer policies to large VLAs; and the planner split between monolithic and modular systems.

## Limits

The strongest limitations recorded in the draft are architectural tradeoffs:

- PVRs with strong global semantics can miss pixel-level detail needed for precise manipulation.
- Forward dynamics is harder than inverse dynamics but can provide stronger training signal.
- World models and CoT-style reasoning both support embodied decisions, but they currently serve different roles: physical next-state prediction versus language-level task planning.
- Monolithic task planners can be more integrated but expensive to train, while modular planners are easier to deploy but need careful alignment with executable low-level actions.

## Module Map

- [[30_Literature_Notes/A Survey on Vision-Language-Action Models for Embodied AI/01 Components of VLA|01 Components of VLA]]
- [[30_Literature_Notes/A Survey on Vision-Language-Action Models for Embodied AI/02 Low-Level Control Policies|02 Low-Level Control Policies]]
- [[30_Literature_Notes/A Survey on Vision-Language-Action Models for Embodied AI/03 Task Planners|03 Task Planners]]
- [[30_Literature_Notes/A Survey on Vision-Language-Action Models for Embodied AI/Vocabulary|Vocabulary]]

## Coverage Note

The source note names Datasets and Benchmarks as a later section, but it does not record details from that section. This organized note keeps that boundary visible without adding new survey content from the PDF.

## Graph Links

- Atlas: [[00_MOC/Embodied AI Atlas]]
- VLA area: [[10_Areas/VLA Robot Foundation Models]]
- Agent planning: [[10_Areas/Agents Planning and Memory]]
- Interaction: [[10_Areas/Interaction Manipulation Tactile]]
- Perception: [[10_Areas/Perception and Grounding]]
- World models: [[10_Areas/World Models Sim2Real Evaluation]]
- Platforms and datasets: [[10_Areas/Platforms Robots Simulators Datasets]]
- Concepts: [[20_Concepts/Vision-Language-Action]], [[20_Concepts/World Models]]

## Zotero

- Zotero key:
- Zotero collection:
- Zotero tags:
