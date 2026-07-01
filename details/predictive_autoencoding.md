# Predictive Autoencoding / Reconstruction (MAE/BERT)

## Overview
Predictive autoencoding works by masking a portion of the input tokens or patches and training the model to reconstruct the missing details using surrounding contextual info.

## Representation Flow / Architecture
```mermaid
graph LR
    Input[Original Input] --> Mask[Masking Block 75%]
    Mask --> Visible[Visible Patches]
    Visible --> Encoder[Encoder]
    Encoder --> Latent[Latent Space]
    Latent --> Decoder[Decoder]
    Decoder --> Reconstruct[Reconstructed Input]
```

---
[← Back to README](../README.md)
