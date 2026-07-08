---
title: "Embodied Perception"
aliases:
  - "Embodied Perception Notes"
tags:
  - paper-note
  - embodied-ai
  - perception
  - vln
source: "[[Aligning Cyber Space with Physical World — Embodied AI Survey|Embodied AI Survey Notes]]"
---

# Embodied Perception

The future of visual perception is embodied-centric visual reasoning and social intelligence.

## Active Visual Perception

Active visual perception requires three fundamental capabilities:

- State estimation
- Scene perception
- Environment exploration

### Visual Simultaneous Localisation and Mapping

> [!summary] Core comparison
> Traditional geometric SLAM knows where coordinate points are in space, but not what those points represent. Semantic vSLAM packages point clouds into labelled objects, so robots can understand the environment and use that understanding for embodied interaction tasks such as grasping and navigation.

Point clouds in low-level maps do not correspond directly to objects in the environment, so embodied robots cannot easily understand or use them. Semantic vSLAM systems combine semantic information with mapping and significantly enhance a robot's ability to perceive unexplored environments.

### 3D Scene Understanding

3D scene understanding distinguishes object semantics, identifies object locations, and infers geometric attributes from 3D scene data. This is fundamental for autonomous driving, robot navigation, and human-computer interaction.

### Active Exploration

Active exploration means interacting with the environment and changing the viewing direction to obtain more visual information.

## 3D Visual Grounding

Unlike traditional 2D Visual Grounding (VG), which operates on flat images, 3D Visual Grounding incorporates depth, perspective, and spatial relationships between objects. This provides a stronger framework for agents that need to interact with their environments.

### Two-Stage 3D Visual Grounding

Limitations:

- The process is split into detection and matching, so the detection stage recognizes objects without using language semantics.
- There are many candidate boxes, making it easy to confuse visually similar furniture or objects.
- The computation cost is high and inference is slow.

### One-Stage 3D Visual Grounding

Compared with two-stage methods, one-stage 3D VG integrates object detection and language-guided feature extraction. This makes it easier to locate objects relevant to the language query.

### Fine-Grained Language Alignment

Both two-stage and one-stage methods have a common weakness: they often extract sentence-level fused features or focus mainly on object nouns. These strategies can lose word-level fine-grained information and ignore attribute modifiers.

EDA addresses this issue by explicitly decoupling textual attributes and building dense alignment between fine-grained language units and point-cloud objects.

The process:

1. Split a long text instruction into five independent semantic units: target object, auxiliary reference object, attribute modifier, pronoun, and spatial relation.
2. Use dense alignment to bind object-related semantic units to 3D visual features.

## Visual-Language Navigation

Visual-Language Navigation (VLN) aims to enable agents to navigate unseen environments by following linguistic instructions.

Inputs:

- Visual information, such as a video of past trajectories or a set of historical and current observation images
- Natural language instructions, including the target the embodied agent should reach or the task it should complete

Action selection can be represented as:

$$
\text{Action} = M(O, H, I)
$$

where \(O\) is the current observation, \(H\) is historical information, and \(I\) is the natural language instruction.

Common metrics:

- Success Rate (SR): directly reflects navigation performance.
- Trajectory Length (TL): reflects navigation efficiency.
- Success Weighted by Path Length (SPL): combines success and path efficiency.

$$
\mathrm{SPL} = \frac{1}{N}\sum_{i=1}^{N} I_i \cdot \frac{L_i}{\max(P_i, L_i)}
$$

where \(I_i\) is the success indicator, \(L_i\) is the shortest-path length, and \(P_i\) is the actual trajectory length.

Dataset notes:

- Natural language instructions may be detailed action descriptions, a fully described goal, a roughly described task, or only a human demand.
- The required task may be single navigation, navigation with interaction, or multiple navigation tasks completed in sequence.

Method notes:

- Memory-understanding-based methods often use graph-based learning to understand and encode the environment. They use historical memory, such as maps and previously observed objects, to localize the robot and compensate for insufficient current visual information.
- Future-prediction-based methods simulate unobserved areas in advance, helping agents avoid collisions and dead ends and improving active exploration.

Long-distance navigation is difficult because robots may revisit repeated areas or lose sight of the target. Memory is stable for already observed regions, while prediction is more useful for unseen regions.

## Non-Visual Perception: Tactile

Touch enables robots to acquire information such as material, shape, temperature, contact force, and gravity.

Current work focuses on three areas:

- Sensor design
- Dataset construction
- Applications

Sensor design categories:

- Non-vision-based sensors
- Vision-based sensors
- Multi-modal sensors

Dataset notes:

- Non-vision sensor datasets contain electrode values, 3D net force vectors, and contact locations. Their samples are usually force samples and grasping samples.
- Vision-based sensors use high-resolution deformation-gel images. Beyond estimating force and sliding, they focus more on texture classification and 3D reconstruction.
- Dataset objects usually include household objects, wildlife environments, different materials, and grasping items.

Methods:

1. Robotic manipulation: RL/GAN-based methods
2. Classification and recognition: traditional methods, LLM-based methods, and VLM-based methods

Main difficulties:

- Each type of tactile sensor has its own limitations.
- Tactile multi-modal data are difficult to collect.
- There is no unified hardware or software standard.
- Data heterogeneity and domain gaps limit large-scale training and deployment.
