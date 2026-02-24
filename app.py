"""Metaphoric Oracle — Gradio app.

User answers 5 tarot-inspired questions → LLM generates wise life advice →
FLUX generates a metaphoric card image visualizing that advice.
HF_TOKEN must be set as an environment variable (or Space secret).
"""

import os
import gradio as gr
from huggingface_hub import InferenceClient
from prompt_builder import build_prompt

HF_TOKEN = os.environ.get("HF_TOKEN")
IMAGE_MODEL = "black-forest-labs/FLUX.1-schnell"
TEXT_MODEL = "meta-llama/Llama-3.1-8B-Instruct"

TITLE = "✨ METAPHORIC ORACLE ✨"
DESCRIPTION = """
*Answer five questions. Receive a personal reading — wise life guidance and a metaphoric card painted just for you.*

Built by [yenka.dev](https://yenka.dev)
"""

SPHERE_OPTIONS = [
    "Love & Relationships",
    "Career & Purpose",
    "Inner Growth",
    "Health & Body",
    "Finances & Abundance",
    "Spirituality & Soul",
]
ENERGY_OPTIONS = ["Confusion", "Stagnation", "Transformation", "Hope", "Fear", "Restlessness"]
NEED_OPTIONS = ["Clarity", "Courage", "Acceptance", "Direction", "Healing", "Perspective"]
SYMBOL_OPTIONS = ["The Moon", "The Mirror", "A Key", "Flowing Water", "A Flame", "Ancient Roots"]
TRUTH_OPTIONS = [
    "I need to let go of something",
    "I need to take action",
    "I'm harder on myself than I should be",
    "I already know the answer",
    "I need to ask for help",
    "I need to rest",
]

SYSTEM_PROMPT = """You are a wise, warm life advisor who speaks in metaphoric, poetic language.
Your role is to give empowering, actionable life guidance based on the person's answers.
Never predict the future as good or bad. Never use fortune-telling language.
Give 4-5 sentences of empowering advice grounded specifically in their answers.
End with one short, powerful guiding sentence on its own line.
Be specific to the answers, not generic."""


def generate_reading(sphere, energy, need, symbol, truth):
    if not all([sphere, energy, need, symbol, truth]):
        return None, "Please answer all five questions."

    user_message = (
        f"My reading:\n"
        f"- Area calling for attention: {sphere}\n"
        f"- Energy I'm moving through: {energy}\n"
        f"- What I most need: {need}\n"
        f"- Symbol that speaks to me: {symbol}\n"
        f"- Honest truth I've been avoiding: {truth}\n\n"
        f"Please give me your wise guidance."
    )

    image_prompt = build_prompt(sphere, energy, need, symbol, truth)

    if not HF_TOKEN:
        preview = (
            f"⚠️ HF_TOKEN not set.\n\n"
            f"**Image prompt would be:**\n`{image_prompt}`\n\n"
            f"**LLM would receive:**\n{user_message}"
        )
        return None, preview

    try:
        client = InferenceClient(token=HF_TOKEN)

        response = client.chat_completion(
            model=TEXT_MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message},
            ],
            max_tokens=300,
        )
        advice_text = response.choices[0].message.content.strip()

        image = client.text_to_image(image_prompt, model=IMAGE_MODEL)

        return image, advice_text

    except Exception as e:
        return None, f"Generation failed: {e}\n\n**Image prompt was:**\n`{image_prompt}`"


with gr.Blocks(title=TITLE) as demo:
    gr.Markdown(f"# {TITLE}")
    gr.Markdown(DESCRIPTION)

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### Your reading")

            sphere = gr.Dropdown(
                choices=SPHERE_OPTIONS,
                label="Which area of your life is calling for attention?",
            )
            energy = gr.Dropdown(
                choices=ENERGY_OPTIONS,
                label="What energy are you moving through right now?",
            )
            need = gr.Dropdown(
                choices=NEED_OPTIONS,
                label="What do you most need right now?",
            )
            symbol = gr.Dropdown(
                choices=SYMBOL_OPTIONS,
                label="Which symbol speaks to you today?",
            )
            truth = gr.Dropdown(
                choices=TRUTH_OPTIONS,
                label="What is the honest truth you've been avoiding?",
            )

            btn = gr.Button("✨ Reveal my oracle", variant="primary", size="lg")

        with gr.Column(scale=1):
            gr.Markdown("### Your card")
            output_image = gr.Image(label="Metaphoric card", show_label=False)
            gr.Markdown("### Your guidance")
            output_text = gr.Markdown()

    btn.click(
        fn=generate_reading,
        inputs=[sphere, energy, need, symbol, truth],
        outputs=[output_image, output_text],
        api_name=False,
    )

    gr.Markdown(
        "---\n*Powered by FLUX.1-schnell + Llama-3.1-8B via HuggingFace Inference API · "
        "Built by [yenka.dev](https://yenka.dev)*"
    )

if __name__ == "__main__":
    demo.launch(theme=gr.themes.Default(primary_hue="purple", neutral_hue="slate"))
