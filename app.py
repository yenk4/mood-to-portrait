"""Mood to Portrait — Gradio app.

User answers 5 poetic questions → Python builds a FLUX prompt → portrait is generated.
HF_TOKEN must be set as an environment variable (or Space secret).
"""

import os
import gradio as gr
from huggingface_hub import InferenceClient
from prompt_builder import build_prompt

HF_TOKEN = os.environ.get("HF_TOKEN")
MODEL = "black-forest-labs/FLUX.1-schnell"

TITLE = "🔮 MOOD TO PORTRAIT 🔮"
DESCRIPTION = """
*Answer five questions about your inner state. Python will translate your mood into a FLUX image prompt and paint your portrait.*

Built by [Yana Makovskaya](https://yenka.dev) — Senior ML/AI Engineer specializing in generative AI.
"""

WEATHER_OPTIONS = ["Stormy", "Foggy", "Sunny", "Rainy", "Blizzard"]
ANIMAL_OPTIONS = ["Wolf", "Cat", "Deer", "Raven", "Fox", "Owl"]
COLOR_OPTIONS = ["Deep blue", "Crimson", "Violet", "Gold", "Silver", "Forest green"]
ELEMENT_OPTIONS = ["Fire", "Water", "Earth", "Air", "Void"]
LANDSCAPE_OPTIONS = ["Ocean", "Forest", "Desert", "City", "Mountain", "Cave"]


def generate_portrait(weather, animal, color, element, landscape):
    if not all([weather, animal, color, element, landscape]):
        return None, "Please answer all five questions."

    prompt = build_prompt(weather, animal, color, element, landscape)

    if not HF_TOKEN:
        return None, f"⚠️ HF_TOKEN not set. Your portrait prompt would be:\n\n`{prompt}`"

    try:
        client = InferenceClient(model=MODEL, token=HF_TOKEN)
        image = client.text_to_image(prompt)
        return image, f"**Assembled prompt:**\n\n`{prompt}`"
    except Exception as e:
        return None, f"Generation failed: {e}\n\n**Prompt was:**\n`{prompt}`"


with gr.Blocks(theme=gr.themes.Default(primary_hue="purple", neutral_hue="gray"), title=TITLE) as demo:
    gr.Markdown(f"# {TITLE}")
    gr.Markdown(DESCRIPTION)

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 🔮 Tell me about your mood")

            weather = gr.Dropdown(
                choices=WEATHER_OPTIONS,
                label="If your mood were weather right now, it would be...",
                info="Choose what resonates most",
            )
            animal = gr.Dropdown(
                choices=ANIMAL_OPTIONS,
                label="What animal matches your energy today?",
                info="Think about how you move through the world right now",
            )
            color = gr.Dropdown(
                choices=COLOR_OPTIONS,
                label="A color that speaks to you in this moment",
                info="Go with your gut",
            )
            element = gr.Dropdown(
                choices=ELEMENT_OPTIONS,
                label="Which element calls to you?",
                info="What forces feel alive in you",
            )
            landscape = gr.Dropdown(
                choices=LANDSCAPE_OPTIONS,
                label="Your inner landscape right now is...",
                info="Where does your mind wander",
            )

            btn = gr.Button("🔮 Paint my portrait", variant="primary", size="lg")

        with gr.Column(scale=1):
            gr.Markdown("### 🔮 Your portrait")
            output_image = gr.Image(label="Generated portrait", show_label=False)
            output_prompt = gr.Markdown()

    btn.click(
        fn=generate_portrait,
        inputs=[weather, animal, color, element, landscape],
        outputs=[output_image, output_prompt],
    )

    gr.Markdown(
        "---\n*Powered by FLUX.1-schnell via HuggingFace Inference API · "
        "Prompt engineering by [yenka.dev](https://yenka.dev)*"
    )

if __name__ == "__main__":
    demo.launch()
