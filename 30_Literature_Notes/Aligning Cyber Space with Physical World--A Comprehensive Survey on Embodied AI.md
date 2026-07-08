---
title: "Aligning Cyber Space with Physical World: A Comprehensive Survey on Embodied AI"
aliases:
  - "Embodied AI Survey"
  - "Aligning Cyber Space with Physical World"
tags:
  - paper-note
  - embodied-ai
  - multimodal-large-models
  - world-models
type: paper-note
source_type: survey
authors:
  - Yang Liu
  - Weixing Chen
  - Yongjie Bai
  - Xiaodan Liang
  - Guanbin Li
  - Wen Gao
  - Liang Lin
year: 2024
arxiv_id: "2407.06886"
status: refined
priority: core
areas:
  - perception
  - interaction
  - agent
  - sim2real
  - world-model
  - platform
source_repos:
  - hcplab
zotero_key: ""
zotero_select: ""
zotero_pdf: ""
paper_url: "https://arxiv.org/abs/2407.06886"
code_url: ""
project_url: "https://github.com/HCPLab-SYSU/Embodied_AI_Paper_List"
created: 2026-07-07
---

# Aligning Cyber Space with Physical World: A Comprehensive Survey on Embodied AI

> [!note] Scope
> These notes preserve the concepts originally selected in the draft. The paper is used only to verify terminology, section order, and formula meaning.

## Module Map

- [[30_Literature_Notes/Aligning Cyber Space with Physical World - Embodied AI Survey/00 Introduction and Framework|00 Introduction and Framework]]
- [[30_Literature_Notes/Aligning Cyber Space with Physical World - Embodied AI Survey/01 Embodied Robots|01 Embodied Robots]]
- [[30_Literature_Notes/Aligning Cyber Space with Physical World - Embodied AI Survey/02 Embodied Simulators|02 Embodied Simulators]]
- [[30_Literature_Notes/Aligning Cyber Space with Physical World - Embodied AI Survey/03 Embodied Perception|03 Embodied Perception]]
- [[30_Literature_Notes/Aligning Cyber Space with Physical World - Embodied AI Survey/04 Embodied Interaction|04 Embodied Interaction]]
- [[30_Literature_Notes/Aligning Cyber Space with Physical World - Embodied AI Survey/05 Embodied Agent|05 Embodied Agent]]
- [[30_Literature_Notes/Aligning Cyber Space with Physical World - Embodied AI Survey/06 Sim-to-Real Adaptation|06 Sim-to-Real Adaptation]]
- [[30_Literature_Notes/Aligning Cyber Space with Physical World - Embodied AI Survey/07 Challenges and Future Directions|07 Challenges and Future Directions]]
- [[30_Literature_Notes/Aligning Cyber Space with Physical World - Embodied AI Survey/Vocabulary|Vocabulary]]

## Graph Links

- Atlas: [[00_MOC/Embodied AI Atlas]]
- Foundations: [[10_Areas/Foundations]]
- Platforms: [[10_Areas/Platforms Robots Simulators Datasets]]
- Perception: [[10_Areas/Perception and Grounding]]
- Interaction: [[10_Areas/Interaction Manipulation Tactile]]
- Agents: [[10_Areas/Agents Planning and Memory]]
- VLA: [[10_Areas/VLA Robot Foundation Models]]
- World models and sim-to-real: [[10_Areas/World Models Sim2Real Evaluation]]
- Zotero workflow: [[00_MOC/Zotero Workflow]]

## Zotero Link

- Zotero collection: `Embodied AI/00 Surveys`
- Zotero tags: `source:hcplab`, `topic:world-model`, `topic:sim2real`, `status:read`, `priority:core`
- Suggested citekey after import: `liu2024aligning`
- PDF and highlights should live in Zotero. This note stores synthesis, graph placement, and reading conclusions.

## Core Takeaways

- The survey organizes Embodied AI around four main research targets: embodied perception, embodied interaction, embodied agents, and sim-to-real adaptation.
- Embodied agents are treated as promising carriers for Multi-modal Large Models (MLMs), because MLMs provide strong perception, interaction, and planning capabilities.
- Current MLMs remain limited in long-term memory, complex intention understanding, and complex task decomposition.
- The representative technical basis spans computer vision, natural language processing, and robotics.
- A useful hierarchy is: vision encoders -> Large Language Models (LLMs) -> Multi-modal Large Models (MLMs) -> World Models (WMs).

## Reading Index

Start with [[30_Literature_Notes/Aligning Cyber Space with Physical World - Embodied AI Survey/00 Introduction and Framework|Introduction and Framework]] for the conceptual hierarchy, then move through the survey modules in order. Use [[30_Literature_Notes/Aligning Cyber Space with Physical World - Embodied AI Survey/Vocabulary|Vocabulary]] as the word bank collected from the paper.
