"""Deterministic, catalog-grounded architecture planning for OpenTeams AI Compass.

These plans are educational starting points, not integration or security certifications.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable
import json

from catalog import Project


@dataclass(frozen=True)
class Stage:
    id: str
    title: str
    description: str
    why: str
    repo_urls: tuple[str, ...]
    optional: bool = False


@dataclass(frozen=True)
class Recipe:
    title: str
    pitch: str
    stages: tuple[Stage, ...]
    gaps: tuple[str, ...]
    tests: tuple[str, ...]


def stage(id: str, title: str, description: str, why: str, *repos: str, optional: bool = False) -> Stage:
    return Stage(id, title, description, why, tuple(f"https://github.com/{r}" for r in repos), optional)


RECIPES: dict[str, Recipe] = {
    "Local private assistant": Recipe(
        "Local private assistant",
        "Prototype a local-first assistant with a small operational footprint.",
        (
            stage("foundation", "Application utilities", "Local numerical or model data utilities", "Support lightweight local processing", "numpy/numpy", "huggingface/transformers"),
            stage("interface", "Interactive development", "Prototype prompts and interactions in a notebook", "Iterate quickly before building an end-user interface", "marimo-team/marimo", "jupyterlab/jupyter-ai"),
            stage("inference", "Local inference", "Run quantized models on local hardware", "Keep inference under local operational control", "ggml-org/llama.cpp"),
            stage("security", "Local safety checks", "Screen unsafe content and test vulnerabilities", "Reduce accidental unsafe responses", "protectai/llm-guard", "NVIDIA/garak"),
            stage("evaluation", "Quality checks", "Test expected question-answer scenarios", "Check quality on actual target hardware", "confident-ai/deepeval", "EleutherAI/lm-evaluation-harness"),
            stage("deployment", "Optional local packaging", "Package the prototype as a service", "Support repeatable local installs", "bentoml/BentoML", optional=True),
        ),
        ("Select and verify a compatible model, weights and local hardware requirements.", "Local operation does not automatically guarantee privacy: review logging, telemetry and external calls.", "Build the end-user chat interface separately; the notebook tools above are for prototyping.", "Package storage, backups and operating-system permissions separately."),
        ("Verify network traffic remains within the intended boundary.", "Benchmark latency and memory on target devices.", "Verify safety rules and input handling work offline."),
    ),
    "Tool-using AI agent": Recipe(
        "Tool-using AI agent",
        "Design a supervised agent that can call tools, produce structured results and recover from failures.",
        (
            stage("foundation", "Core model utilities", "Model interfaces and tensor processing", "Provide model integration building blocks", "huggingface/transformers", "pytorch/pytorch"),
            stage("orchestration", "Agent orchestration", "Implement tool calls, state and approvals", "Control multi-step tasks with human review", "langchain-ai/langgraph", "pydantic/pydantic-ai", "crewAIInc/crewAI"),
            stage("inference", "Model inference", "Host the language model", "Separate agent logic from serving", "vllm-project/vllm", "ggml-org/llama.cpp"),
            stage("security", "Adversarial testing", "Probe prompts for jailbreaks, injection and leakage", "Find risky model behavior before tools are attached", "Azure/PyRIT", "NVIDIA/garak"),
            stage("evaluation", "Agent evaluations", "Test task success and failure recovery", "Measure useful behavior against a scenario suite", "confident-ai/deepeval"),
            stage("deployment", "Serving", "Deploy the API or workflow service", "Expose the agent with operational controls", "bentoml/BentoML", "ray-project/ray"),
        ),
        ("Design actual tool connectors and schemas; integrations are not guaranteed by this list.", "Define permissions, human approvals and audit logs for sensitive actions.", "Prompt red-teaming tools do not exercise tool permissions; test tool misuse with your own scenario suite.", "Select an actual model, hosting, identity provider and secrets store."),
        ("Test a no-access tool call and ensure it fails safely.", "Test tool timeout, malformed output and partial execution recovery.", "Review prompts and tools for injection and privilege escalation.", "Set human approval checkpoints for consequential actions."),
    ),
    "Autonomous coding agent for a repository": Recipe(
        "Autonomous coding agent for a repository",
        "Set up a coding agent that works inside a sandboxed repository with review gates and measurable task success.",
        (
            stage("foundation", "Model utilities", "Model interfaces for the agent's language model", "Provide model integration building blocks", "huggingface/transformers"),
            stage("harness", "Coding agent harness", "Choose an agent that edits code, runs commands and opens changes", "Start from a maintained harness rather than a custom loop", "All-Hands-AI/OpenHands", "block/goose", "cline/cline", "anomalyco/opencode"),
            stage("reference", "Minimal reference agent", "Study a small, readable agent loop", "Understand what the larger harnesses automate", "SWE-agent/mini-swe-agent", optional=True),
            stage("inference", "Model inference", "Host the model the agent calls", "Separate agent logic from serving", "vllm-project/vllm", "ggml-org/llama.cpp"),
            stage("security", "Input screening and probing", "Screen repository content and probe for injection", "Untrusted files in the repo are prompts to the agent", "protectai/llm-guard", "NVIDIA/garak"),
            stage("evaluation", "Task-success evaluation", "Measure resolved issues on a benchmark", "Compare harnesses and models on real repository tasks", "SWE-bench/SWE-bench"),
            stage("deployment", "Parallel runs", "Run many agent sessions concurrently", "Scale evaluations or batch tasks", "ray-project/ray", optional=True),
        ),
        ("Sandboxing, repository permissions and secret isolation are not provided by this catalog; design them first.", "CI integration and branch protection rules are external to the agent.", "Select an actual model and confirm its license allows code generation for your use."),
        ("Verify the agent cannot push to protected branches or read secrets outside its scope.", "Confirm untrusted file content cannot change tool calls or targets.", "Measure resolved-task rate against a held-out issue set.", "Require human review on every change before merge."),
    ),
    "Fine-tune and serve a model": Recipe(
        "Fine-tune and serve a model",
        "Plan a model adaptation pipeline with training, optimization, serving and quality gates.",
        (
            stage("foundation", "Training framework", "Select your deep learning base", "Provide model and tensor operations", "pytorch/pytorch", "huggingface/transformers"),
            stage("training", "Fine-tuning", "Train or adapt a pretrained model", "Use a reproducible training recipe", "hiyouga/LLaMA-Factory", "unslothai/unsloth", "huggingface/trl"),
            stage("optimization", "Optimize", "Quantize for training memory or for target hardware", "Reduce memory during training and improve serving throughput", "pytorch/ao", "ModelCloud/GPTQModel", "bitsandbytes-foundation/bitsandbytes"),
            stage("inference", "Serve", "Deploy model inference", "Make the model usable via an endpoint", "vllm-project/vllm", "sgl-project/sglang"),
            stage("security", "Scan and red-team", "Test model files and unsafe behavior", "Find risks before release", "protectai/modelscan", "NVIDIA/garak"),
            stage("evaluation", "Benchmark and evaluate", "Test regressions and task performance", "Measure adaptation results against baseline", "EleutherAI/lm-evaluation-harness", "huggingface/lighteval"),
            stage("deployment", "Production packaging", "Deploy models with repeatable infrastructure", "Manage rollouts and scaling", "bentoml/BentoML", "kserve/kserve"),
        ),
        ("Training data governance, provenance and labeling are not defined by this catalog.", "Confirm model licenses and rights to train and distribute resulting weights.", "Add artifact registry, observability, GPU provisioning, rollback and incident response."),
        ("Compare quality against the base model on a held-out dataset.", "Review training data for private or restricted material.", "Scan artifacts and track software/model provenance.", "Run throughput, memory and rollback tests."),
    ),
    "Document Q&A (RAG)": Recipe(
        "Document Q&A (RAG)",
        "Build a document question-answering service with retrieval, model inference, evaluation and guardrails.",
        (
            stage("foundation", "Application foundation", "Numerical and model utilities", "Support data and model processing", "numpy/numpy", "huggingface/transformers"),
            stage("pipeline", "Retrieval and orchestration", "Index documents, retrieve relevant passages and orchestrate the prompt flow", "Connect documents to prompts; an orchestrator still needs a retriever and vector store", "deepset-ai/haystack", "langchain-ai/langgraph"),
            stage("inference", "Model inference", "Run a language model behind an endpoint", "Generate answers using retrieved context", "vllm-project/vllm", "ggml-org/llama.cpp"),
            stage("security", "Input/output safety", "Test and screen risky inputs and model outputs", "Reduce known prompt- and content-based risks", "protectai/llm-guard", "NVIDIA/garak"),
            stage("evaluation", "Quality evaluation", "Measure answer faithfulness and retrieval relevance", "Track quality before deployment and after changes", "explodinggradients/ragas", "confident-ai/deepeval"),
            stage("deployment", "Deployment", "Package and expose an inference-backed service", "Deliver a repeatable API deployment", "bentoml/BentoML", "ray-project/ray"),
        ),
        ("Document ingestion, chunking strategy, embeddings and vector index selection are not fully specified by this catalog.", "Select and license an actual model and weights; check model behavior and hardware fit.", "Implement authentication, secret management, privacy controls, telemetry, backup and hosting."),
        ("Use a held-out question set to measure retrieval and answer grounding.", "Test prompt injection through retrieved documents.", "Verify access controls on each document and API request.", "Load-test realistic traffic and set latency/cost targets."),
    ),
    "Evaluate and red-team an existing model": Recipe(
        "Evaluate and red-team an existing model",
        "Assess a model you did not train: benchmarks, behavioral tests, adversarial probing and artifact scanning before adoption.",
        (
            stage("foundation", "Model loading", "Load weights and tokenizers for testing", "Provide a consistent harness for every test below", "huggingface/transformers"),
            stage("benchmarks", "Capability benchmarks", "Run standard task suites against the model", "Establish a comparable baseline", "EleutherAI/lm-evaluation-harness", "stanford-crfm/helm", "huggingface/lighteval"),
            stage("behavior", "Behavioral testing", "Probe bias, robustness and task-specific failure modes", "Catch issues that benchmarks do not measure", "Giskard-AI/giskard", "confident-ai/deepeval", "mit-ll-ai-technology/checkmaite"),
            stage("security", "Adversarial probing", "Red-team for jailbreaks, leakage and adversarial inputs", "Find exploitable behavior before deployment", "NVIDIA/garak", "Azure/PyRIT", "Trusted-AI/adversarial-robustness-toolbox"),
            stage("artifacts", "Artifact scanning", "Scan model files for unsafe serialization", "Avoid executing untrusted code when loading weights", "protectai/modelscan"),
            stage("deployment", "Scale the test harness", "Run evaluations across many models or configurations", "Keep assessment repeatable as models change", "ray-project/ray", optional=True),
        ),
        ("Acceptance thresholds, sign-off owners and re-test cadence are organizational decisions this catalog does not make.", "Benchmark scores can be contaminated by training data; verify against held-out, domain-specific sets.", "Confirm the model license permits your intended use and redistribution."),
        ("Record benchmark results with model hash, prompt format and decoding settings.", "Run the adversarial suite on the exact deployment configuration, including system prompts.", "Scan every downloaded artifact before loading it.", "Re-run the full suite when the model, prompt or serving stack changes."),
    ),
    "Classical ML prediction service": Recipe(
        "Classical ML prediction service",
        "Train, evaluate and serve a tabular model with a reproducible pipeline and production endpoint.",
        (
            stage("foundation", "Numerical foundation", "Array and scientific computing", "Underpin data preparation and modeling", "numpy/numpy", "scipy/scipy"),
            stage("modeling", "Modeling", "Train and validate classical models", "Use well-tested estimators and cross-validation", "scikit-learn/scikit-learn"),
            stage("pipeline", "Pipeline and tracking", "Define reproducible training steps and track runs", "Make retraining repeatable", "zenml-io/zenml", "kubeflow/kubeflow"),
            stage("evaluation", "Model testing", "Test performance, fairness and robustness on tabular data", "Catch regressions and bias before release", "Giskard-AI/giskard", "mit-ll-ai-technology/checkmaite"),
            stage("security", "Adversarial robustness", "Test classifiers against adversarial inputs", "Understand how inputs can be manipulated", "Trusted-AI/adversarial-robustness-toolbox", optional=True),
            stage("inference", "Serving", "Expose predictions through an endpoint", "Deliver a repeatable API deployment", "bentoml/BentoML", "kserve/kserve"),
            stage("deployment", "Platform", "Run training and serving on shared infrastructure", "Manage compute for the team", "ray-project/ray", "nebari-dev", optional=True),
        ),
        ("Feature storage, data validation and drift monitoring are not covered by this catalog.", "Data access, privacy review and retention rules are organizational decisions.", "Select hosting, authentication and observability separately."),
        ("Compare against a simple baseline on a held-out set.", "Test prediction quality on each important subgroup.", "Verify the serving endpoint returns identical results to the training-time model.", "Load-test realistic traffic and set latency targets."),
    ),
    "Distributed training at scale": Recipe(
        "Distributed training at scale",
        "Plan multi-GPU or multi-node pre-training or large fine-tuning with scale-out utilities and shared infrastructure.",
        (
            stage("foundation", "Framework", "Select the training framework", "Provide model and tensor operations", "pytorch/pytorch", "jax-ml/jax"),
            stage("training", "Training recipe", "Choose a training codebase", "Start from a maintained, reproducible recipe", "Lightning-AI/litgpt", "pytorch/torchtune", "axolotl-ai-cloud/axolotl"),
            stage("scale", "Scale-out", "Distribute training across devices and nodes", "Fit larger models and shorten wall-clock time", "deepspeedai/DeepSpeed", "huggingface/accelerate", "ray-project/ray"),
            stage("kernels", "Kernel tooling", "Write or tune custom kernels", "Remove bottlenecks the framework does not optimize", "triton-lang/triton", "arogozhnikov/einops", optional=True),
            stage("security", "Checkpoint scanning", "Scan saved checkpoints before reuse", "Avoid loading unsafe serialized artifacts", "protectai/modelscan"),
            stage("evaluation", "Evaluation", "Benchmark checkpoints during and after training", "Detect regressions early", "EleutherAI/lm-evaluation-harness"),
            stage("deployment", "Platform", "Provision and manage cluster resources", "Run training jobs on shared, reproducible infrastructure", "nebari-dev", "kubeflow/kubeflow"),
        ),
        ("Cluster provisioning, networking, storage throughput and cost controls are outside this catalog.", "Training data pipelines, deduplication and licensing are not defined here.", "Confirm rights to train on and distribute resulting weights."),
        ("Verify checkpoint save and resume on a short run before a long one.", "Measure throughput per device and scaling efficiency as nodes are added.", "Scan every checkpoint before loading.", "Evaluate intermediate checkpoints against a fixed benchmark set."),
    ),
    "Compile and optimize a model for target hardware": Recipe(
        "Compile and optimize a model for target hardware",
        "Quantize, compile and benchmark a trained model for edge devices, accelerators or Apple silicon.",
        (
            stage("foundation", "Source framework", "The framework the model was trained in", "Export from the original representation", "pytorch/pytorch", "jax-ml/jax"),
            stage("quantization", "Quantization", "Reduce precision for memory and speed", "Fit the model on the target device", "pytorch/ao", "ModelCloud/GPTQModel", "ggml-org/ggml"),
            stage("compile", "Compilation", "Lower the model to hardware-specific code", "Get portable, optimized executables", "iree-org/iree", "openxla/xla", "openxla/stablehlo"),
            stage("kernels", "Kernel tuning", "Benchmark and tune critical kernels", "Close the gap between compiled and hand-tuned performance", "triton-lang/triton", "thunlp/TritonBench", optional=True),
            stage("inference", "Runtime", "Run the optimized model on the device", "Match the runtime to the hardware", "ggml-org/llama.cpp", "NVIDIA/TensorRT-LLM", "ml-explore/mlx"),
            stage("evaluation", "Quality check", "Confirm accuracy survived optimization", "Quantization and compilation can change outputs", "EleutherAI/lm-evaluation-harness"),
        ),
        ("On-device packaging, update delivery and device management are not covered by this catalog.", "Hardware availability, drivers and vendor SDK licensing are external constraints.", "Model license terms still apply to optimized copies."),
        ("Compare accuracy before and after quantization on a held-out set.", "Measure latency, memory and energy on the actual target device.", "Verify numerical outputs match within tolerance across runtimes.", "Test the fallback path when the accelerator is unavailable."),
    ),
    "Formally verify a safety-critical component": Recipe(
        "Formally verify a safety-critical component",
        "Specify and prove properties of a neural network or the system around it, where testing alone is not enough.",
        (
            stage("foundation", "Model", "The trained component to verify", "Verification targets a concrete, fixed model", "pytorch/pytorch"),
            stage("nn-verification", "Neural network verification", "Prove bounds or robustness properties of the network", "Certify behavior over input regions, not just test points", "NeuralNetworkVerification/Marabou", "Verified-Intelligence/auto_LiRPA"),
            stage("specification", "Specification and proof", "Write and check specifications for surrounding code", "Make guarantees about the code that uses the model", "leanprover/lean4", "dafny-lang/dafny", "verus-lang/verus"),
            stage("system", "System and protocol modeling", "Model concurrency, failure and decision logic", "Find design errors before implementation", "tlaplus/tlaplus", "Z3Prover/z3"),
            stage("security", "Robustness testing", "Empirically test adversarial robustness alongside proofs", "Proofs cover stated properties; tests catch the rest", "Trusted-AI/adversarial-robustness-toolbox"),
            stage("evaluation", "Assurance evidence", "Collect test and verification evidence for review", "Support certification or audit", "mit-ll-ai-technology/checkmaite", optional=True),
        ),
        ("Writing the specification is the hardest step and no tool in this catalog does it for you.", "Verification results hold only for the stated property, input region and exact model; retraining invalidates them.", "Certification processes, safety cases and regulatory requirements are outside this catalog."),
        ("State each property in plain language and in the tool's formal language, and have both reviewed.", "Verify the deployed model hash matches the verified one.", "Re-run verification after any retraining or quantization.", "Pair every proof with an empirical test of the same property."),
    ),
}

def candidates(stage: Stage, projects: Iterable[Project]) -> list[Project]:
    """Only return recommendations genuinely present in the parsed catalog."""
    available = {p.url.rstrip('/').lower(): p for p in projects}
    return [available[url.rstrip('/').lower()] for url in stage.repo_urls if url.rstrip('/').lower() in available]


def defaults(recipe: Recipe, projects: Iterable[Project]) -> dict[str, str | None]:
    return {s.id: (candidates(s, projects)[0].url if candidates(s, projects) else None) for s in recipe.stages}


def architecture(recipe_name: str, projects: Iterable[Project], choices: dict[str, str | None], context: dict[str, str]) -> dict:
    if recipe_name not in RECIPES:
        raise ValueError("Unknown template")
    recipe = RECIPES[recipe_name]
    project_map = {p.url: p for p in projects}
    steps = []
    for s in recipe.stages:
        url = choices.get(s.id)
        p = project_map.get(url) if url else None
        steps.append({"id": s.id, "stage": s.title, "purpose": s.description, "rationale": s.why,
                      "optional": s.optional, "tool": p.name if p else None, "repository": p.url if p else None})
    return {"template": recipe_name, "goal": context.get("goal", ""), "deployment": context.get("deployment", ""),
            "data_sensitivity": context.get("data_sensitivity", ""), "constraints": context.get("constraints", ""),
            "stages": steps, "gaps": list(recipe.gaps), "verification": list(recipe.tests),
            "disclaimer": "Planning blueprint only. Selection does not verify license compatibility, integration, security or deployment readiness."}


def blueprint_markdown(plan: dict) -> str:
    lines = [f"# AI system blueprint: {plan['template']}", "", f"**Goal:** {plan['goal'] or 'Not specified'}",
             f"**Deployment:** {plan['deployment'] or 'Not specified'}", f"**Data sensitivity:** {plan['data_sensitivity'] or 'Not specified'}",
             f"**Constraints:** {plan['constraints'] or 'Not specified'}", "", "## Proposed stages", ""]
    for n, s in enumerate(plan['stages'], 1):
        tool = f"[{s['tool']}]({s['repository']})" if s['tool'] else "Not selected — needs decision"
        lines.extend([f"### {n}. {s['stage']}", f"- Purpose: {s['purpose']}", f"- Proposed tool: {tool}",
                      f"- Reason: {s['rationale']}", ""])
    lines.extend(["## Unresolved dependencies", ""] + [f"- [ ] {gap}" for gap in plan['gaps']])
    lines.extend(["", "## Validation checklist", ""] + [f"- [ ] {test}" for test in plan['verification']])
    lines.extend(["", "## Caveat", plan['disclaimer']])
    return "\n".join(lines) + "\n"


def blueprint_json(plan: dict) -> str:
    return json.dumps(plan, indent=2, ensure_ascii=False)
