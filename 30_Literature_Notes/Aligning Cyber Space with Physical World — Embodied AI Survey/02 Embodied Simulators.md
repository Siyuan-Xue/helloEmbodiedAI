---
title: "Embodied Simulators"
aliases:
  - "Embodied Simulation"
tags:
  - paper-note
  - embodied-ai
  - simulators
source: "[[Aligning Cyber Space with Physical World — Embodied AI Survey|Embodied AI Survey Notes]]"
---

# Embodied Simulators

## Why Simulators Matter

Real-world robot training is slow because it proceeds in real time and cannot easily be parallelized. It is also costly and difficult to reproduce.

Embodied simulators are vital because they provide:

- Cost-effective experimentation
- Safety for potentially hazardous scenarios
- Scalability across diverse environments
- Rapid prototyping
- Broader accessibility for researchers
- Controlled environments for precise studies
- Data generation for training and evaluation
- Standardized benchmarks for algorithm comparison

## General Simulators

General-purpose simulators provide virtual environments that closely mimic the physical world. They support algorithm development and model training while offering cost, time, and safety advantages.

Key strengths:

- Strong physical dynamics
- Support for large-scale parallel reinforcement learning
- Adaptation to robotic arms, autonomous vehicles, quadruped robots, and other robot types

Limitation:

- Scenes are often simple and lack realistic household furniture and interactive daily objects.

## Real-Scene-Based Simulators

Real-scene-based simulators aim to make simulated environments as close to the real world as possible. This creates high requirements for complexity and realism.

Key strengths:

- Based on 3D-scanned real houses
- Include many interactive objects such as furniture and kitchenware
- Provide visual environments close to real household scenarios

Limitation:

- Physical engines are usually less precise, so they are less suitable for complex dynamics or high-precision robotic control training.
