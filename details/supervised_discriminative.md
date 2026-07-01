# Supervised Discriminative Representation

## Overview
Supervised discriminative representation maps input objects into distinct categories using softmax cross-entropy loss, pulling similar classes together and pushing dissimilar classes apart.

## Representation Flow / Architecture
```mermaid
graph LR
    Input[Input Image] --> CNN[Feature Extractor]
    CNN --> Latent[Latent Representation]
    Latent --> Classifier[Softmax Classifier]
    Classifier -->|Loss| CE[Cross-Entropy Loss]
```

---
[← Back to README](../README.md)
