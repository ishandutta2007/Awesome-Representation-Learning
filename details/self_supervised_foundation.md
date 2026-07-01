# Self-Supervised Foundation & Joint-Embedding

## Overview
Self-Supervised Learning (SSL) utilizes raw, unlabeled data by creating artificial pretext tasks (like masking tokens or contrasting views) to train large foundation models.

## Representation Flow / Architecture
```mermaid
graph TD
    Data[Unlabeled Data] --> Pretext[Pretext Tasks]
    Pretext -->|Masking / Contrastive| Model[Foundation Model]
    Model -->|Fine-tuning| TaskA[Downstream Task A]
    Model -->|Zero-shot| TaskB[Downstream Task B]
```

---
[← Back to README](../README.md)
