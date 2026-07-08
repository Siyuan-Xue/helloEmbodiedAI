---
title: "Embodied Interaction"
aliases:
  - "Embodied Interaction Notes"
tags:
  - paper-note
  - embodied-ai
  - interaction
source: "[[Aligning Cyber Space with Physical World--A Comprehensive Survey on Embodied AI|Embodied AI Survey Notes]]"
---

# Embodied Interaction

## Embodied Question Answering

Embodied Question Answering (EQA) methods include:

- Neural network methods
- LLM/VLM-based methods

Evaluation focuses on two dimensions: navigation and question answering.

Navigation metrics:

- Target endpoint distance \(d_T\)
- Distance change \(d_{\Delta}\)
- Minimum distance over the whole trajectory \(d_{\min}\)
- Trajectory length
- Target Intersection over Union (IoU)

Question-answering metrics:

- Mean Rank (MR)
- Answer accuracy
- LLM-Match as a newer large-model-based matching metric
- Path-length-normalized weighting for judging model efficiency

Current limitations:

- Dataset construction is costly.
- Large-scale datasets are scarce.
- Evaluation standards are inconsistent across datasets, making horizontal comparison difficult.
- Current large models perform far below humans.
- Future work needs better environment memory storage, action planning based on memory and questions, and more interpretable actions.

## Embodied Grasping

Gripper settings:

- 4 degrees of freedom: \(x\), \(y\), \(z\), and yaw around the z-axis
- 6 degrees of freedom

Spatial reasoning example:

> "grasp the keyboard that is to the right of the brown kleenex box"

Logical reasoning example:

> "I am thirsty, can you give me something to drink?"

Limitation:

Current embodied grasping methods require large amounts of data and generalize poorly to unknown objects. Future research should improve agent generalization and strengthen complex semantic understanding, unknown-object grasping, and fine-grained grasping.
