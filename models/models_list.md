# LLMs:

### Big China - Mostly SoTA for their class

| Model Name        | HF Link | OpenRouter Link | MMLU Pro | SWE-bench | HLE | GPQA Diamond |
| :---------------- | :------: | :------: | :-----: | :-----: | :-----: | :-----: |
| Qwen3-235B-2507| [Link](https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507)| [Link](https://openrouter.ai/qwen/qwen3-235b-a22b-2507) |  84.5 | 34.4 | 15.0 | 79.0 |
| Qwen3.5-397B | [Link](https://huggingface.co/Qwen/Qwen3.5-397B-A17B)| [Link](https://openrouter.ai/qwen/qwen3.5-397b-a17b) | 88.5 | 76.4 | 27.3 | 88.4 |
| DeepSeek-R1-0528 | [Link](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) | [Link](https://openrouter.ai/deepseek/deepseek-r1-0528)| 84.9 | 41.4 |  | 81.3 |
| DeepSeek-V3.2 | [Link](https://huggingface.co/deepseek-ai/DeepSeek-V3.2) | [Link](https://openrouter.ai/deepseek/deepseek-chat-v3.2) | 81.9 | 73.1 | 22.2 | 82.4
| Kimi K2.5 | [Link](https://huggingface.co/moonshotai/Kimi-K2.5) | [Link](https://openrouter.ai/moonshotai/kimi-k2.5) | 87.1 | 76.8 | 29.4 | 87.6 |
| GLM-5 | [Link](https://huggingface.co/zai-org/GLM-5) | [Link](https://openrouter.ai/z-ai/glm-5) | 86 | 77.8 | 27.2 | 86.0 |
| MiniMax M2.5 | [Link](https://huggingface.co/MiniMaxAI/MiniMax-M2.5) | [Link](https://openrouter.ai/minimax/minimax-m2.5) |  80.1 | 80.2 | 19.1 | 85.0 |


---------------------------------
### Little China - Still mostly SoTA for size

| Model Name        | HF Link | OpenRouter Link | MMLU Pro | SWE-bench | LiveCodeBench | GPQA Diamond |
| :---------------- | :------: | :------: | :-----: | :-----: | :-----: | :-----: |
| Qwen3-Coder-30B | [Link](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct) | NA | 70.6 | 51.6| 40.3 | 51.6|
| Qwen3-32B-2507 | [Link](https://huggingface.co/Qwen/Qwen3-30B-A3B-Thinking-2507) | [Link](https://openrouter.ai/qwen/qwen3-32b) | 78.5 | | 66 | 73.4
| Kimi-Dev-72B | [Link](https://huggingface.co/moonshotai/Kimi-Dev-72B) | [Link](https://openrouter.ai/moonshotai/kimi-dev-72b) * | | 60.4 | |  |
| Qwen-QwQ | [Link](https://huggingface.co/Qwen/QwQ-32B) | [Link](https://openrouter.ai/qwen/qwq-32b) | 69.1 | | 63.1 | 59.3 |
| GLM-4.7-Flash | [Link](https://huggingface.co/zai-org/GLM-4.7-Flash) | [Link](https://openrouter.ai/z-ai/glm-4.7-flash) |  | 59.2 |  | 58 |
| Qwen3 Coder Next | [Link](https://huggingface.co/Qwen/Qwen3-Coder-Next) | [Link](https://openrouter.ai/qwen/qwen3-coder-next) |  | 70.6| 60.66 | 74 | 


--------------------------------
### Not China - Larger

| Model Name        | HF Link | OpenRouter Link | MMLU Pro | SWE-bench | LiveCodeBench | GPQA Diamond |
| :---------------- | :------: | :------: | :-----: | :-----: | :-----: | :-----: |
| Nvidia-nemotron ‘Ultra’ | [Link](https://huggingface.co/nvidia/Llama-3_1-Nemotron-Ultra-253B-CPT-v1) | [Link](https://openrouter.ai/nvidia/llama-3.1-nemotron-ultra-253b-v1) | 82.5 | | 64.1 | 72.8 |
| Llama4-Maverick | [Link](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct) | [Link](https://openrouter.ai/meta-llama/llama-4-maverick) | 80.9 | | 39.7 | 67.1 |
| Llama3.1-405B | [Link](https://huggingface.co/meta-llama/Llama-3.1-405B) | [Link](https://openrouter.ai/meta-llama/llama-3.1-405b-instruct) | 73.3 | | 30.5 | 51.5 |
| GPT-OSS-120B | [Link](https://huggingface.co/openai/gpt-oss-120b) | [Link](https://openrouter.ai/openai/gpt-oss-120b) | 80.8 | 47.9/62.4 | 63.9 | 78.2 |
| Mistral-Large-3 | [Link](https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512) | [Link](https://openrouter.ai/mistralai/mistral-large-2512) | 79.8 | 36.2 | 55.3 | 43.9 |
| Devstral-2-123B | [Link](https://huggingface.co/mistralai/Devstral-2-123B-Instruct-2512) | [Link](https://openrouter.ai/mistralai/devstral-2512) | 76.2 | 72.2 | 66.8 | 59 |
| Arcee-Trinity-Large | [Link](https://huggingface.co/arcee-ai/Trinity-Large-Preview) | [Link](https://openrouter.ai/arcee-ai/trinity-large-preview) | 75.2 | | 65.7 | 63.3 |

---------------------------------
### Not China - Smaller

| Model Name        | HF Link | OpenRouter Link | MMLU Pro | SWE-bench | LiveCodeBench | GPQA Diamond |
| :---------------- | :------: | :------: | :-----: | :-----: | :-----: | :-----: |
| Nemotron ‘Super’ | [Link](https://huggingface.co/nvidia/Llama-3_3-Nemotron-Super-49B-v1_5) | [Link](https://openrouter.ai/nvidia/llama-3.3-nemotron-super-49b-v1) | 81.4 | | 73.7 | 74.8 |
| Nemotron 3 Nano | [Link](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16) | [Link](https://openrouter.ai/nvidia/nemotron-3-nano-30b-a3b) | 78.3 | 38.8 | 68.3 | 73 |
| Llama3.3-70B | [Link](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) | [Link](https://openrouter.ai/meta-llama/llama-3.3-70b-instruct) | 65.9 | | 28.8 | 49.8 |
| Gemma 3-27B | [Link](https://huggingface.co/google/gemma-2-27b-it) | [Link](https://openrouter.ai/google/gemma-3-27b-it) | 67.5 | | 13.7 | 42.8 |
| Devstral-Small-2 | [Link](https://huggingface.co/mistralai/Devstral-Small-2-24B-Instruct-2512) | NA |  | 68.0 | 45 | 59 |
| Magistral-24B-2506 | [Link](https://huggingface.co/mistralai/Magistral-Small-2506) | [Link](https://openrouter.ai/mistralai/magistral-small-2506) | 74.6 | | 55.8 | 64.1
| GPT-OSS-20B | [Link](https://huggingface.co/openai/gpt-oss-20b) | [Link](https://openrouter.ai/openai/gpt-oss-20b) | 73.1 | 37.4/60.7 | 72.1 | 61.7
| Olmo 3.1 32B | [Link](https://huggingface.co/allenai/Olmo-3.1-32B-Instruct) | [Link](https://openrouter.ai/allenai/olmo-3.1-32b-instruct) | 80.9 | | 54.7 | 48.6 |

-------------------------------

## With Vision Focus:

### Chinese:
| Model Name        | HF Link | OpenRouter Link |
| :---------------- | :------: | :------: |
| GLM-4.6V | [Link](https://huggingface.co/zai-org/GLM-4.6V) | [Link](https://openrouter.ai/z-ai/glm-4.6v) |
| Qwen3-VL-32B | [Link](https://huggingface.co/Qwen/Qwen3-VL-30B-A3B-Instruct) | [Link](https://openrouter.ai/qwen/qwen3-vl-30b-a3b-instruct) |
| Qwen2.5-VL-72B | [Link](https://huggingface.co/Qwen/Qwen2.5-VL-72B-Instruct) | [Link](https://openrouter.ai/qwen/qwen2.5-vl-72b-instruct) |

----------------------------

### Not Chinese:
| Model Name        | HF Link | OpenRouter Link |
| :---------------- | :------: | :------: |
| (Llama4, Gemma 3 from above) |
| Molmo2-8B | [Link](https://huggingface.co/allenai/Molmo2-8B) | [Link](https://openrouter.ai/allenai/molmo-2-8b) |
| Molmo-72B | [Link](https://huggingface.co/allenai/Molmo-72B-0924) | NA |
| Aria | [Link](https://huggingface.co/rhymes-ai/Aria) | NA |
| Mistral Small-3.2 | [Link](https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506) | [Link](https://openrouter.ai/mistralai/mistral-small-3.2-24b-instruct) |
| Llama 3.2 11B | [Link](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision) | [Link](https://openrouter.ai/meta-llama/llama-3.2-11b-vision-instruct) | 
| Llama 3.2 90B | [Link](https://huggingface.co/meta-llama/Llama-3.2-90B-Vision) | [Link](https://openrouter.ai/meta-llama/llama-3.2-90b-vision-instruct) |
| Ministral 3 14B | [Link](https://openrouter.ai/mistralai/ministral-14b-2512) | [Link](https://huggingface.co/mistralai/Ministral-3-14B-Instruct-2512) |

-----------------------------

## Other:
| Model Name        | HF Link | OpenRouter Link |
| :---------------- | :------: | :------: |
| UIGen-32B | [Link](https://huggingface.co/Tesslate/UIGEN-X-32B-0727) | NA |
| UI-TARS 72B | [Link](https://huggingface.co/ByteDance-Seed/UI-TARS-72B-DPO) | [Link](https://openrouter.ai/bytedance-research/ui-tars-72b) |