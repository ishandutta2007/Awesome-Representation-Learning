# Monosemantic Feature Dictionaries (Sparse Autoencoders)

## Overview
Decomposes superposition-affected hidden states of transformers into sparse, overcomplete representations to isolate human-interpretable concepts.

## Representation Flow / Architecture
```mermaid
graph TD
    Dense[Dense Layer Activations] --> Encoder[Sparse Encoder]
    Encoder --> Sparse[Sparse Latent Features]
    Sparse --> Decoder[Reconstructed Activations]
    Sparse -->|Feature Extraction| Concepts[Concept Neurons]
```

---
[← Back to README](../README.md)
