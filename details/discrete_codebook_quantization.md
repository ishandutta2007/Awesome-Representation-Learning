# Discrete Codebook Quantization (VQGAN Class)

## Overview
Snaps continuous latent vectors to their nearest neighbors inside a codebook matrix, producing discrete tokens that can be read sequentially like words.

## Representation Flow / Architecture
```mermaid
graph LR
    Encoder[Encoder Output] --> Quantize[Vector Quantizer]
    Codebook[Codebook Matrix] --> Quantize
    Quantize --> Index[Discrete Indices]
    Index --> Decoder[Decoder]
```

---
[← Back to README](../README.md)
