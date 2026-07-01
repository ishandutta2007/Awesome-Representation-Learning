# Contrastive Joint-Embedding Representation (CLIP/SimCLR)

## Overview
Formulates feature extraction as a multi-dimensional semantic alignment task. Using InfoNCE or Sigmoid loss, it maximizes similarity for positive pairs while repelling negative pairs.

## Representation Flow / Architecture
```mermaid
graph TD
    Image[Image View A] --> EncA[Encoder A] --> VecA[Vector A]
    ImagePrime[Image View B] --> EncB[Encoder B] --> VecB[Vector B]
    VecA & VecB -->|Dot Product| Sim[Maximize Similarity]
    VecA & Neg[Negative Samples] -->|InfoNCE| Diff[Minimize Similarity]
```

---
[← Back to README](../README.md)
