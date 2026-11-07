# Awesome Open Source AI

A bundled offline subset of the OpenTeams catalog. The app loads the full upstream README when online.

## Foundations
### Foundational Libraries & Frameworks
- [NumPy](https://github.com/numpy/numpy) - Foundational array computing library for numerical Python and the scientific Python ecosystem.
- [SciPy](https://github.com/scipy/scipy) - Scientific computing algorithms for optimization, linear algebra, statistics, and signal processing.
- [PyTorch](https://github.com/pytorch/pytorch) - Tensor computing and deep learning framework with automatic differentiation and accelerator support.
- [JAX](https://github.com/jax-ml/jax) - Accelerator-oriented array computing and automatic differentiation.
- [TensorFlow](https://github.com/tensorflow/tensorflow) - Machine learning framework for model development, training, and deployment.
- [scikit-learn](https://github.com/scikit-learn/scikit-learn) - Machine learning tools for classification, regression, clustering and preprocessing.
- [Hugging Face Transformers](https://github.com/huggingface/transformers) - Pretrained architectures and training utilities for text, vision, audio and multimodal models.
- [MLX](https://github.com/ml-explore/mlx) - Array framework for machine learning on Apple silicon.

## Build & Experiment
### Agentic Frameworks & Harnesses
- [LangGraph](https://github.com/langchain-ai/langgraph) - Framework for stateful agent workflows with persistence and human-in-the-loop controls.
- [Hermes Agent](https://github.com/NousResearch/hermes-agent) - AI agent with persistent memory and skill creation.
- [CrewAI](https://github.com/crewAIInc/crewAI) - Framework for coordinating role-based agents and structured multi-agent workflows.
- [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) - Framework for developing agents and multi-agent workflows.
- [Google Agent Development Kit](https://github.com/google/adk-python) - Code-first toolkit for building, testing and deploying multi-agent systems.
- [OpenAI Agents SDK](https://github.com/openai/openai-agents-python) - Agent framework with tools, handoffs, guardrails and tracing.
- [Pydantic AI](https://github.com/pydantic/pydantic-ai) - Type-safe Python framework for model-agnostic agents.
- [smolagents](https://github.com/huggingface/smolagents) - Lightweight tool-using agents that execute code.
- [Haystack](https://github.com/deepset-ai/haystack) - Modular RAG and agent pipelines.
- [Mastra](https://github.com/mastra-ai/mastra) - TypeScript framework for agents, workflows, memory and evaluation.
### AI Coding Tools & Harnesses
- [OpenHands](https://github.com/All-Hands-AI/OpenHands) - Platform for coding agents that modify code and run tests.
- [OpenCode](https://github.com/anomalyco/opencode) - Open-source terminal coding agent.
- [Cline](https://github.com/cline/cline) - IDE-based coding agent with terminal and file editing.
- [goose](https://github.com/block/goose) - Extensible coding agent with MCP integrations.
- [mini-swe-agent](https://github.com/SWE-agent/mini-swe-agent) - Research harness for resolving GitHub issues.
- [Pi](https://github.com/badlogic/pi-mono) - Extensible terminal-based coding agent.
### Interactive Computing
- [Awesome Jupyter AI](https://github.com/openteams-ai/awesome-jupyter-ai) - Curated AI integrations for JupyterLab and Jupyter Notebook.
- [Jupyter AI](https://github.com/jupyterlab/jupyter-ai) - AI-assisted notebook workflows and conversational JupyterLab interfaces.
- [marimo](https://github.com/marimo-team/marimo) - Reactive reproducible Python notebooks.

## Train & Optimize
### Model Training & Fine-Tuning Frameworks
- [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) - Language model fine-tuning and alignment framework.
- [Axolotl](https://github.com/axolotl-ai-cloud/axolotl) - Configuration-driven language-model fine-tuning.
- [Unsloth](https://github.com/unslothai/unsloth) - Memory-efficient model fine-tuning.
- [LitGPT](https://github.com/Lightning-AI/litgpt) - Language-model training recipes.
- [TRL](https://github.com/huggingface/trl) - Toolkit for supervised fine-tuning and preference optimization.
- [PyTorch Ignite](https://github.com/pytorch/ignite) - Composable training loops, metrics and handlers.
- [torchtune](https://github.com/pytorch/torchtune) - PyTorch post-training recipes; not actively maintained.
### Model Training & Optimization Utilities
- [Hugging Face Accelerate](https://github.com/huggingface/accelerate) - Distributed and mixed-precision training.
- [einops](https://github.com/arogozhnikov/einops) - Readable tensor rearrangement and reduction.
- [Numba](https://github.com/numba/numba) - LLVM-based JIT compiler for numerical Python.
- [DeepSpeed](https://github.com/deepspeedai/DeepSpeed) - Distributed deep-learning optimization and offloading.
### ML Compilers & Kernel Tooling
- [Triton](https://github.com/triton-lang/triton) - Language and compiler for high-performance GPU kernels.
- [XLA](https://github.com/openxla/xla) - Machine-learning compiler for CPUs, GPUs and accelerators.
- [StableHLO](https://github.com/openxla/stablehlo) - Portable operation set connecting ML frontends and compilers.
- [IREE](https://github.com/iree-org/iree) - MLIR compiler and runtime for heterogeneous hardware.
### Model Compression & Optimization
- [GGML](https://github.com/ggml-org/ggml) - Tensor library for efficient local inference.
- [bitsandbytes](https://github.com/bitsandbytes-foundation/bitsandbytes) - Low-bit quantization and memory-efficient optimizers.
- [TorchAO](https://github.com/pytorch/ao) - PyTorch quantization and low-precision execution.
- [GPTQModel](https://github.com/ModelCloud/GPTQModel) - Post-training quantization for language models.

## Serve & Deploy
### Model Inference & Serving
- [vLLM](https://github.com/vllm-project/vllm) - High-throughput LLM serving.
- [SGLang](https://github.com/sgl-project/sglang) - High-performance inference and serving.
- [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) - NVIDIA optimized LLM inference.
- [llama.cpp](https://github.com/ggml-org/llama.cpp) - Efficient local and server-side language-model inference.
- [Text Generation Inference](https://github.com/huggingface/text-generation-inference) - Text-generation serving; archived in 2026.
### ML Infrastructure & Deployment
- [BentoML](https://github.com/bentoml/BentoML) - Packaging and deployment of AI inference services.
- [Ray Serve](https://github.com/ray-project/ray) - Scalable model serving built on Ray.
- [ZenML](https://github.com/zenml-io/zenml) - ML pipeline orchestration.
- [Kubeflow](https://github.com/kubeflow/kubeflow) - Kubernetes-native machine-learning platform.
- [KServe](https://github.com/kserve/kserve) - Kubernetes-based inference serving.
- [Nebari Infrastructure Core](https://github.com/nebari-dev) - Composable infrastructure for AI/ML workflows.

## Secure & Verify
### Cybersecurity for AI
- [garak](https://github.com/NVIDIA/garak) - Vulnerability scanner for language models.
- [PyRIT](https://github.com/Azure/PyRIT) - AI red-teaming and risk identification framework.
- [Adversarial Robustness Toolbox](https://github.com/Trusted-AI/adversarial-robustness-toolbox) - Adversarial robustness evaluation.
- [ModelScan](https://github.com/protectai/modelscan) - Scanning serialized ML model files.
- [LLM Guard](https://github.com/protectai/llm-guard) - Input and output scanning for LLM applications.
- [Giskard](https://github.com/Giskard-AI/giskard) - ML and LLM testing and vulnerability assessment.
### Verification & Assurance for AI Systems
- [Marabou](https://github.com/NeuralNetworkVerification/Marabou) - Neural network verification.
- [auto_LiRPA](https://github.com/Verified-Intelligence/auto_LiRPA) - Bound propagation and certified robustness.
- [Lean 4](https://github.com/leanprover/lean4) - Interactive theorem prover.
- [TLA+ Tools](https://github.com/tlaplus/tlaplus) - Formal specification and model checking.
- [Z3](https://github.com/Z3Prover/z3) - SMT solver for verification and constraint solving.
- [Dafny](https://github.com/dafny-lang/dafny) - Verification-aware programming language.
- [Verus](https://github.com/verus-lang/verus) - Rust program verification framework.

## Evaluate & Learn
### Evaluation Frameworks
- [DeepEval](https://github.com/confident-ai/deepeval) - Pytest-style LLM evaluation framework.
- [Ragas](https://github.com/explodinggradients/ragas) - RAG evaluation framework.
- [Lighteval](https://github.com/huggingface/lighteval) - Language-model evaluation toolkit.
- [CheckMAITE](https://github.com/mit-ll-ai-technology/checkmaite) - AI testing and evaluation toolkit.
### Benchmark Suites
- [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) - Reproducible language-model benchmarking.
- [HELM](https://github.com/stanford-crfm/helm) - Holistic foundation-model evaluation.
- [TritonBench](https://github.com/thunlp/TritonBench) - GPU kernel performance benchmarks.
- [SWE-bench](https://github.com/SWE-bench/SWE-bench) - Benchmark for software engineering agents.
### Starter Projects & Examples
- [PyTorch Examples](https://github.com/pytorch/examples) - Deep learning examples.
- [TensorFlow Tutorials](https://github.com/tensorflow/docs) - TensorFlow tutorials.
- [Hugging Face Transformers Notebooks](https://github.com/huggingface/notebooks) - Interactive Transformers examples.
- [Deep Learning Examples](https://github.com/NVIDIA/DeepLearningExamples) - Training and inference examples.
- [Bonsai](https://github.com/RobertTLange/bonsai) - Minimal JAX model implementations for teaching.
