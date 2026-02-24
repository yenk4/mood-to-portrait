"""Maps oracle answers to a FLUX image prompt for the Metaphoric Oracle."""

SPHERE_MAP = {
    "Love & Relationships": "two intertwined figures in cosmic embrace",
    "Career & Purpose": "a luminous path ascending through mist",
    "Inner Growth": "a blooming lotus rising from dark water",
    "Health & Body": "a radiant human silhouette filled with light",
    "Finances & Abundance": "a tree heavy with golden fruit",
    "Spirituality & Soul": "an ethereal figure reaching toward stars",
}

ENERGY_MAP = {
    "Confusion": "swirling fog and scattered light fragments",
    "Stagnation": "still dark water reflecting a distant glow",
    "Transformation": "a chrysalis cracking open with golden light",
    "Hope": "dawn breaking over a deep violet horizon",
    "Fear": "shadows dissolving at the edge of candlelight",
    "Restlessness": "wind-swept leaves spiraling upward",
}

NEED_MAP = {
    "Clarity": "a clear crystal orb revealing hidden truths",
    "Courage": "a lone flame burning in the dark",
    "Acceptance": "open hands releasing birds into the sky",
    "Direction": "a glowing compass rose on ancient parchment",
    "Healing": "soft golden light pouring through a wound",
    "Perspective": "a figure standing atop a mountain seeing all",
}

SYMBOL_MAP = {
    "The Moon": "a full silver moon casting mystical shadows",
    "The Mirror": "an ornate mirror reflecting inner light",
    "A Key": "an ancient golden key floating in mist",
    "Flowing Water": "a sacred river winding through sacred stones",
    "A Flame": "an eternal flame at the center of all things",
    "Ancient Roots": "deep intertwined roots glowing beneath the earth",
}

TRUTH_MAP = {
    "I need to let go of something": "chains dissolving into luminous dust",
    "I need to take action": "a hand reaching forward through darkness toward light",
    "I'm harder on myself than I should be": "a gentle embrace surrounding a wounded heart",
    "I already know the answer": "an inner light illuminating from within",
    "I need to ask for help": "hands reaching toward each other across a void",
    "I need to rest": "a figure resting peacefully under a canopy of stars",
}


def build_prompt(sphere: str, energy: str, need: str, symbol: str, truth: str) -> str:
    sphere_img = SPHERE_MAP.get(sphere, "a radiant figure")
    energy_img = ENERGY_MAP.get(energy, "swirling ethereal energy")
    symbol_img = SYMBOL_MAP.get(symbol, "a mystical symbol")
    truth_img = TRUTH_MAP.get(truth, "hidden truth revealed")

    prompt = (
        f"a mystical metaphoric card illustration, art nouveau style, "
        f"{sphere_img}, {energy_img}, {symbol_img}, {truth_img}, "
        f"intricate ornate border with golden filigree and esoteric symbols, "
        f"jewel tones — purple violet teal gold, ethereal atmosphere, "
        f"highly detailed spiritual illustration, tarot card format, masterpiece"
    )
    return prompt
