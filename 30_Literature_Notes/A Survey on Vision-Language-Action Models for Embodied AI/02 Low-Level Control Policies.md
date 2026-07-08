---
title: "Low-Level Control Policies"
aliases:
  - "VLA Control Policies"
tags:
  - paper-note
  - embodied-ai
  - vla
  - control-policy
source: "[[30_Literature_Notes/A Survey on Vision-Language-Action Models for Embodied AI|VLA Survey Notes]]"
---

# Low-Level Control Policies

## Control Policy Frame

A VLA becomes a control policy by integrating an action decoder with perception modules such as vision encoders and language encoders. The policy executes language instructions by predicting low-level actions:

$$
\hat{a}_t \sim \pi_\theta(a_t \mid p, s_{\le t}, a_{<t})
$$

The same component may be described as a low-level policy, low-level controller, or action primitive.

## Architecture Progression

| Stage | Policy family | Core idea |
| --- | --- | --- |
| Early language-conditioned control | Non-Transformer policies | Demonstrates that language plus vision can control a robot. |
| Unified sequence modeling | Transformer-based policies | Represents vision, language, actions, and history as sequences. |
| Richer human input | Multimodal instructions | Lets users specify tasks with text, images, videos, clicks, or mixed prompts. |
| Spatial grounding | Policies with 3D vision | Moves from image-space position to real spatial position. |
| Action distribution modeling | Diffusion-based policies | Generates complex action distributions instead of one narrow action prediction. |
| Spatial and generative control | 3D vision plus diffusion | Combines 3D understanding with high-quality trajectory generation. |
| Safe execution | Motion-planning policies | Adds obstacles, constraints, and waypoints. |
| Lightweight execution | Point-based actions | Simplifies control by selecting key points. |
| Generalization | Large VLA | Uses large-model knowledge for cross-task, cross-environment, and cross-robot transfer. |

## Non-Transformer Control Policies

Early policies established the feasibility of language-conditioned visual control before Transformer architectures became dominant. The important lesson in the draft is not a single architecture, but the proof that visual state and language instruction can jointly guide robot action.

## Transformer-Based Policies

Transformer-based policies unify multimodal inputs and action histories in one sequence-processing architecture. This makes them a natural fit for VLA settings where state, instruction, and previous actions all influence the next action.

## Multimodal Instructions

Multimodal instruction policies broaden the user interface. A task can be expressed through language, images, video demonstrations, clicks, or other prompt forms. This matters because embodied users often communicate goals by pointing, showing, or demonstrating rather than only writing text.

## 3D Vision

Policies with 3D vision upgrade the grounding target from image coordinates to physical-space coordinates. This is especially important for manipulation, where the robot must reason about object pose, distance, and affordances in the execution space.

## Diffusion-Based Policies

Diffusion policies model richer action distributions. Instead of predicting a single deterministic action, they can represent multiple plausible trajectories and select actions through a generative process.

## Motion Planning

Motion-planning policies connect learned VLA outputs to safer execution. They can incorporate constraints, avoid obstacles, and represent waypoints that make the generated action sequence executable in the physical environment.

## Point-Based Actions

Point-based actions reduce complex control into key point selection. This can make policies lighter and easier to deploy when the task can be expressed through salient action points.

## Large VLA

Large VLAs use large language or vision-language model knowledge to improve generalization across tasks, environments, and robot embodiments. In the draft, this is the stage where VLA research most clearly aligns with robot foundation models.

## Summary Lens

The low-level policy section is a progression from feasibility to generality: first show that language and vision can control a robot, then unify modalities, enrich instructions, improve spatial grounding, model action distributions, add safety constraints, simplify execution, and finally scale toward broad robot generalization.
