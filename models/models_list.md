# LLMs:

### Big China - Mostly SoTA for their class

| Model Name        | HF Link | OpenRouter Link | MMLU Pro | SWE-bench | LiveCodeBench |
| :---------------- | :------: | :------: | :-----: | :-----: | :-----: |
| Qwen3-235B (updated)| [Link](https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507)| [Link](https://openrouter.ai/qwen/qwen3-235b-a22b-2507) |  84.5 | | 74.1 |
| Qwen3-Coder | [Link](https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct) | [Link](https://openrouter.ai/qwen/qwen3-coder)| 71.0 | 67.0 | |
| DeepSeek-R1-0528 | [Link](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) | [Link](https://openrouter.ai/deepseek/deepseek-r1-0528)| 84.9 | 41.4 | 78.2 |
| DeepSeek-V3 | [Link](https://huggingface.co/deepseek-ai/DeepSeek-V3) | [Link](https://openrouter.ai/deepseek/deepseek-chat-v3-0324) | 81.9 | 38.8 | 41.0 |
| Kimi K2 | [Link](https://huggingface.co/moonshotai/Kimi-K2-Instruct) | [Link](https://openrouter.ai/moonshotai/kimi-k2) | 81.0 | 65.4 | 55.6 |
| GLM-4.5 | [Link](https://huggingface.co/zai-org/GLM-4.5) | [Link](https://openrouter.ai/z-ai/glm-4.5) | 84.6 | 64.2 | 72.9 | 

---------------------------------
### Little China - Still mostly SoTA for size

| Model Name        | HF Link | OpenRouter Link | MMLU Pro | SWE-bench | LiveCodeBench |
| :---------------- | :------: | :------: | :-----: | :-----: | :-----: |
Qwen3-Coder-30B | [Link](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct) | NA |  | 51.6| |
Qwen3-32B | [Link](https://huggingface.co/Qwen/Qwen3-32B) | [Link](https://openrouter.ai/qwen/qwen3-32b) | 79.8 | | 54.6 | 
Kimi-Dev-72B | [Link](https://huggingface.co/moonshotai/Kimi-Dev-72B) | [Link](https://openrouter.ai/moonshotai/kimi-dev-72b) * | | 60.4 | |
Qwen-QwQ | [Link](https://huggingface.co/Qwen/QwQ-32B) | [Link](https://openrouter.ai/qwen/qwq-32b) | 69.1 | | 63.1 | 
GLM-4.5-Air | [Link](https://huggingface.co/zai-org/GLM-4.5-Air) | [Link](https://openrouter.ai/z-ai/glm-4.5-air) | 81.4 | 57.6 | 70.7 |

--------------------------------
### Not China - Larger

| Model Name        | HF Link | OpenRouter Link | MMLU Pro | SWE-bench | LiveCodeBench |
| :---------------- | :------: | :------: | :-----: | :-----: | :-----: |
| Nvidia-nemotron ‘Ultra’ | [Link](https://huggingface.co/nvidia/Llama-3_1-Nemotron-Ultra-253B-CPT-v1) | [Link](https://openrouter.ai/nvidia/llama-3.1-nemotron-ultra-253b-v1) | 82.5 | | 64.1 |
| Llama4-Maverick | [Link](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct) | [Link](https://openrouter.ai/meta-llama/llama-4-maverick) | 80.9 | | 39.7 |
| Llama4-Scout | [Link](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct) | [Link](https://openrouter.ai/meta-llama/llama-4-scout) | 74.3 | | 29.9 | 
| Llama3.1-405B | [Link](https://huggingface.co/meta-llama/Llama-3.1-405B) | [Link](https://openrouter.ai/meta-llama/llama-3.1-405b-instruct) | 73.3 | | 30.5 | 
| GPT-OSS-120B | [Link](https://huggingface.co/openai/gpt-oss-120b) | [Link](https://openrouter.ai/openai/gpt-oss-120b) | 80.8 | 47.9/62.4 | 63.9 |

---------------------------------
### Not China - Smaller

| Model Name        | HF Link | OpenRouter Link | MMLU Pro | SWE-bench | LiveCodeBench |
| :---------------- | :------: | :------: | :-----: | :-----: | :-----: |
| Nemotron ‘Super’ | [Link](https://huggingface.co/nvidia/Llama-3_3-Nemotron-Super-49B-v1_5) | [Link](https://openrouter.ai/nvidia/llama-3.3-nemotron-super-49b-v1) | 81.4 | | 73.7 |
| Llama3.3-70B | [Link](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) | [Link](https://openrouter.ai/meta-llama/llama-3.3-70b-instruct) | 65.9 | | 28.8 |
| Gemma 3-27B | [Link](https://huggingface.co/google/gemma-2-27b-it) | [Link](https://openrouter.ai/google/gemma-3-27b-it) | 67.5 | | 13.7 |
| Devstral-24B-2507 | [Link](https://huggingface.co/mistralai/Devstral-Small-2507) | [Link](https://openrouter.ai/mistralai/devstral-small) | 62.2 | 53.6 | 25.4 | 
| Magistral-24B-2506 | [Link](https://huggingface.co/mistralai/Magistral-Small-2506) | [Link](https://openrouter.ai/mistralai/magistral-small-2506) | 74.6 | | 55.8 | 
| GPT-OSS-20B | [Link](https://huggingface.co/openai/gpt-oss-20b) | [Link](https://openrouter.ai/openai/gpt-oss-20b) | 73.1 | 37.4/60.7 | 72.1 |
| Reason-Nemo *(chinese base) | [Link](https://huggingface.co/nvidia/OpenReasoning-Nemotron-32B) | NA |

-------------------------------

## With Vision:

### Chinese:
| Model Name        | HF Link | OpenRouter Link |
| :---------------- | :------: | :------: |
| GLM-4.5V | [Link](https://huggingface.co/zai-org/GLM-4.5V) | [Link](https://openrouter.ai/z-ai/glm-4.5v) |
| Qwen2.5-VL-32B | [Link](https://huggingface.co/Qwen/Qwen2.5-VL-32B-Instruct) | [Link](https://openrouter.ai/qwen/qwen2.5-vl-32b-instruct) |
| Qwen2.5-VL-72B | [Link](https://huggingface.co/Qwen/Qwen2.5-VL-72B-Instruct) | [Link](https://openrouter.ai/qwen/qwen2.5-vl-72b-instruct) |
| Qwen-Image | [Link](https://huggingface.co/Qwen/Qwen-Image) | NA |

----------------------------

### Not Chinese:
| Model Name        | HF Link | OpenRouter Link |
| :---------------- | :------: | :------: |
| (Llama4, Gemma 3 from above) |
| Molmo-7B | [Link](https://huggingface.co/allenai/Molmo-7B-D-0924) | [Link](https://openrouter.ai/allenai/molmo-7b-d) |
| Molmo-72B | [Link](https://huggingface.co/allenai/Molmo-72B-0924) | NA |
| Aria | [Link](https://huggingface.co/rhymes-ai/Aria) | NA |
| Mistral Small-3.2 | [Link](https://huggingface.co/mistralai/Mistral-Small-3.2-24B-Instruct-2506) | [Link](https://openrouter.ai/mistralai/mistral-small-3.2-24b-instruct) |
| Llama 3.2 11B | [Link](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision) | [Link](https://openrouter.ai/meta-llama/llama-3.2-11b-vision-instruct) | 
| Llama 3.2 90B | [Link](https://huggingface.co/meta-llama/Llama-3.2-90B-Vision) | [Link](https://openrouter.ai/meta-llama/llama-3.2-90b-vision-instruct) | 

-----------------------------

## Other:
| Model Name        | HF Link | OpenRouter Link |
| :---------------- | :------: | :------: |
| UIGen-32B | [Link](https://huggingface.co/Tesslate/UIGEN-X-32B-0727) | NA |
| UI-TARS 72B | [Link](https://huggingface.co/ByteDance-Seed/UI-TARS-72B-DPO) | [Link](https://openrouter.ai/bytedance-research/ui-tars-72b) |