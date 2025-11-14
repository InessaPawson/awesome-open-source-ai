# awesome-nebari

Curated tools and write-ups that the Nebari awesome-list team has hands-on experience with for building Nebari-based AI systems. (Vör was the legacy name prior to 1 Nov 2025.)

## Where to Start
- Read `models/intro_to_OR.md` for Dillon’s overview of OpenRouter and how we evaluate hosted models.
- Browse `models/models_list.md` for the latest, opinionated model table (benchmarks, links, and why we care).
- Use this README as the jumping-off point for the broader categories we maintain together.

## Categories We Stand Behind
- **Frameworks:** [Pydantic-AI](https://ai.pydantic.dev/), [LangGraph](https://www.langchain.com/langgraph), [Hrafnar](https://github.com/openteams-ai/hrafnar).
- **DevOps Tooling:** [liteLLM](https://www.litellm.ai/), [MLflow](https://mlflow.org/), [OpenTofu](https://opentofu.org/), [Kamal](https://kamal-deploy.org/).
- **Model Building & Tuning:** [PyTorch](https://pytorch.org/), [XGBoost](https://xgboost.readthedocs.io/en/stable/), [Unsloth](https://unsloth.ai/), [HF Transformers](https://huggingface.co/docs/transformers/en/index).
- **Model Inference & Hosting:** [llama.cpp](https://github.com/ggml-org/llama.cpp), [vLLM](https://docs.vllm.ai/en/latest/), [KServe](https://kserve.github.io/website/), [Envoy Gateway](https://gateway.envoyproxy.io/), [OpenRouter](https://openrouter.ai/), [Lemonade Server](https://lemonade-server.ai/).
- **Dev Tools & Frontend:** [Pixi](https://pixi.sh/latest/), [Lumino](https://github.com/jupyterlab/lumino) (chosen frontend), [Nebari](https://www.nebari.dev/).
- **Observability:** [OpenTelemetry](https://opentelemetry.io/), [Loki](https://grafana.com/oss/loki/), [Grafana](https://grafana.com/oss/grafana), [Tempo](https://grafana.com/oss/tempo/), [Mimir](https://grafana.com/oss/mimir/), [Prometheus](https://prometheus.io/), [Langfuse](https://langfuse.com/).

## Quick Reference List
This section mirrors the original awesome-nebari bullets for folks who want the high-level scan.

### Frameworks
- Pydantic-Ai: [https://ai.pydantic.dev/](https://ai.pydantic.dev/)
- Langgraph: [https://www.langchain.com/langgraph](https://www.langchain.com/langgraph)
- Hrafnar: [https://github.com/openteams-ai/hrafnar](https://github.com/openteams-ai/hrafnar)

### DevOps Tooling
- liteLLM: [https://www.litellm.ai/](https://www.litellm.ai/)
- MLflow: [https://mlflow.org/](https://mlflow.org/)
- Open-Tofu: [https://opentofu.org/](https://opentofu.org/)
- Kamal: [https://kamal-deploy.org/](https://kamal-deploy.org/)

### Model Building and Tuning
- pytorch: [https://pytorch.org/](https://pytorch.org/)
- xgboost: [https://xgboost.readthedocs.io/en/stable/](https://xgboost.readthedocs.io/en/stable/)
- unsloth: [https://unsloth.ai/](https://unsloth.ai/)
- HF transformers [https://huggingface.co/docs/transformers/en/index](https://huggingface.co/docs/transformers/en/index)

### Model Inference and Hosting
- llama.cpp: [https://github.com/ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)
- vLLM: [https://docs.vllm.ai/en/latest/](https://docs.vllm.ai/en/latest/)
- kserve: [https://kserve.github.io/website/](https://kserve.github.io/website/)
- Envoy Gateway: [https://gateway.envoyproxy.io/](https://gateway.envoyproxy.io/)
- OpenRouter (Service): [https://openrouter.ai/](https://openrouter.ai/)
- Lemonade Server: [https://lemonade-server.ai/](https://lemonade-server.ai/)

### Dev Tools
- Pixi [https://pixi.sh/latest/](https://pixi.sh/latest/)
- Lumino [https://github.com/jupyterlab/lumino](https://github.com/jupyterlab/lumino)
- Nebari [https://www.nebari.dev/](https://www.nebari.dev/)

### Observability
- OpenTelemetry: [https://opentelemetry.io/](https://opentelemetry.io/)
- Loki: [https://grafana.com/oss/loki/](https://grafana.com/oss/loki/)
- Grafana: [https://grafana.com/oss/grafana](https://grafana.com/oss/grafana)
- Tempo: [https://grafana.com/oss/tempo/](https://grafana.com/oss/tempo/)
- Mimir: [https://grafana.com/oss/mimir/](https://grafana.com/oss/mimir/)
- Prometheus: [https://prometheus.io/](https://prometheus.io/)
- Langfuse: [https://langfuse.com/](https://langfuse.com/)

## Decisions from the Oct 30 2025 Awesome-List Sync
- Keep the list tight and curated—include only tooling we actively use or can confidently recommend today.
- Lumino is the frontend direction for Nebari awesome; future UI updates should show how it supports easy file uploads and a lightweight dev experience (Travis’s priority).
- Approval path is expanding so updates are not blocked on Darhos alone; William Martinez-Torres (WMT), Dillon Roach, and Chuck are the additional approvers we will loop in.

## Contributing
- Start with a draft PR that describes where an item fits (category, link, quick rationale, and hands-on notes).
- Tag WMT, Dillon, and Chuck on the PR for review along with anyone owning the category.
- Prefer depth over breadth; if something is aspirational, label the risk/reward and who will validate it next.

Questions? Open an issue or drop a note in the nebari awesome-list channel—either way we’ll route it to the right reviewer.
Collapse
