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
- [Specialized UI and computer-use models](#specialized-ui-and-computer-use-models)
- [Legacy checkpoints](#legacy-checkpoints)
- [Benchmarks and evaluation](#benchmarks-and-evaluation)
- [Contributing](#contributing)
- [Changelog](#changelog)

## How to use this list

- **Checkpoint:** The Hugging Face link points to the exact checkpoint being described, including its model card. Some repositories require accepting terms or requesting access.
- **Hosted inference:** OpenRouter links point to the same release and variant as the checkpoint. `—` means no matching provider link has been supplied or verified, not that hosting is impossible. Availability, pricing, and context length can change.
- **Model size:** Parameter counts and active parameters are not interchangeable for mixture-of-experts (MoE) models; compare memory and throughput using the specific architecture and deployment format.
- **License:** The license column records what the model card stated when the row was last reviewed. It is a starting point, not legal advice: licenses change, base-model restrictions can apply, and several entries are custom licenses (Llama Community License, Gemma Terms of Use, NVIDIA Open Model License, Qwen license) with their own conditions. Only Apache-2.0 and MIT entries should be assumed OSI-approved.
- **Evaluation focus:** Short descriptions identify the intended evaluation category, not verified superiority.

## Inclusion criteria

A row is kept in the main sections when it is still a reasonable starting point for evaluation in its category. A row moves to [Legacy checkpoints](#legacy-checkpoints) when the same organization has published a successor that appears in this list, or when the checkpoint is more than roughly eighteen months old and no longer represents the state of its category. Legacy rows are kept for a limited time so that readers who already use those models can still find them, then removed. Preview checkpoints are listed only until the final release is available.

## General-purpose and reasoning models

Models to consider for general language generation, knowledge-intensive work, and multi-step reasoning. Listed alphabetically; **not ranked**.

| Model / checkpoint | Organization | Hugging Face | Hosted inference | License (per model card) | Evaluation focus |
| --- | --- | --- | --- | --- | --- |
| Arcee Trinity Large Preview | Arcee AI | [Model card](https://huggingface.co/arcee-ai/Trinity-Large-Preview) | [OpenRouter](https://openrouter.ai/arcee-ai/trinity-large-preview) | Apache-2.0 | General-purpose instruction following; preview checkpoint, replace with final release when available |
| DeepSeek R1 0528 | DeepSeek | [Model card](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) | [OpenRouter](https://openrouter.ai/deepseek/deepseek-r1-0528) | MIT | Reasoning and mathematics |
| DeepSeek V3.2 | DeepSeek | [Model card](https://huggingface.co/deepseek-ai/DeepSeek-V3.2) | [OpenRouter](https://openrouter.ai/deepseek/deepseek-chat-v3.2) | MIT | General-purpose and reasoning |
| GLM-5 | Z.ai | [Model card](https://huggingface.co/zai-org/GLM-5) | [OpenRouter](https://openrouter.ai/z-ai/glm-5) | MIT | General-purpose and tool use |
| GPT-OSS 120B | OpenAI | [Model card](https://huggingface.co/openai/gpt-oss-120b) | [OpenRouter](https://openrouter.ai/openai/gpt-oss-120b) | Apache-2.0 | Reasoning; large deployment |
| Kimi K2.5 | Moonshot AI | [Model card](https://huggingface.co/moonshotai/Kimi-K2.5) | [OpenRouter](https://openrouter.ai/moonshotai/kimi-k2.5) | Modified MIT | Reasoning, coding, multimodal tasks |
| Llama 3.1 405B Instruct | Meta | [Model card](https://huggingface.co/meta-llama/Llama-3.1-405B-Instruct) | [OpenRouter](https://openrouter.ai/meta-llama/llama-3.1-405b-instruct) | Llama 3.1 Community License | Large-scale general-purpose inference |
| Llama 3.3 70B Instruct | Meta | [Model card](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) | [OpenRouter](https://openrouter.ai/meta-llama/llama-3.3-70b-instruct) | Llama 3.3 Community License | General-purpose instruction following; dense 70B |
| Llama 4 Maverick | Meta | [Model card](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct) | [OpenRouter](https://openrouter.ai/meta-llama/llama-4-maverick) | Llama 4 Community License | General-purpose and multimodal |
| MiniMax M2.5 | MiniMax | [Model card](https://huggingface.co/MiniMaxAI/MiniMax-M2.5) | [OpenRouter](https://openrouter.ai/minimax/minimax-m2.5) | MIT (verify) | Reasoning and agentic workflows |
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
| Qwen3 30B-A3B Thinking 2507 | Qwen | [Model card](https://huggingface.co/Qwen/Qwen3-30B-A3B-Thinking-2507) | — | Apache-2.0 | Efficient reasoning |

## Coding and software engineering models

Coding performance depends heavily on whether models receive an agent harness, tools, tests, and multiple attempts. Distinguish code completion from repository-level issue solving.

| Model / checkpoint | Organization | Hugging Face | Hosted inference | License (per model card) | Evaluation focus |
| --- | --- | --- | --- | --- | --- |
| Devstral 2 123B Instruct 2512 | Mistral AI | [Model card](https://huggingface.co/mistralai/Devstral-2-123B-Instruct-2512) | [OpenRouter](https://openrouter.ai/mistralai/devstral-2512) | Apache-2.0 (verify) | Software engineering agents |
| Devstral Small 2 24B Instruct 2512 | Mistral AI | [Model card](https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512) | — | Apache-2.0 (verify) | Smaller coding-agent deployments |
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

## Specialized UI and computer-use models

| Model / checkpoint | Organization | Hugging Face | Hosted inference | License (per model card) | Evaluation focus |
| --- | --- | --- | --- | --- | --- |
| UIGEN-X 32B 0727 | Tesslate | [Model card](https://huggingface.co/Tesslate/UIGEN-X-32B-0727) | — | Apache-2.0 (verify) | UI/code generation |

**Safety note:** Evaluate computer-use agents in sandboxed environments with scoped permissions, human approval for consequential actions, and protections against prompt injection in screenshots and page content.

## Legacy checkpoints

Entries that no longer meet the [inclusion criteria](#inclusion-criteria) but are retained temporarily for readers who already rely on them. Each row names the successor to evaluate instead. Rows in this section are scheduled for removal at a later editorial update.

| Model / checkpoint | Organization | Hugging Face | Hosted inference | License (per model card) | Successor in this list |
| --- | --- | --- | --- | --- | --- |
| Aria | Rhymes AI | [Model card](https://huggingface.co/rhymes-ai/Aria) | — | Apache-2.0 | No direct successor; see current vision and multimodal section |
| Llama 3.2 11B Vision Instruct | Meta | [Model card](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct) | [OpenRouter](https://openrouter.ai/meta-llama/llama-3.2-11b-vision-instruct) | Llama 3.2 Community License | Llama 4 Maverick |
| Llama 3.2 90B Vision Instruct | Meta | [Model card](https://huggingface.co/meta-llama/Llama-3.2-90B-Vision-Instruct) | [OpenRouter](https://openrouter.ai/meta-llama/llama-3.2-90b-vision-instruct) | Llama 3.2 Community License | Llama 4 Maverick |
| Molmo 72B 0924 | Ai2 | [Model card](https://huggingface.co/allenai/Molmo-72B-0924) | — | Apache-2.0 | Molmo2 8B |
| Qwen QwQ 32B | Qwen | [Model card](https://huggingface.co/Qwen/QwQ-32B) | [OpenRouter](https://openrouter.ai/qwen/qwq-32b) | Apache-2.0 | Qwen3 30B-A3B Thinking 2507 |
| UI-TARS 72B DPO | ByteDance Seed | [Model card](https://huggingface.co/ByteDance-Seed/UI-TARS-72B-DPO) | [OpenRouter](https://openrouter.ai/bytedance-research/ui-tars-72b) | Apache-2.0 | Newer UI-TARS releases exist; add the current checkpoint via PR |

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

## Contributing

Model additions and corrections are welcome. In a pull request, please:

1. Link to the **exact, downloadable checkpoint** and its model card (not only an organization homepage). For models published as base and instruct variants, link the variant the row describes.
2. Specify the **model's primary use case** and whether it is general-purpose, coding, multimodal, or specialized; cross-link instead of duplicating rows where possible.
3. Confirm that any hosted inference link points to the **same release and variant** as the checkpoint. If it does not, omit the link rather than adding a caveat.
4. Record the **license named on the model card** in the License column, and note any access restrictions or usage conditions. Do not infer "OSI open source" from public weights alone.
5. Supply **primary-source evaluation evidence** for benchmark claims, with the complete setup described above.
6. Prefer stable names, concise factual descriptions, and neutral classifications over regional or subjective rankings.
7. Run a link checker over the file before submitting; model and provider slugs change frequently.
8. Put notes about *why* a row changed in the pull request description and the [Changelog](#changelog), not in table cells.

This directory is periodically curated; links and deployment terms should be rechecked before making adoption decisions.

## Changelog

- **2026-11-04:** Added License column and inclusion criteria. Moved Aria, Llama 3.2 Vision (11B, 90B), Molmo 72B 0924, QwQ 32B, and UI-TARS 72B DPO to Legacy checkpoints. Moved Llama 3.3 70B Instruct to the general-purpose section. Corrected checkpoint links to match the described variant: Llama 3.1 405B (Instruct), Llama 3.2 Vision (Instruct), Nemotron Ultra 253B (v1 rather than CPT-v1). Corrected hosted links for Nemotron Super 49B (v1.5) and Qwen3 235B-A22B Thinking 2507. Added Kimi K2.5 to the multimodal cross-reference. Removed the previously published benchmark score table because sources and evaluation setups were not consistently documented.
- **Earlier:** Replaced an incorrectly labeled "Qwen3-32B-2507" entry with Qwen3 30B-A3B Thinking 2507. Corrected the Qwen3 VL entry from "32B" to 30B-A3B.
