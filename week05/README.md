# Week 05 - LLM Prompt Engineering & Agentic Workflows

This project covers prompt engineering techniques, LLM validation loops, and agentic workflows using Ollama.

## Structure

- `phase01/` - Basic LLM classification (rule-based vs LLM)
- `phase02/` - Prompt engineering (concise vs noisy, zero-shot vs few-shot)
- `phase03/` - Temperature, determinism, and tokenization
- `phase04/` - Structured output with JSON mode
- `phase05/` - Validation loops, retry patterns, and state machines
- `phase06/` - Tool use and agentic workflows
- `evidence/` - Lab outputs

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install ollama
```

## Requirements

- Ollama installed locally
- Model: `qwen2.5:7b` (pull with `ollama pull qwen2.5:7b`)

## Running Examples

```bash
python phase01/demo.py
python phase02/demo_2.py
python phase03/demo_3.py
python phase04/demo_5.py
python phase05/demo_2_2.py
python phase06/demo_6_1.py
```