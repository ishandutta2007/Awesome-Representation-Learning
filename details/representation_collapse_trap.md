# The Representation Collapse Trap

## Overview
A failure mode in self-supervised learning where the encoder maps all inputs to a constant vector to minimize the loss function.

## Representation Flow / Architecture
```mermaid
graph TD
    DifferentViews[Different Views of Input] --> Encoder[Collapsing Encoder]
    Encoder --> Constant[All Zeros / Constant Vector]
    Constant -->|Zero Info| Failed[Failed Representation]
```

---
[← Back to README](../README.md)
