---
title: Mood To Portrait
emoji: 🔮
colorFrom: purple
colorTo: pink
sdk: gradio
sdk_version: "4"
app_file: app.py
pinned: false
---

# 🔮 Mood to Portrait

**Answer 5 poetic questions → Python builds a FLUX prompt → your portrait is generated.**

A small creative demo showing prompt engineering + HuggingFace Inference API integration.

## How it works

1. You answer 5 questions about your current mood (weather, animal, color, element, inner landscape)
2. `prompt_builder.py` maps each answer to descriptive visual art terms
3. The assembled prompt goes to **FLUX.1-schnell** via HuggingFace Inference API
4. Your portrait appears

**Example assembled prompt:**
```
a dramatic fantasy portrait, mysterious graceful cat energy, ethereal misty atmosphere,
purple violet haze palette, lush dense forest background, fluid flowing water energy,
cinematic lighting, painterly style, high detail, fantasy art
```

## Tech stack

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Gradio](https://img.shields.io/badge/Gradio-UI-orange)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FLUX.1--schnell-yellow)

- **UI**: Gradio
- **Model**: FLUX.1-schnell (via HF Inference API free tier)
- **Hosting**: HuggingFace Spaces (free)
- **Auth**: `HF_TOKEN` environment variable / Space secret

## Run locally

```bash
uv run app.py
```

Or with plain Python:

```bash
pip install -r requirements.txt
HF_TOKEN=your_token python app.py
```

## Project structure

```
mood-to-portrait/
├── app.py             # Gradio UI + inference call
├── prompt_builder.py  # Maps answers → FLUX prompt
├── requirements.txt   # gradio, huggingface_hub, Pillow
└── README.md
```

---

Built by [Yana Makovskaya](https://yenka.dev) · Senior ML/AI Engineer · Generative AI
