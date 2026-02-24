---
title: Metaphoric Oracle
emoji: ✨
colorFrom: purple
colorTo: pink
sdk: gradio
sdk_version: "5.9.1"
python_version: "3.11"
app_file: app.py
pinned: false
---

# ✨ Metaphoric Oracle

**Answer 5 tarot-inspired questions → LLM generates wise life advice → FLUX paints your metaphoric card.**

A creative demo combining LLM text generation + image generation with HuggingFace Inference API.

## How it works

1. You answer 5 questions about your inner state (area of life, current energy, what you need, a symbol, an honest truth)
2. `prompt_builder.py` maps answers to visual imagery for a metaphoric card
3. **Llama-3.1-8B-Instruct** generates 4–5 sentences of wise, empowering life advice grounded in your answers
4. **FLUX.1-schnell** generates a tarot-style card illustration
5. Both appear together as your personal reading

The oracle never predicts the future as good or bad — only empowering, actionable guidance.

**Example image prompt:**
```
a mystical metaphoric card illustration, art nouveau style,
a blooming lotus rising from dark water, a chrysalis cracking open with golden light,
a lone flame burning in the dark, a full silver moon casting mystical shadows,
chains dissolving into luminous dust,
intricate ornate border with golden filigree and esoteric symbols,
jewel tones — purple violet teal gold, ethereal atmosphere,
highly detailed spiritual illustration, tarot card format, masterpiece
```

## Tech stack

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Gradio](https://img.shields.io/badge/Gradio-UI-orange)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FLUX%20%2B%20Llama-yellow)

- **UI**: Gradio
- **Image model**: FLUX.1-schnell (via HF Inference API)
- **Text model**: Llama-3.1-8B-Instruct (via HF Inference API)
- **Hosting**: HuggingFace Spaces (free)
- **Auth**: `HF_TOKEN` environment variable / Space secret

## Run locally

```bash
uv run python app.py
```

Or with plain Python:

```bash
pip install -r requirements.txt
HF_TOKEN=your_token python app.py
```

## Project structure

```
mood-to-portrait/
├── app.py             # Gradio UI + inference calls (LLM + image)
├── prompt_builder.py  # Maps oracle answers → FLUX prompt
├── requirements.txt   # gradio, huggingface_hub, Pillow
└── README.md
```

---

Built by [Yana Makovskaya](https://yenka.dev) · Senior ML/AI Engineer · Generative AI
