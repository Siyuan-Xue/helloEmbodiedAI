---
title: "Embodied Agent"
aliases:
  - "Embodied Agents"
tags:
  - paper-note
  - embodied-ai
  - agents
  - planning
source: "[[Aligning Cyber Space with Physical World — Embodied AI Survey|Embodied AI Survey Notes]]"
---

# Embodied Agent

To complete a task, embodied agents typically follow two levels of planning:

1. Decompose an abstract and complex task into specific subtasks. This is high-level embodied task planning.
2. Implement these subtasks by using embodied perception and embodied interaction models, or by using the policy function of a foundation model. This is low-level embodied action planning.

## Embodied Multimodal Foundation Model

Embodied agents need to:

- Visually recognize the environment
- Understand spoken or language instructions
- Comprehend their own state
- Enable complex interaction and operation

### Robot Transformer: Native Strengths and Weaknesses

Strength:

- High-level semantic reasoning: understanding complex long-text instructions and decomposing multi-step long-horizon tasks.

Weaknesses:

1. Insufficient control-parameter precision: generative models can produce inaccurate continuous robot action coordinates or gripper poses, which limits precise robotic-arm control.
2. A gap between high-level and low-level planning: the high-level planner decides what to do, but the low-level controller must still determine how to move. Environmental changes can make real-time replanning difficult.

## Embodied Task Planning

Task planning corresponds to the high-level planning stage.

Relationship among three planning modes:

- LLM planning uses language and commonsense knowledge to plan.
- LLM + perception uses visual results to correct language-based planning.
- VLM planning plans directly from joint vision-language understanding.

These methods move from insufficiently grounded language planning toward visually grounded embodied planning.

However, they mainly solve task planning: what should be done first and what should be done next. Navigation, grasping, obstacle avoidance, and trajectory control are lower-level action planning and control problems. This explains why task-planning accuracy can be high while the final task-completion rate remains constrained by low-level execution ability.

## Embodied Action Planning

Action planning must handle real-world uncertainty, because the subtasks produced by task planning are not granular enough to guide efficient interaction with the environment.

### Modular Tool-Calling Approach

Architecture:

- LLMs or VLMs perform high-level task planning.
- Perception, grasping, and navigation models are used as low-level tools.
- These tools are called through APIs to execute subtasks step by step.

Advantages:

- Modules can be trained and replaced independently.

Limitation:

- There can be an information gap between high-level and low-level modules.

### Native End-to-End VLA Approach

Vision-Language-Action (VLA) models receive images and text together and directly output continuous robot actions. This integrates visual localization and action generation while reducing the need for multi-module interface coordination.
