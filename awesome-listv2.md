## AWESOME AI LIST

Explore open-source tools for building, training, optimizing, deploying, and evaluating AI systems—from foundational libraries to practical frameworks and examples.

#### Model Training & Optimization Utilities
- [Hugging Face Accelerate](https://github.com/huggingface/accelerate) - Simple API to make training scripts run on any hardware (multi-GPU, TPU, mixed precision) with minimal code changes.
- [einops](https://github.com/arogozhnikov/einops) - Tensor operations for readable reshaping, reduction, and composition across PyTorch, JAX, NumPy, MLX, and other array libraries.
- [Numba](https://github.com/numba/numba) - NumPy-aware JIT compiler that uses LLVM to accelerate numerical Python, including parallel and GPU-oriented workloads.
- [DeepSpeed](https://github.com/microsoft/DeepSpeed) - Microsoft's deep learning optimization library for extreme-scale training (ZeRO, offloading, MoE).

#### High-performance Serving & API Servers
- [vLLM](https://github.com/vllm-project/vllm) - State-of-the-art serving engine with PagedAttention and continuous batching.
- [Text Generation Inference (TGI)](https://github.com/huggingface/text-generation-inference) - Hugging Face's production-ready Rust-based server.
- [SGLang](https://github.com/sgl-project/sglang) - Next-gen serving framework with RadixAttention.
- [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) - NVIDIA's official high-performance inference backend.

#### ML Compilers & Kernel Tooling
- [Triton](https://github.com/triton-lang/triton) - Language and compiler for writing high-performance custom deep-learning primitives with a Python-based programming model.
- [XLA](https://github.com/openxla/xla) - Machine-learning compiler that optimizes models from frameworks such as PyTorch, TensorFlow, and JAX for CPUs, GPUs, and ML accelerators.
- [StableHLO](https://github.com/openxla/stablehlo) - Versioned ML operation set and portability layer connecting framework frontends with compilers such as XLA and IREE.

#### Quantization, Distillation & Optimization
- [GGUF](https://github.com/ggerganov/ggml) - Modern quantized format that powers most local inference.
- [bitsandbytes](https://github.com/bitsandbytes-foundation/bitsandbytes) - 8-bit and 4-bit optimizers + quantization.
- [TorchAO](https://github.com/pytorch/ao) - PyTorch-native model optimization library for quantization, sparsity, low-precision training, and efficient inference.

#### Full Training Frameworks
- [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) - One-stop unified framework for SFT, DPO, ORPO, KTO with web UI.
- [Axolotl](https://github.com/axolotl-ai-cloud/axolotl) - YAML-driven full pipeline for SFT, DPO, GRPO.
- [Unsloth](https://github.com/unslothai/unsloth) - 2× faster, 70% less memory fine-tuning.
- [LitGPT](https://github.com/Lightning-AI/litgpt) - Clean from-scratch implementations of 20+ LLMs.
- [torchtune](https://github.com/pytorch/torchtune) - PyTorch-native library for post-training, fine-tuning, and experimentation with LLMs.
- [TRL (Transformers Reinforcement Learning)](https://github.com/huggingface/trl) - Official library for RLHF, SFT, DPO, ORPO.
- [PyTorch Ignite](https://github.com/pytorch/ignite) - High-level PyTorch library for composing training and evaluation loops with engines, events, metrics, and reusable handlers.

#### Deployment & Orchestration
- [BentoML](https://github.com/bentoml/BentoML) - Unified framework to build, ship, and scale AI apps.
- [Ray Serve](https://github.com/ray-project/ray) - Scalable model serving library.
- [ZenML](https://github.com/zenml-io/zenml) - Pipeline and orchestration framework for taking ML and LLM systems from development to production.
- [Kubeflow](https://github.com/kubeflow/kubeflow) - Kubernetes-native ML/LLM platform.
- [KServe](https://github.com/kserve/kserve) - Kubernetes-based model serving.
- [Nebari Infrastructure Core (NIC)](https://github.com/nebari-dev/nebari-infrastructure-core) - Kubernetes platform infrastructure for AI/ML workflows using OpenTofu provisioning, Argo CD GitOps, and composable software packs.

#### Benchmark Suites
- [lm-evaluation-harness (EleutherAI)](https://github.com/EleutherAI/lm-evaluation-harness) - De-facto standard for generative model evaluation.
- [HELM (Stanford)](https://github.com/stanford-crfm/helm) - Holistic Evaluation of Language Models.
- [TritonBench](https://github.com/meta-pytorch/tritonbench) - Benchmark suite for measuring PyTorch operator performance with Triton and alternative kernel implementations.

#### Evaluation Frameworks
- [DeepEval](https://github.com/confident-ai/deepeval) - The "Pytest for LLMs".
- [RAGAs](https://github.com/explodinggradients/ragas) - End-to-end RAG evaluation framework.
- [Lighteval](https://github.com/huggingface/lighteval) - Evaluation toolkit for LLMs across multiple backends with reusable tasks, metrics, and result tracking.
- [Hugging Face Evaluate](https://github.com/huggingface/evaluate) - Standardized evaluation metrics.
- [CheckMAITE](https://github.com/openteams-ai/checkmaite) - Open-source toolkit for testing AI systems.

#### Starter Projects & Examples
- [PyTorch Examples](https://github.com/pytorch/examples) - Official tutorials: image classification, NLP, reinforcement learning.
- [TensorFlow Tutorials](https://www.tensorflow.org/tutorials) - Official guides for beginners to advanced users.
- [Hugging Face Transformers Notebooks](https://github.com/huggingface/notebooks) - Run Transformers, Datasets, and more in Colab.
- [Deep Learning Examples (NVIDIA)](https://github.com/NVIDIA/DeepLearningExamples) - Production-quality reference implementations.
- [Bonsai](https://github.com/jax-ml/bonsai) - Minimal, readable JAX implementations of popular vision and language models for experimentation and research.