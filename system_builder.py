"""Deterministic, catalog-grounded architecture planning for OpenTeams AI Explorer.

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
    "Document Q&A (RAG)": Recipe(
        "Document Q&A (RAG)",
        "Build a document question-answering service with retrieval, model inference, evaluation and guardrails.",
        (
            stage("foundation", "Application foundation", "Numerical and model utilities", "Support data and model processing", "numpy/numpy", "huggingface/transformers"),
            stage("pipeline", "Retrieval and orchestration", "Index and retrieve relevant document content", "Connect documents to prompts; validate retrieval behavior", "deepset-ai/haystack", "langchain-ai/langgraph"),
            stage("inference", "Model inference", "Run a language model behind an endpoint", "Generate answers using retrieved context", "vllm-project/vllm", "ggml-org/llama.cpp"),
            stage("security", "Input/output safety", "Test and screen risky inputs and model outputs", "Reduce known prompt- and content-based risks", "protectai/llm-guard", "NVIDIA/garak"),
            stage("evaluation", "Quality evaluation", "Measure answer faithfulness and retrieval relevance", "Track quality before deployment and after changes", "explodinggradients/ragas", "confident-ai/deepeval"),
            stage("deployment", "Deployment", "Package and expose an inference-backed service", "Deliver a repeatable API deployment", "bentoml/BentoML", "ray-project/ray"),
        ),
        ("Document ingestion, chunking strategy, embeddings and vector index selection are not fully specified by this catalog.", "Select and license an actual model and weights; check model behavior and hardware fit.", "Implement authentication, secret management, privacy controls, telemetry, backup and hosting."),
        ("Use a held-out question set to measure retrieval and answer grounding.", "Test prompt injection through retrieved documents.", "Verify access controls on each document and API request.", "Load-test realistic traffic and set latency/cost targets."),
    ),
    "Tool-using AI agent": Recipe(
        "Tool-using AI agent",
        "Design a supervised agent that can call tools, produce structured results and recover from failures.",
        (
            stage("foundation", "Core model utilities", "Model interfaces and tensor processing", "Provide model integration building blocks", "huggingface/transformers", "pytorch/pytorch"),
            stage("orchestration", "Agent orchestration", "Implement tool calls, state and approvals", "Control multi-step tasks with human review", "langchain-ai/langgraph", "pydantic/pydantic-ai", "crewAIInc/crewAI"),
            stage("inference", "Model inference", "Host the language model", "Separate agent logic from serving", "vllm-project/vllm", "ggml-org/llama.cpp"),
            stage("security", "Adversarial testing", "Probe unsafe prompts and tool behavior", "Catch tool misuse and risky instructions", "Azure/PyRIT", "NVIDIA/garak"),
            stage("evaluation", "Agent evaluations", "Test task success and failure recovery", "Measure useful behavior against a scenario suite", "confident-ai/deepeval", "huggingface/lighteval"),
            stage("deployment", "Serving", "Deploy the API or workflow service", "Expose the agent with operational controls", "bentoml/BentoML", "ray-project/ray"),
        ),
        ("Design actual tool connectors and schemas; integrations are not guaranteed by this list.", "Define permissions, human approvals and audit logs for sensitive actions.", "Select an actual model, hosting, identity provider and secrets store."),
        ("Test a no-access tool call and ensure it fails safely.", "Test tool timeout, malformed output and partial execution recovery.", "Review prompts and tools for injection and privilege escalation.", "Set human approval checkpoints for consequential actions."),
    ),
    "Local private assistant": Recipe(
        "Local private assistant",
        "Prototype a local-first assistant with a small operational footprint.",
        (
            stage("foundation", "Application utilities", "Local numerical or model data utilities", "Support lightweight local processing", "numpy/numpy", "huggingface/transformers"),
            stage("interface", "Interactive development", "Build a local prototype interface", "Iterate on prompts and interactions", "marimo-team/marimo", "jupyterlab/jupyter-ai"),
            stage("inference", "Local inference", "Run quantized models on local hardware", "Keep inference under local operational control", "ggml-org/llama.cpp", "ggml-org/ggml"),
            stage("security", "Local safety checks", "Screen unsafe content and test vulnerabilities", "Reduce accidental unsafe responses", "protectai/llm-guard", "NVIDIA/garak"),
            stage("evaluation", "Quality checks", "Test expected question-answer scenarios", "Check quality on actual target hardware", "confident-ai/deepeval", "EleutherAI/lm-evaluation-harness"),
            stage("deployment", "Optional local packaging", "Package the prototype as a service", "Support repeatable local installs", "bentoml/BentoML", optional=True),
        ),
        ("Select and verify a compatible model, weights and local hardware requirements.", "Local operation does not automatically guarantee privacy: review logging, telemetry and external calls.", "Package UI, storage, backups and operating-system permissions separately."),
        ("Verify network traffic remains within the intended boundary.", "Benchmark latency and memory on target devices.", "Verify safety rules and input handling work offline."),
    ),
    "Fine-tune and serve a model": Recipe(
        "Fine-tune and serve a model",
        "Plan a model adaptation pipeline with training, optimization, serving and quality gates.",
        (
            stage("foundation", "Training framework", "Select your deep learning base", "Provide model and tensor operations", "pytorch/pytorch", "huggingface/transformers"),
            stage("training", "Fine-tuning", "Train or adapt a pretrained model", "Use a reproducible training recipe", "hiyouga/LLaMA-Factory", "unslothai/unsloth", "huggingface/trl"),
            stage("optimization", "Optimize", "Quantize or adapt for target hardware", "Reduce memory or improve throughput", "pytorch/ao", "bitsandbytes-foundation/bitsandbytes"),
            stage("inference", "Serve", "Deploy model inference", "Make the model usable via an endpoint", "vllm-project/vllm", "sgl-project/sglang"),
            stage("security", "Scan and red-team", "Test model files and unsafe behavior", "Find risks before release", "protectai/modelscan", "NVIDIA/garak"),
            stage("evaluation", "Benchmark and evaluate", "Test regressions and task performance", "Measure adaptation results against baseline", "EleutherAI/lm-evaluation-harness", "huggingface/lighteval"),
            stage("deployment", "Production packaging", "Deploy models with repeatable infrastructure", "Manage rollouts and scaling", "bentoml/BentoML", "kserve/kserve"),
        ),
        ("Training data governance, provenance and labeling are not defined by this catalog.", "Confirm model licenses and rights to train and distribute resulting weights.", "Add artifact registry, observability, GPU provisioning, rollback and incident response."),
        ("Compare quality against the base model on a held-out dataset.", "Review training data for private or restricted material.", "Scan artifacts and track software/model provenance.", "Run throughput, memory and rollback tests."),
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
