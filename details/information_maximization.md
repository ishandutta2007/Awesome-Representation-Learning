# Information-Maximization (Non-Contrastive / VICReg)

## Overview
Information-Maximization methods (like VICReg) bypass negative samples entirely and prevent representation collapse by regularizing variance and covariance of the embedding dimensions.

## Representation Flow / Architecture
```mermaid
graph TD
    InputA[View A] --> EncA[Encoder] --> ProjA[Projector]
    InputB[View B] --> EncB[Encoder] --> ProjB[Projector]
    ProjA & ProjB -->|Variance/Covariance Reg| Loss[VICReg Loss]
    Loss -->|Prevents| Collapse[Representation Collapse]
```

---
[← Back to README](../README.md)
