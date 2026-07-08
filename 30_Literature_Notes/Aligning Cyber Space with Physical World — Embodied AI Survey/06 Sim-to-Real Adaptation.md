---
title: "Sim-to-Real Adaptation"
aliases:
  - "Sim-to-Real"
tags:
  - paper-note
  - embodied-ai
  - sim-to-real
  - world-models
source: "[[Aligning Cyber Space with Physical World — Embodied AI Survey|Embodied AI Survey Notes]]"
---

# Sim-to-Real Adaptation

Sim-to-real adaptation transfers capabilities or behaviors learned in simulated environments to real-world scenarios.

## Embodied World Model

### End-to-End

End-to-end means that a model takes raw observations, such as images or text, and directly outputs robot control actions. There is no manually separated intermediate procedure or independent submodule; the whole network completes reasoning, localization, and action generation in an integrated flow.

World Models can build end-to-end mapping networks. They use generation or prediction to anticipate the next environmental state and make action decisions based on state prediction. This can support vision-to-action mappings and even arbitrary input-output mappings.

### VLA and World Models

| Dimension | World Model (WM) | Vision-Language-Action (VLA) |
| --- | --- | --- |
| Training process | Learns from physical interaction data from scratch. | Pretrains on large-scale internet image-text data, then fine-tunes with robot data. |
| Capability level | Mainly captures low-level physical dynamics. | Combines language, commonsense knowledge, and long-horizon high-level planning. |
| Suitable scenarios | Standardized tasks with structured inputs and outputs. | Complex open-ended embodied tasks without fixed procedures. |

### Limitations of World Models

1. They lack general pretrained commonsense and learn slowly from interaction data.
2. They mainly model low-level physics and lack high-level semantic reasoning.
3. They cannot understand abstract natural-language instructions well.
4. They fit standardized tasks with structured inputs and outputs better than complex, unstructured, open-ended embodied tasks.

### Learning the World Environment

There are three ways to learn the world environment:

- Generative: directly generates full multi-modal raw data and learns world regularities autonomously, but requires large computation, may distort reality, and is hard to interpret.
- Predictive: performs state prediction in latent feature space; it is lightweight and generalizes better, but may be unstable in unfamiliar environments and difficult to interpret.
- Knowledge-driven: embeds physical or commonsense priors manually; it is reliable and interpretable and is strong for building simulation training environments, but depends heavily on hand-designed knowledge.

## Data Collection and Training

The method improves sim-to-real transfer through several steps:

1. Train robots with reinforcement learning in simulation to establish foundational strategies.
2. Deploy those strategies on real robots.
3. Let humans intervene through real-time remote control when errors occur.
4. Use intervention data to train a residual policy.
5. Combine the foundational policy and residual policy to produce smoother real-world trajectories after sim-to-real transfer.

## Embodied Control

Embodied control aims to help robots acquire new skills through interaction and learning from the environment, so that they can adapt to and complete complex tasks.

It learns through environmental interaction and optimizes behavior with a reward mechanism to obtain the optimal policy. This avoids some drawbacks of traditional physical modeling methods.

Two main types:

- Deep Reinforcement Learning (DRL)
- Imitation Learning

### Deep Reinforcement Learning

DRL adapts well to high-dimensional inputs such as images and to complex robotic motion control. It can work with task-planning modules to optimize action policies, but it requires massive trial-and-error interaction data and has high training cost.

### Imitation Learning

Imitation Learning centers on expert demonstration data. It reduces DRL's dependence on large-scale trial-and-error samples and improves data efficiency. A common practical pattern is offline pretraining combined with online reinforcement-learning fine-tuning.
