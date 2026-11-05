# Open and Open-Weight AI Models

> A curated starting point for evaluating downloadable AI models for research, development, and deployment.
>
> **Last editorial update:** 2026-11-04. **Scope:** This is a model directory, not a performance ranking or an endorsement by OpenTeams.

Many models described as "open source" are more accurately **open weight**: weights may be downloadable while training data, training code, or usage rights remain restricted. **Always review the license and model card for the exact checkpoint before using a model commercially, redistributing it, or deploying it with sensitive data.** An inference API's terms may differ from the model's license.

## Contents

- [How to use this list](#how-to-use-this-list)
- [Inclusion criteria](#inclusion-criteria)
- [General-purpose and reasoning models](#general-purpose-and-reasoning-models)
- [Smaller and efficient models](#smaller-and-efficient-models)
- [Coding and software engineering models](#coding-and-software-engineering-models)
- [Vision and multimodal models](#vision-and-multimodal-models)
- [UI generation and computer-use models](#ui-generation-and-computer-use-models)
- [Historical and reference checkpoints](#historical-and-reference-checkpoints)
- [Benchmarks and evaluation](#benchmarks-and-evaluation)
- [License verification notes](#license-verification-notes)
- [Contributing](#contributing)
- [Changelog](#changelog)

## How to use this list

- **Checkpoint:** Hugging Face links identify the checkpoint described by each row. Check the model card and repository revision before deployment; some repositories require accepting terms or requesting access.
- **Hosted inference:** OpenRouter links point to a hosted endpoint for the same release and variant as the checkpoint. They are not a guarantee of an identical revision, quantization, or configuration, so confirm the provider model ID and capabilities before comparing outputs. `—` means no hosted link is provided; it does not mean hosting is impossible. Availability, pricing, and context length can change.
- **Model size:** Parameter counts and active parameters are not interchangeable for mixture-of-experts (MoE) models; compare memory and throughput using the specific architecture and deployment format.
- **License:** Values are reported from model cards or associated license files where checked; **this is not a completed license audit of every row**. Read the license for the exact checkpoint and any upstream/base-model obligations before commercial use, modification, or redistribution. Apache-2.0 and MIT are OSI-approved *software licenses*, but applying one to model weights does not, by itself, establish compliance with the [Open Source AI Definition](https://opensource.org/ai/open-source-ai-definition). Custom or modified licenses may impose additional conditions. See [License verification notes](#license-verification-notes).
- **Evaluation focus:** Short descriptions identify the intended evaluation category, not verified superiority.

### Openness and licensing terminology

- **Open-source AI:** Whether a system satisfies the [Open Source AI Definition](https://opensource.org/ai/open-source-ai-definition) depends on the required code, parameters, and information about data and training—not merely the name of its license.
- **Open weights:** Weights are downloadable, but additional materials needed to study, modify, or reproduce the system may not be available.
These terms describe different properties. The directory does **not** classify rows by them: there is no openness column, and the License column records only what the model card or license file states. Use the terms as a lens for your own assessment, and consult original model and license materials before making policy or procurement decisions.

## Inclusion criteria

The main sections feature downloadable checkpoints that remain useful starting points for evaluation. Selection is editorial, not a performance ranking. Contributors should identify an exact checkpoint, a primary use case, and its published licensing terms. Model age, a newer release, or parameter count **alone** does not determine inclusion.

A checkpoint may move to [Historical and reference checkpoints](#historical-and-reference-checkpoints) when a well-established alternative serves a comparable use case **and** the older checkpoint no longer has a clearly documented advantage for the directory's intended audiences. Consider architecture (including dense versus MoE), licensing, hardware and memory requirements, inference latency, model capabilities, and value as a research baseline. **Active parameter count is not a measure of total deployment cost.** Such moves require an editorial rationale; where evidence is uncertain, keep the checkpoint in the main catalog or label the move as an editorial judgment rather than an objective performance claim.

Historical and reference checkpoints remain discoverable, including when they are useful for reproducibility or comparison. A suggested alternative is not necessarily a direct successor. Preview checkpoints should be revisited after a stable release appears.

## General-purpose and reasoning models

Models to consider for general language generation, knowledge-intensive work, and multi-step reasoning. Listed alphabetically; **not ranked**.

| Model / checkpoint | Organization | Hugging Face | Hosted inference | License (per model card) | Evaluation focus |
| --- | --- | --- | --- | --- | --- |
| Arcee Trinity Large Preview | Arcee AI | [Model card](https://huggingface.co/arcee-ai/Trinity-Large-Preview) | [OpenRouter](https://openrouter.ai/arcee-ai/trinity-large-preview) | Apache-2.0 | General-purpose instruction following; preview checkpoint |
| DeepSeek R1 0528 | DeepSeek | [Model card](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) | [OpenRouter](https://openrouter.ai/deepseek/deepseek-r1-0528) | MIT | Reasoning and mathematics |
| DeepSeek V3.2 | DeepSeek | [Model card](https://huggingface.co/deepseek-ai/DeepSeek-V3.2) | [OpenRouter](https://openrouter.ai/deepseek/deepseek-chat-v3.2) | MIT | General-purpose and reasoning |
| GLM-5 | Z.ai | [Model card](https://huggingface.co/zai-org/GLM-5) | [OpenRouter](https://openrouter.ai/z-ai/glm-5) | MIT | General-purpose and tool use |
| GPT-OSS 120B | OpenAI | [Model card](https://huggingface.co/openai/gpt-oss-120b) | [OpenRouter](https://openrouter.ai/openai/gpt-oss-120b) | Apache-2.0 | Reasoning; large deployment |
| Kimi K2.5 | Moonshot AI | [Model card](https://huggingface.co/moonshotai/Kimi-K2.5) | [OpenRouter](https://openrouter.ai/moonshotai/kimi-k2.5) | Modified MIT | Reasoning, coding, multimodal tasks |
| Llama 3.1 405B Instruct | Meta | [Model card](https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct) | [OpenRouter](https://openrouter.ai/meta-llama/llama-3.1-405b-instruct) | Llama 3.1 Community License | Large-scale general-purpose inference |
| Llama 3.3 70B Instruct | Meta | [Model card](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) | [OpenRouter](https://openrouter.ai/meta-llama/llama-3.3-70b-instruct) | Llama 3.3 Community License | General-purpose instruction following; dense 70B |
| Llama 4 Maverick | Meta | [Model card](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct) | [OpenRouter](https://openrouter.ai/meta-llama/llama-4-maverick) | Llama 4 Community License | General-purpose and multimodal |
| MiniMax M2.5 | MiniMax | [Model card](https://huggingface.co/MiniMaxAI/MiniMax-M2.5) | [OpenRouter](https://openrouter.ai/minimax/minimax-m2.5) | Modified MIT | Reasoning and agentic workflows |
| Mistral Large 3 | Mistral AI | [Model card](https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512) | [OpenRouter](https://openrouter.ai/mistralai/mistral-large-2512) | Apache-2.0 | General-purpose instruction following |
| NVIDIA Llama 3.1 Nemotron Ultra 253B v1 | NVIDIA | [Model card](https://huggingface.co/nvidia/Llama-3_1-Nemotron-Ultra-253B-v1) | [OpenRouter](https://openrouter.ai/nvidia/llama-3.1-nemotron-ultra-253b-v1) | NVIDIA Open Model License | Reasoning |
| Qwen3 235B-A22B Thinking 2507 | Qwen | [Model card](https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507) | [OpenRouter](https://openrouter.ai/qwen/qwen3-235b-a22b-thinking-2507) | Apache-2.0 | Reasoning |
| Qwen3.5 397B-A17B | Qwen | [Model card](https://huggingface.co/Qwen/Qwen3.5-397B-A17B) | [OpenRouter](https://openrouter.ai/qwen/qwen3.5-397b-a17b) | Apache-2.0 | General-purpose and multimodal |

## Smaller and efficient models

Smaller *relative to frontier-scale models*, though some still require substantial accelerator memory. This group includes dense and MoE checkpoints; verify **active versus total** parameters.

| Model / checkpoint | Organization | Hugging Face | Hosted inference | License (per model card) | Evaluation focus |
| --- | --- | --- | --- | --- | --- |
| Gemma 3 27B IT | Google | [Model card](https://huggingface.co/google/gemma-3-27b-it) | [OpenRouter](https://openrouter.ai/google/gemma-3-27b-it) | Gemma Terms of Use | Instruction following and vision |
| GLM-4.7 Flash | Z.ai | [Model card](https://huggingface.co/zai-org/GLM-4.7-Flash) | [OpenRouter](https://openrouter.ai/z-ai/glm-4.7-flash) | MIT | Efficient general-purpose use |
| GPT-OSS 20B | OpenAI | [Model card](https://huggingface.co/openai/gpt-oss-20b) | [OpenRouter](https://openrouter.ai/openai/gpt-oss-20b) | Apache-2.0 | Reasoning with smaller deployments |
| Magistral Small 2506 | Mistral AI | [Model card](https://huggingface.co/mistralai/Magistral-Small-2506) | [OpenRouter](https://openrouter.ai/mistralai/magistral-small-2506) | Apache-2.0 | Reasoning |
| NVIDIA Llama 3.3 Nemotron Super 49B v1.5 | NVIDIA | [Model card](https://huggingface.co/nvidia/Llama-3_3-Nemotron-Super-49B-v1_5) | [OpenRouter](https://openrouter.ai/nvidia/llama-3.3-nemotron-super-49b-v1.5) | NVIDIA Open Model License | Reasoning |
| NVIDIA Nemotron 3 Nano 30B-A3B | NVIDIA | [Model card](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16) | [OpenRouter](https://openrouter.ai/nvidia/nemotron-3-nano-30b-a3b) | NVIDIA Open Model License | Efficient MoE inference |
| OLMo 3.1 32B Instruct | Ai2 | [Model card](https://huggingface.co/allenai/Olmo-3.1-32B-Instruct) | [OpenRouter](https://openrouter.ai/allenai/olmo-3.1-32b-instruct) | Apache-2.0 | Research transparency and instruction following |
| Qwen QwQ 32B | Qwen | [Model card](https://huggingface.co/Qwen/QwQ-32B) | [OpenRouter](https://openrouter.ai/qwen/qwq-32b) | Apache-2.0 | Reasoning baseline with dense architecture |
| Qwen3 30B-A3B Thinking 2507 | Qwen | [Model card](https://huggingface.co/Qwen/Qwen3-30B-A3B-Thinking-2507) | — | Apache-2.0 | Efficient reasoning |

## Coding and software engineering models

Coding performance depends heavily on whether models receive an agent harness, tools, tests, and multiple attempts. Distinguish code completion from repository-level issue solving.

| Model / checkpoint | Organization | Hugging Face | Hosted inference | License (per model card) | Evaluation focus |
| --- | --- | --- | --- | --- | --- |
| Devstral 2 123B Instruct 2512 | Mistral AI | [Model card](https://huggingface.co/mistralai/Devstral-2-123B-Instruct-2512) | [OpenRouter](https://openrouter.ai/mistralai/devstral-2512) | Modified MIT (revenue restriction; see notes) | Software engineering agents |
| Devstral Small 2 24B Instruct 2512 | Mistral AI | [Model card](https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512) | — | Apache-2.0 | Smaller coding-agent deployments |
| Kimi-Dev 72B | Moonshot AI | [Model card](https://huggingface.co/moonshotai/Kimi-Dev-72B) | [OpenRouter](https://openrouter.ai/moonshotai/kimi-dev-72b) | MIT | Repository-level software engineering |
| Qwen3 Coder 30B-A3B Instruct | Qwen | [Model card](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct) | — | Apache-2.0 | Coding and tool use |
| Qwen3 Coder Next | Qwen | [Model card](https://huggingface.co/Qwen/Qwen3-Coder-Next) | [OpenRouter](https://openrouter.ai/qwen/qwen3-coder-next) | Apache-2.0 | Coding agents |

## Vision and multimodal models

For document understanding, OCR, charts, screenshots, and image-based reasoning, test on representative inputs. General image understanding is not the same as grounded detection or reliable OCR.

| Model / checkpoint | Organization | Hugging Face | Hosted inference | License (per model card) | Evaluation focus |
| --- | --- | --- | --- | --- | --- |
| GLM-4.6V | Z.ai | [Model card](https://huggingface.co/zai-org/GLM-4.6V) | [OpenRouter](https://openrouter.ai/z-ai/glm-4.6v) | MIT | Visual reasoning |
| Ministral 3 14B Instruct 2512 | Mistral AI | [Model card](https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512) | [OpenRouter](https://openrouter.ai/mistralai/ministral-14b-2512) | Apache-2.0 | Compact multimodal use |
| Mistral Small 3.2 24B Instruct | Mistral AI | [Model card](https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506) | [OpenRouter](https://openrouter.ai/mistralai/mistral-small-3.2-24b-instruct) | Apache-2.0 | General multimodal tasks |
| Molmo2 8B | Ai2 | [Model card](https://huggingface.co/allenai/Molmo2-8B) | [OpenRouter](https://openrouter.ai/allenai/molmo-2-8b) | Apache-2.0 | Image and visual reasoning |
| Qwen2.5 VL 72B Instruct | Qwen | [Model card](https://huggingface.co/Qwen/Qwen2.5-VL-72B-Instruct) | [OpenRouter](https://openrouter.ai/qwen/qwen2.5-vl-72b-instruct) | Qwen license | Document and image understanding |
| Qwen3 VL 30B-A3B Instruct | Qwen | [Model card](https://huggingface.co/Qwen/Qwen3-VL-30B-A3B-Instruct) | [OpenRouter](https://openrouter.ai/qwen/qwen3-vl-30b-a3b-instruct) | Apache-2.0 | Vision-language tasks |

**Also multimodal:** [Gemma 3 27B IT](https://huggingface.co/google/gemma-3-27b-it), [Kimi K2.5](https://huggingface.co/moonshotai/Kimi-K2.5), [Llama 4 Maverick](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct), and [Qwen3.5 397B-A17B](https://huggingface.co/Qwen/Qwen3.5-397B-A17B) appear in the earlier sections.

## UI generation and computer-use models

UI/code-generation checkpoints produce interface code from prompts or images. Computer-use models operate interfaces by reading screenshots and emitting actions. The two serve different purposes and are evaluated differently.

| Model / checkpoint | Organization | Hugging Face | Hosted inference | License (per model card) | Evaluation focus |
| --- | --- | --- | --- | --- | --- |
| UI-TARS 1.5 7B | ByteDance Seed | [Model card](https://huggingface.co/ByteDance-Seed/UI-TARS-1.5-7B) | — | Apache-2.0 | GUI understanding and computer-use agents |
| UIGEN-X 32B 0727 | Tesslate | [Model card](https://huggingface.co/Tesslate/UIGEN-X-32B-0727) | — | Apache-2.0 | UI/code generation |

**Safety note:** Evaluate computer-use agents in sandboxed environments with scoped permissions, human approval for consequential actions, and protections against prompt injection in screenshots and page content.

## Historical and reference checkpoints

These checkpoints remain useful as historical references or comparison baselines. Alternatives cover overlapping tasks but **are not necessarily direct replacements**; the notes reflect editorial placement, not proven superiority. See the [inclusion criteria](#inclusion-criteria).

| Model / checkpoint | Organization | Hugging Face | Hosted inference | License (per model card) | Suggested alternative | Editorial note |
| --- | --- | --- | --- | --- | --- | --- |
| Aria | Rhymes AI | [Model card](https://huggingface.co/rhymes-ai/Aria) | — | Apache-2.0 | See current vision and multimodal section | Retained for historical reference; the main multimodal section offers newer evaluation candidates |
| Llama 3.2 11B Vision Instruct | Meta | [Model card](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct) | [OpenRouter](https://openrouter.ai/meta-llama/llama-3.2-11b-vision-instruct) | Llama 3.2 Community License | Molmo2 8B; Ministral 3 14B | Retained as a reference point for earlier Llama vision models; alternative licensing and architectures differ |
| Llama 3.2 90B Vision Instruct | Meta | [Model card](https://huggingface.co/meta-llama/Llama-3.2-90B-Vision-Instruct) | [OpenRouter](https://openrouter.ai/meta-llama/llama-3.2-90b-vision-instruct) | Llama 3.2 Community License | Llama 4 Maverick | Earlier Meta vision checkpoint; Llama 4 Maverick is a newer multimodal candidate, not an equivalent deployment substitute |
| Molmo 72B 0924 | Ai2 | [Model card](https://huggingface.co/allenai/Molmo-72B-0924) | — | Apache-2.0 | Molmo2 8B | Earlier Molmo reference checkpoint; Molmo2 offers a newer, differently sized evaluation candidate |
| UI-TARS 72B DPO | ByteDance Seed | [Model card](https://huggingface.co/ByteDance-Seed/UI-TARS-72B-DPO) | [OpenRouter](https://openrouter.ai/bytedance-research/ui-tars-72b) | Apache-2.0 | UI-TARS 1.5 7B | Earlier GUI-agent checkpoint retained as a baseline; the smaller 1.5 model is not assumed to be an equivalent replacement |

## Benchmarks and evaluation

This directory does not publish a leaderboard. Benchmark numbers taken from different evaluation protocols (prompting, tool access, sampling, agent harness) are not comparable, and reproducing them without the full setup produces misleading rankings. The table below lists benchmarks commonly cited for these models and what a defensible result must specify.

| Benchmark | What it measures | Key caveat |
| --- | --- | --- |
| [MMLU-Pro](https://github.com/TIGER-AI-Lab/MMLU-Pro) | Broad academic knowledge and reasoning | Prompting and evaluation protocol affect scores |
| [SWE-bench](https://www.swebench.com/) | Resolving real software-repository issues | Specify Verified/other split, agent scaffold, tools, and attempts |
| [Humanity's Last Exam](https://lastexam.ai/) | Difficult expert-level knowledge and reasoning | Specify test subset, tool access, and scoring protocol |
| [GPQA](https://github.com/idavidrein/gpqa) | Graduate-level scientific questions | Specify Diamond subset and scoring approach |
| [LiveCodeBench](https://livecodebench.github.io/) | Competitive programming and coding | Specify date range, contamination controls, and pass@k |

For a defensible comparison, record the **exact checkpoint revision, evaluation date, benchmark version/split, hardware, quantization, inference engine, context setting, prompt template, tools or agent harness, pass@k, and a primary-source result link**. Use `Not reported` rather than a blank score, and never combine distinct SWE-bench configurations into a single undifferentiated value.

### Suggested contribution format for benchmark results

| Model revision | Benchmark and split | Score and unit | Evaluation setup | Date | Source |
| --- | --- | --- | --- | --- | --- |
| `org/model@revision` | `SWE-bench Verified` | `XX% resolved` | `agent / tools / attempts` | `YYYY-MM-DD` | `Primary result URL` |

## License verification notes

The following exceptions were checked against their published model-card metadata or license text on 2026-11-04. They do **not** imply that every other row has undergone a fresh license review.

- **[Devstral 2 123B Instruct 2512](https://huggingface.co/mistralai/Devstral-2-123B-Instruct-2512/blob/main/LICENSE):** Modified MIT. Its license restricts exercising licensed rights if the company or employer's **global consolidated revenue exceeded US$20 million in the preceding month**; it provides a path to request a separate commercial license. Do not confuse it with Devstral Small 2.
- **[Devstral Small 2 24B Instruct 2512](https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512):** Apache-2.0, according to its official model card.
- **[MiniMax M2.5](https://huggingface.co/MiniMaxAI/MiniMax-M2.5):** `modified-mit`, not plain MIT. Read its license terms before relying on commercial or redistribution rights.
- **[UIGEN-X 32B 0727](https://huggingface.co/Tesslate/UIGEN-X-32B-0727):** Apache-2.0, according to its model-card metadata.

## Contributing

Contributions are welcome. For a straightforward model addition or metadata correction, please provide:

1. **Exact downloadable checkpoint** and model-card URL, including the relevant base or instruct variant.
2. **Primary use case** and the most appropriate category; use cross-references rather than duplicate rows.
3. **Published license identifier or license link**, including any material restrictions visible in the source. If terms are unclear, flag them for maintainer review rather than guessing.
4. **Hosted inference URL, if supplied**, only when it appears to match the model's release and variant; leave it blank (`—`) if uncertain.

Benchmark numbers are **optional**. If adding a quantitative claim, provide the primary result source and sufficient evaluation details to make it interpretable. For proposed moves to the historical/reference section, explain the rationale and meaningful tradeoffs; avoid inferring lower deployment cost from active parameter counts alone. Maintainers can conduct additional license and link verification during review; contributors are not expected to perform a full audit of the directory.

Please keep descriptions concise and classifications neutral. A link checker is encouraged before submitting, but is not required for every small correction. For detailed change history, rely on Git and the pull request description.

## Changelog

- **2026-11-04:** Reorganized the model directory and corrected checkpoint and hosted links to match the described variants. Added a License column, license verification notes, openness terminology, inclusion criteria, and a Historical and reference checkpoints section. Added UI-TARS 1.5 7B. Lists QwQ 32B as a dense reasoning baseline. Removed the previously published benchmark score table because sources and evaluation setups were not consistently documented. See Git history and pull requests for individual changes.
