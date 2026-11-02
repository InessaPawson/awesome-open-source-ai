# Awesome Open Source AI

A curated collection of open-source AI tools trusted by OpenTeams' engineering and research teams.

> **Editorial note:** Projects span research, development, and production. Inclusion does not imply a formal security audit or endorsement of every release. Verify license, maintenance status, dependencies, and security posture before adoption. Projects explicitly marked *not actively maintained* or *archived* are included for reference.

## Foundations

### Foundational Libraries & Frameworks

Core numerical, machine learning, and deep learning libraries used to build and experiment with AI systems.

- [NumPy](https://github.com/numpy/numpy) - Foundational array computing library for numerical Python and the scientific Python ecosystem.
- [SciPy](https://github.com/scipy/scipy) - Scientific computing algorithms for optimization, linear algebra, statistics, and signal processing.
- [PyTorch](https://github.com/pytorch/pytorch) - Tensor computing and deep learning framework with automatic differentiation and accelerator support.
- [JAX](https://github.com/jax-ml/jax) - Accelerator-oriented array computing and automatic differentiation with composable program transformations.
- [TensorFlow](https://github.com/tensorflow/tensorflow) - Machine learning framework for model development, training, and deployment.
- [scikit-learn](https://github.com/scikit-learn/scikit-learn) - Machine learning tools for classification, regression, clustering, preprocessing, and model selection.
- [Hugging Face Transformers](https://github.com/huggingface/transformers) - Pretrained model architectures, inference APIs, and training utilities for text, vision, audio, and multimodal models.
- [MLX](https://github.com/ml-explore/mlx) - Array framework for machine learning on Apple silicon.

## Build & Experiment

### Agentic Frameworks & Harnesses

Frameworks and runtime environments for building, orchestrating, executing, and managing autonomous AI agents across domains.

- [LangGraph](https://github.com/langchain-ai/langgraph) - Framework for stateful agent workflows with persistence, durable execution, and human-in-the-loop controls.
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) - Self-improving AI agent with persistent memory, autonomous skill creation, multi-model support, and cross-platform integrations.
- [CrewAI](https://github.com/crewAIInc/crewAI) - Framework for coordinating role-based agents and structured multi-agent workflows.
- [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) - Framework for developing agents and multi-agent workflows with orchestration and observability.
- [Google Agent Development Kit (ADK)](https://github.com/google/adk-python) - Code-first toolkit for building, testing, and deploying agents and multi-agent systems.
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - Lightweight agent framework with tools, handoffs, guardrails, and tracing.
- [Pydantic AI](https://github.com/pydantic/pydantic-ai) - Type-safe Python framework for model-agnostic agents and structured outputs.
- [smolagents](https://github.com/huggingface/smolagents) - Lightweight framework for agents that use tools and execute code.
- [Haystack](https://github.com/deepset-ai/haystack) - Modular framework for retrieval, agentic pipelines, and language-model applications.
- [Mastra](https://github.com/mastra-ai/mastra) - TypeScript framework for agents, workflows, memory, and evaluation; check component-level licensing.

### AI Coding Tools & Harnesses

Coding agents, IDE integrations, automated code review, debugging, testing, and autonomous software engineering workflows.

- [OpenHands](https://github.com/OpenHands/OpenHands) - Platform for coding agents that can inspect repositories, modify code, run commands, and test changes.
- [OpenCode](https://github.com/anomalyco/opencode) - Open-source coding agent for terminal-based development with configurable models.
- [Cline](https://github.com/cline/cline) - IDE-based coding agent with file editing, terminal access, and user approval of actions.
- [goose](https://github.com/block/goose) - Extensible agent for coding and automation with tool integrations, including MCP.
- [mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent/) - Research-oriented agent harness for resolving software repository issues.
- [Pi](https://github.com/badlogic/pi-mono) - Minimal, extensible terminal-based coding agent with multi-provider LLM support, customizable tools, and extensions.

### Interactive Computing

Notebook-centered tools and resources for exploratory computing, reproducible research, and AI-assisted development.

- [Awesome Jupyter AI](https://github.com/openteams-ai/awesome-jupyter-ai) - Curated collection of AI integrations for JupyterLab and Jupyter Notebook, including coding assistants and notebook automation.
- [Jupyter AI](https://github.com/jupyterlab/jupyter-ai) - AI-assisted notebook workflows and conversational interfaces in JupyterLab.
- [marimo](https://github.com/marimo-team/marimo) - Reactive Python notebooks designed for reproducible, executable applications and experiments.

## Train & Optimize

### Model Training & Fine-Tuning Frameworks

Frameworks and recipes for pretraining, instruction tuning, alignment, and post-training experimentation.

- [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) - Unified framework and web UI for fine-tuning and aligning language models with multiple training methods.
- [Axolotl](https://github.com/axolotl-ai-cloud/axolotl) - Configuration-driven framework for language-model fine-tuning and preference optimization.
- [Unsloth](https://github.com/unslothai/unsloth) - Optimized model fine-tuning tools designed to reduce memory use and training overhead.
- [LitGPT](https://github.com/Lightning-AI/litgpt) - Readable language-model implementations and recipes for training and fine-tuning.
- [TRL (Transformer Reinforcement Learning)](https://github.com/huggingface/trl) - Hugging Face toolkit for supervised fine-tuning, preference optimization, and reinforcement-learning-based post-training.
- [PyTorch Ignite](https://github.com/pytorch/ignite) - Composable training and evaluation loops with events, metrics, and handlers.
- [torchtune](https://github.com/meta-pytorch/torchtune) - PyTorch-native post-training recipes and experimentation library; **not actively maintained** (development wound down in 2025).

### Model Training & Optimization Utilities

Tools for efficient training, tensor operations, hardware portability, and numerical acceleration.

- [Hugging Face Accelerate](https://github.com/huggingface/accelerate) - Simplifies distributed and mixed-precision training across supported hardware.
- [einops](https://github.com/arogozhnikov/einops) - Readable tensor rearrangement, reduction, and composition across array frameworks.
- [Numba](https://github.com/numba/numba) - LLVM-based JIT compiler for accelerating numerical Python workloads.
- [DeepSpeed](https://github.com/microsoft/DeepSpeed) - Distributed deep learning optimization with techniques such as ZeRO and offloading.

### ML Compilers & Kernel Tooling

Compilers, intermediate representations, and programming models for efficient machine-learning execution.

- [Triton](https://github.com/triton-lang/triton) - Language and compiler for writing high-performance custom GPU kernels using a Python-based programming model.
- [XLA](https://github.com/openxla/xla) - Compiler that optimizes machine learning computations for CPUs, GPUs, and accelerators.
- [StableHLO](https://github.com/openxla/stablehlo) - Portable, versioned operation set connecting machine-learning frontends with compiler backends.
- [IREE](https://github.com/iree-org/iree) - MLIR-based compiler and runtime for deploying machine learning workloads across heterogeneous hardware.

### Model Compression & Optimization

Tools and formats for quantization, low-precision execution, pruning, and efficient model deployment.

- [GGML / GGUF](https://github.com/ggml-org/ggml) - Tensor library and associated model serialization format commonly used for efficient local inference.
- [bitsandbytes](https://github.com/bitsandbytes-foundation/bitsandbytes) - Low-bit quantization and memory-efficient optimizer implementations.
- [TorchAO](https://github.com/pytorch/ao) - PyTorch model optimization library for quantization, sparsity, and low-precision execution.
- [GPTQModel](https://github.com/ModelCloud/GPTQModel) - Post-training quantization tooling for efficient language-model inference.

## Serve & Deploy

### Model Inference & Serving

Engines and servers for efficient model inference, batching, and production APIs.

- [vLLM](https://github.com/vllm-project/vllm) - High-throughput language-model inference and serving with efficient attention and request scheduling.
- [SGLang](https://github.com/sgl-project/sglang) - High-performance inference and serving framework with optimized scheduling and attention mechanisms.
- [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) - NVIDIA toolkit for optimized large-language-model inference on supported GPUs.
- [llama.cpp](https://github.com/ggml-org/llama.cpp) - Efficient local and server-side inference for language models on a wide range of hardware.
- [Text Generation Inference (TGI)](https://github.com/huggingface/text-generation-inference) - Hugging Face text-generation server; **archived on March 21, 2026** and retained for reference.

### ML Infrastructure & Deployment

Platforms and orchestration tools for packaging, deploying, serving, and operating AI and ML applications.

- [BentoML](https://github.com/bentoml/BentoML) - Framework for packaging, deploying, and scaling AI inference services.
- [Ray Serve](https://github.com/ray-project/ray) - Scalable model serving library built on Ray.
- [ZenML](https://github.com/zenml-io/zenml) - ML pipeline orchestration for moving experimental workflows into production.
- [Kubeflow](kubeflow.org) - Kubernetes-native machine learning platform and ecosystem.
- [KServe](https://github.com/kserve/kserve) - Kubernetes-based inference serving platform.
- [Nebari Infrastructure Core (NIC)](https://github.com/nebari-dev/nebari-infrastructure-core) - Composable Kubernetes infrastructure for AI/ML workflows using OpenTofu and GitOps tooling.

## Secure & Verify

### Cybersecurity for AI

Tools for assessing and securing models, agents, data pipelines, and AI applications against adversarial inputs, prompt injection, and unsafe artifacts.

- [garak](https://github.com/NVIDIA/garak) - Vulnerability scanner for language models, probing risks such as prompt injection and information leakage.
- [PyRIT](https://github.com/Azure/PyRIT) - Microsoft framework for automating AI red-teaming and risk identification.
- [Adversarial Robustness Toolbox (ART)](https://github.com/Trusted-AI/adversarial-robustness-toolbox) - Tools to evaluate and improve machine-learning robustness against adversarial attacks.
- [ModelScan](https://github.com/protectai/modelscan) - Scans serialized machine-learning model files for potentially unsafe content.
- [LLM Guard](https://github.com/protectai/llm-guard) - Input and output scanning toolkit for LLM applications, including sensitive-data and prompt-injection checks.
- [Giskard](https://github.com/Giskard-AI/giskard) - Testing and vulnerability assessment tools for machine learning and LLM applications.

### Verification & Assurance for AI Systems

Formal methods applied to AI: checking properties of neural networks, verifying the protocols and infrastructure that agents and serving systems run on, and using language models to generate and check machine-verified proofs. Guarantees apply to specified properties under stated assumptions, not to arbitrary model behavior.

- [Marabou](https://github.com/NeuralNetworkVerification/Marabou) - Neural-network verification framework for proving robustness, safety, and reachability properties of trained networks.
- [auto_LiRPA](https://github.com/Verified-Intelligence/auto_LiRPA) - Automatic bound propagation for certified robustness and scalable neural-network verification; core of the α,β-CROWN verifier.
- [Lean 4](https://github.com/leanprover/lean4) - Interactive theorem prover and programming language; the standard target for LLM-based proof generation, autoformalization, and AI-for-mathematics research.
- [TLA+ Tools](https://github.com/tlaplus/tlaplus) - Specification language and model checker for concurrent and distributed systems, including agent orchestration, tool-calling protocols, and inference-serving infrastructure.
- [Z3](https://github.com/Z3Prover/z3) - SMT solver underlying many neural-network and program verifiers; also used to check constraints on LLM-generated code and structured outputs.
- [Dafny](https://github.com/dafny-lang/dafny) - Verification-aware language used to prove correctness of code, including code produced by AI coding agents, against explicit specifications.
- [Verus](https://github.com/verus-lang/verus) - Rust verification framework for proving memory-safety and functional-correctness properties of systems code such as runtimes and inference engines.

## Evaluate & Learn

### Evaluation Frameworks

Tools for validating model quality, retrieval quality, AI application behavior, and regression risks.

- [DeepEval](https://github.com/confident-ai/deepeval) - Pytest-style framework for evaluating LLM applications and agents.
- [Ragas](https://github.com/explodinggradients/ragas) - Evaluation framework for RAG and other LLM application workflows.
- [Lighteval](https://github.com/huggingface/lighteval) - Language-model evaluation toolkit supporting tasks, metrics, and multiple backends.
- [CheckMAITE](https://github.com/openteams-ai/checkmaite) - Open-source toolkit for testing and evaluating AI systems.

### Benchmark Suites

Standardized tasks and suites for comparing model capabilities and systems performance.

- [lm-evaluation-harness (EleutherAI)](https://github.com/EleutherAI/lm-evaluation-harness) - Framework and task collection for reproducible language-model benchmarking.
- [HELM (Stanford)](https://github.com/stanford-crfm/helm) - Holistic evaluation framework and benchmark suite for foundation models.
- [TritonBench](https://github.com/meta-pytorch/tritonbench) - Benchmarks for PyTorch operators and Triton kernel performance.
- [SWE-bench](https://github.com/SWE-bench/SWE-bench) - Benchmark for evaluating agents on real-world software engineering issues.

### Starter Projects & Examples

Tutorials and approachable examples for learning, experimentation, and reference implementations.

- [PyTorch Examples](https://github.com/pytorch/examples) - Official examples covering image classification, NLP, and reinforcement learning.
- [TensorFlow Tutorials](https://github.com/tensorflow/docs) - Tutorials spanning introductory and advanced machine learning workflows.
- [Hugging Face Transformers Notebooks](https://github.com/huggingface/notebooks) - Interactive examples for Transformers, Datasets, and related libraries.
- [Deep Learning Examples (NVIDIA)](https://github.com/NVIDIA/DeepLearningExamples) - Reference implementations for deep learning training and inference.
- [Bonsai](https://github.com/jax-ml/bonsai) - Minimal JAX implementations of vision and language models for education and research.

---

## Contributing and Curation Notes

When suggesting a project, provide its repository, a concise explanation of its role, and the reason it belongs in the proposed category. Reviewers should consider:

- **Open-source licensing:** Check that the relevant project components have an OSI-approved license and distinguish community code from separately licensed add-ons.
- **Maintenance:** Check recent releases, contributions, security reporting, and deprecation notices; label archived or inactive projects.
- **Practical relevance:** Prefer projects that engineering and research teams have used, evaluated, or can explain with credible evidence.
- **Security:** Consider dependency hygiene, release integrity, tool permissions, data handling, and model/agent trust boundaries.
- **Categorization:** Choose the primary use case; projects may span categories, but avoid duplicate entries unless they serve distinct purposes.

