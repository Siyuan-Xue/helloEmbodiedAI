---
title: "Introduction and Framework"
aliases:
  - "Embodied AI Framework"
tags:
  - paper-note
  - embodied-ai
  - framework
source: "[[Aligning Cyber Space with Physical World — Embodied AI Survey|Embodied AI Survey Notes]]"
---

# Introduction and Framework

## Research Targets

The survey highlights four main research targets:

1. Embodied perception
2. Embodied interaction
3. Embodied agent
4. Sim-to-real adaptation

Embodied agents are considered strong carriers for Multi-modal Large Models (MLMs), because MLMs inject perception, interaction, and planning capabilities into embodied models.

The embodied agent is the most prominent basis of Embodied AI because it connects perception, interaction, planning, and physical execution.

However, current MLMs are still limited in:

- Long-term memory
- Understanding complex intentions
- Decomposing complex tasks

The key techniques span computer vision, natural language processing, and robotics. The most representative areas are embodied perception, embodied interaction, embodied agents, and sim-to-real robotic control.

## Vision Encoders, LLMs, MLMs, and World Models

The relationship can be understood as a bottom-up hierarchy:

| Level | Component | Role |
| --- | --- | --- |
| Input layer | Vision encoders | Convert raw visual data into representations. They are visual input modules for MLMs and cannot independently complete human-robot interaction. |
| Foundation layer | Large Language Models (LLMs) | Provide the core language understanding and logical reasoning abilities that MLMs rely on for semantic output. |
| Fusion layer | Multi-modal Large Models (MLMs) | Combine a vision encoder with an LLM to bridge vision and language. This is a common basis for Vision-Language-Action (VLA) models. |
| Decision layer | World Models (WMs) | Build on MLMs as a semantic foundation and add temporal prediction, environment simulation, memory, and physical-law understanding. |

MLMs support three basic embodied capabilities:

- Multi-modal active perception
- Human-robot interaction
- Basic task planning

World Models exhibit strong simulation capabilities and a promising understanding of physical laws. This helps embodied models understand both virtual and physical environments more comprehensively.
