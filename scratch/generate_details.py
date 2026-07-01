import os

details = {
    "hand_crafted_feature_engineering": {
        "title": "Hand-Crafted Feature Engineering",
        "description": "Traditional machine learning pipelines relied heavily on manual feature engineering. Domain experts designed mathematical extractors (like SIFT for contours or HOG for shapes) to capture specific patterns in data.",
        "mermaid": """graph TD
    RawData[Raw Data] -->|Manual Extraction| SIFT[SIFT / HOG / TF-IDF]
    SIFT -->|Static Vectors| Classifier[SVM / Linear Classifier]
    Classifier -->|Prediction| Output[Output Class]"""
    },
    "supervised_deep_hierarchical": {
        "title": "Supervised Deep Hierarchical Era",
        "description": "Deep Convolutional Networks and Recurrent Networks learn hierarchical representations natively through backpropagation on labeled datasets. Early layers capture basic features like edges, intermediate layers capture textures, and deep layers capture semantics.",
        "mermaid": """graph TD
    RawPixels[Raw Pixels] -->|Layer 1| Edges[Edges & Blobs]
    Edges -->|Layer 2| Textures[Textures & Shapes]
    Textures -->|Layer 3| Semantics[Object Parts]
    Semantics -->|Softmax| Class[Class Label]"""
    },
    "self_supervised_foundation": {
        "title": "Self-Supervised Foundation & Joint-Embedding",
        "description": "Self-Supervised Learning (SSL) utilizes raw, unlabeled data by creating artificial pretext tasks (like masking tokens or contrasting views) to train large foundation models.",
        "mermaid": """graph TD
    Data[Unlabeled Data] --> Pretext[Pretext Tasks]
    Pretext -->|Masking / Contrastive| Model[Foundation Model]
    Model -->|Fine-tuning| TaskA[Downstream Task A]
    Model -->|Zero-shot| TaskB[Downstream Task B]"""
    },
    "supervised_discriminative": {
        "title": "Supervised Discriminative Representation",
        "description": "Supervised discriminative representation maps input objects into distinct categories using softmax cross-entropy loss, pulling similar classes together and pushing dissimilar classes apart.",
        "mermaid": """graph LR
    Input[Input Image] --> CNN[Feature Extractor]
    CNN --> Latent[Latent Representation]
    Latent --> Classifier[Softmax Classifier]
    Classifier -->|Loss| CE[Cross-Entropy Loss]"""
    },
    "contrastive_joint_embedding": {
        "title": "Contrastive Joint-Embedding Representation (CLIP/SimCLR)",
        "description": "Formulates feature extraction as a multi-dimensional semantic alignment task. Using InfoNCE or Sigmoid loss, it maximizes similarity for positive pairs while repelling negative pairs.",
        "mermaid": """graph TD
    Image[Image View A] --> EncA[Encoder A] --> VecA[Vector A]
    ImagePrime[Image View B] --> EncB[Encoder B] --> VecB[Vector B]
    VecA & VecB -->|Dot Product| Sim[Maximize Similarity]
    VecA & Neg[Negative Samples] -->|InfoNCE| Diff[Minimize Similarity]"""
    },
    "predictive_autoencoding": {
        "title": "Predictive Autoencoding / Reconstruction (MAE/BERT)",
        "description": "Predictive autoencoding works by masking a portion of the input tokens or patches and training the model to reconstruct the missing details using surrounding contextual info.",
        "mermaid": """graph LR
    Input[Original Input] --> Mask[Masking Block 75%]
    Mask --> Visible[Visible Patches]
    Visible --> Encoder[Encoder]
    Encoder --> Latent[Latent Space]
    Latent --> Decoder[Decoder]
    Decoder --> Reconstruct[Reconstructed Input]"""
    },
    "information_maximization": {
        "title": "Information-Maximization (Non-Contrastive / VICReg)",
        "description": "Information-Maximization methods (like VICReg) bypass negative samples entirely and prevent representation collapse by regularizing variance and covariance of the embedding dimensions.",
        "mermaid": """graph TD
    InputA[View A] --> EncA[Encoder] --> ProjA[Projector]
    InputB[View B] --> EncB[Encoder] --> ProjB[Projector]
    ProjA & ProjB -->|Variance/Covariance Reg| Loss[VICReg Loss]
    Loss -->|Prevents| Collapse[Representation Collapse]"""
    },
    "continuous_latent_vector": {
        "title": "Continuous Latent Vector Spaces (Embeddings)",
        "description": "Projects inputs into a continuous high-dimensional vector space where semantic distance corresponds to mathematical distance measures like cosine similarity.",
        "mermaid": """graph LR
    Word1[King] --> Embed[Embedding Space] --> Vec1[Vector 1]
    Word2[Queen] --> Embed --> Vec2[Vector 2]
    Vec1 & Vec2 -->|Distance Metrics| Cosine[Cosine Similarity]"""
    },
    "discrete_codebook_quantization": {
        "title": "Discrete Codebook Quantization (VQGAN Class)",
        "description": "Snaps continuous latent vectors to their nearest neighbors inside a codebook matrix, producing discrete tokens that can be read sequentially like words.",
        "mermaid": """graph LR
    Encoder[Encoder Output] --> Quantize[Vector Quantizer]
    Codebook[Codebook Matrix] --> Quantize
    Quantize --> Index[Discrete Indices]
    Index --> Decoder[Decoder]"""
    },
    "monosemantic_feature_dictionaries": {
        "title": "Monosemantic Feature Dictionaries (Sparse Autoencoders)",
        "description": "Decomposes superposition-affected hidden states of transformers into sparse, overcomplete representations to isolate human-interpretable concepts.",
        "mermaid": """graph TD
    Dense[Dense Layer Activations] --> Encoder[Sparse Encoder]
    Encoder --> Sparse[Sparse Latent Features]
    Sparse --> Decoder[Reconstructed Activations]
    Sparse -->|Feature Extraction| Concepts[Concept Neurons]"""
    },
    "representation_collapse_trap": {
        "title": "The Representation Collapse Trap",
        "description": "A failure mode in self-supervised learning where the encoder maps all inputs to a constant vector to minimize the loss function.",
        "mermaid": """graph TD
    DifferentViews[Different Views of Input] --> Encoder[Collapsing Encoder]
    Encoder --> Constant[All Zeros / Constant Vector]
    Constant -->|Zero Info| Failed[Failed Representation]"""
    },
    "quadratic_visual_token_explosion": {
        "title": "The Quadratic Visual Token Explosion",
        "description": "Processing high-resolution visual inputs creates a massive token count, causing self-attention memory usage to scale quadratically O(N^2) and causing memory bottlenecks.",
        "mermaid": """graph LR
    Image[High Res Image] --> Patches[Thousands of Patches]
    Patches --> Attention[Attention Calculation]
    Attention -->|Quadratic Complexity| O_N2[O N^2 Memory Wall]"""
    },
    "pretraining_web_scale_multimodal": {
        "title": "Pre-Training Web-Scale Multi-Modal Foundation LLMs",
        "description": "Pre-training multi-modal foundation models on web-scale datasets enables them to learn cross-modal alignments, reasoning capabilities, and facts natively.",
        "mermaid": """graph TD
    WebData[Web-Scale Text, Images, Video] --> Pretrain[Autoregressive Pre-training]
    Pretrain --> Foundational[Foundation LLM]
    Foundational --> Alignment[Instruction Tuning & RLHF]"""
    },
    "realtime_cybersecurity_anomaly": {
        "title": "Real-Time Cyber-Security Anomaly & Fraud Detection Platforms",
        "description": "By learning the manifolds of normal transaction logs, deep autoencoders and contrastive models can detect anomalies and cybersecurity threats in real time.",
        "mermaid": """graph TD
    Logs[Transaction Logs] --> Autoencoder[Reconstruction Model]
    Autoencoder --> LowError[Low Error: Normal]
    Autoencoder --> HighError[High Error: Anomaly/Threat]"""
    },
    "denovo_bioinformatics": {
        "title": "De Novo Bio-Informatics & Genetic Structural Discovery",
        "description": "Self-supervised representation learning models map sequence details of DNA, RNA, and proteins to accelerate genetic structural discovery and target drug designs.",
        "mermaid": """graph TD
    Sequence[DNA/RNA/Protein Sequences] --> Model[AlphaFold / ESM]
    Model --> Latent[Structural Representations]
    Latent --> Output[3D Protein Folding / Drug Targets]"""
    }
}

os.makedirs("details", exist_ok=True)

for filename, data in details.items():
    content = f"""# {data['title']}

## Overview
{data['description']}

## Representation Flow / Architecture
```mermaid
{data['mermaid']}
```

---
[← Back to README](../README.md)
"""
    with open(f"details/{filename}.md", "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated details/{filename}.md")
