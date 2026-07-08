---
title: "Components of VLA"
aliases:
  - "VLA Components"
tags:
  - paper-note
  - embodied-ai
  - vla
source: "[[30_Literature_Notes/A Survey on Vision-Language-Action Models for Embodied AI|VLA Survey Notes]]"
---

# Components of VLA

## Component Frame

VLA models are closely related to three lines of work: individual model components, low-level control policies, and high-level task planners. This module focuses on the first line.

## Reinforcement Learning

Reinforcement learning is a foundation for embodied AI and VLA models. DQN showed that policies can be trained end-to-end from high-dimensional pixels. RL trajectories also fit the sequence-modeling view used by Transformers, because states, actions, and rewards form temporal sequences.

The draft highlights a two-way relationship between RL and LLMs:

- RLHF and related feedback methods can improve robot learning, sparse-reward handling, and safety.
- LLMs can help design better RL frameworks and reward functions.

## Pretrained Visual Representations

The vision encoder directly affects VLA performance because it provides information about the current state, including object categories, positions, and affordances. In a VLA, the normalized feature vectors produced by the vision encoder are the basis for understanding the environment.

| Function | Role in VLA |
| --- | --- |
| Raw image compression | Converts RGB or depth images into lower-dimensional feature vectors while retaining object categories, spatial position, and affordances. |
| Vision-language alignment | Places visual features and text features in a shared representation space so instructions can match scenes. |
| Temporal video modeling | Uses video representations such as R3M or VIP to capture frame-to-frame changes caused by actions. |
| General pretrained priors | Reduces dependence on expensive robot data by transferring large-scale image, text, or video pretraining to downstream robot tasks. |

## Video Representations

Video representations can be built by concatenating single-frame PVRs, but they can also exploit temporal structure through time contrastive learning, masked autoencoding, and other video-specific objectives. The draft also notes that video can support 3D representations such as NeRF and 3D Gaussian splatting, with the latter offering stronger rendering speed and quality.

Video is naturally multi-view:

- Spatial multi-view: robots may use synchronized top, wrist, and side cameras to observe the same scene from multiple angles.
- Temporal multi-view: as the robot or camera moves, each frame introduces a new viewpoint over time.

A typical manipulation setup combines a global overhead camera with a local wrist camera. The global camera helps the policy understand layout, while the wrist camera captures fine-grained gripper interaction.

## Dynamics Learning

Dynamics learning appears in two directions:

$$
\hat{s}_{t+1} \leftarrow f_{\mathrm{fwd}}(s_t, a_t)
$$

$$
\hat{a}_t \leftarrow f_{\mathrm{inv}}(s_t, s_{t+1})
$$

Forward dynamics predicts the next state from the current state and action. Inverse dynamics infers the action that caused a state transition.

## World Models

A world model encodes commonsense knowledge about the world and predicts future states for a given action:

$$
\hat{s}_{t+1} \sim P(s_{t+1} \mid s_t, a_t)
$$

This enables model-based control and planning, because an embodied agent can search for a good action sequence in imagined space before executing actions in the real world. The draft distinguishes world models from ordinary forward dynamics: forward dynamics is often used as a pretraining task or auxiliary loss, while a world model can function as its own predictive module.

Visual world models can also generate images, videos, or 3D scenes of future states, which makes them closer to physical-world simulation and useful for generating new trajectories.

## LLM-Induced World Models

LLMs contain commonsense, physical, causal, and everyday knowledge. Injecting this knowledge into world models can compensate for weaknesses in purely visual world models, especially when visual models produce implausible rollouts or struggle with long-horizon planning.

## Reasoning

Reasoning relies on large-model chain-of-thought style inference. The draft separates two uses:

- High-level task planning, where language logic helps decompose and refine long tasks.
- Low-level robot control, where reasoning can help inspect visual features, motion intent, and action choices before the policy acts.

Reasoning and high-level planning are naturally compatible because both operate heavily in language space.

## Policy Steering

Policy steering improves VLA action output at test time without retraining. The core idea is to sample multiple candidate actions, score or verify them, and execute the best candidate.

## Strengths and Limitations

| Component | Strength | Limitation or tradeoff |
| --- | --- | --- |
| CLIP and time-contrastive PVRs | Strong image-level semantics. | Weaker pixel-level detail for precise manipulation. |
| MAE-style PVRs | Strong pixel-level detail for position, depth, and segmentation. | Less focused on global language-aligned semantics. |
| DINOv2 and I-JEPA | DINOv2 balances global and pixel features; I-JEPA is strong on lower-level visual detail. | The best representation depends on task precision and generalization needs. |
| Theia | Fuses multiple vision foundation models. | More complex than relying on one encoder. |
| Forward dynamics | Harder prediction task with stronger learning signal. | More difficult than inverse dynamics. |
| Inverse dynamics | Useful for labeling unlabeled robot videos with actions. | Less directly predictive of future environment state. |
| World models | Support low-level physical prediction and imagined planning. | Need grounded physical consistency. |
| CoT reasoning | Supports high-level logical decomposition and plan repair. | Better aligned with language planning than raw physical simulation. |
