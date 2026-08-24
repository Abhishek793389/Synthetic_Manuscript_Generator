from pathlib import Path
import random

from src.text_loader import load_text, get_random_chunk
from src.background import create_aged_paper
from src.renderer import render_text
from src.annotation import save_annotation
from src.effects import apply_manuscript_effects


BASE_DIR = Path(__file__).resolve().parent

OUTPUT_DIR = BASE_DIR / "output" / "dataset"


SCRIPTS = {
    "sharada": {
        "input": BASE_DIR / "input" / "sharada.md",
        "font": BASE_DIR / "fonts" / "sharada" / "NotoSansSharada-Regular.ttf",
    },

    "devanagari": {
        "input": BASE_DIR / "input" / "devanagari.md",
        "font": BASE_DIR / "fonts" / "devanagari" / "NotoSansDevanagari-Regular.ttf",
    },

    "modi": {
        "input": BASE_DIR / "input" / "modi.md",
        "font": BASE_DIR / "fonts" / "modi" / "NotoSansModi-Regular.ttf",
    },
}


SPLITS = {
    "train": 85,
    "validation": 10,
    "test": 5,
}

def generate_image(text,image_number,script,split,font_path,seed,):
    output_dir = OUTPUT_DIR / script / split

    output_dir.mkdir(parents=True,exist_ok=True,)

    image_file = (output_dir/ f"{script}_{image_number:04d}.png")

    annotation_file = (output_dir/ f"{script}_{image_number:04d}.md")

    image = create_aged_paper(
        width=1600,
        height=1200,
        seed=seed,)

    boxes = render_text(
        image=image,
        text=text,
        font_path=font_path,
        font_size=46,
        margin=140,
        seed=seed,)

    image = apply_manuscript_effects(
        image=image,
        seed=seed + 1000,)

    image.save(
        image_file,
        quality=95,
)

    save_annotation(
        path=annotation_file,
        script=script.capitalize(),
        material="Aged Handmade Paper",
        source_text=text,
        bounding_boxes=boxes,)


def generate_script(
    script,
    config,
    global_seed=42,):

    input_file = config["input"]
    font_path = config["font"]

    if not input_file.exists():
        raise FileNotFoundError(
            f"Input file not found:\n{input_file}")


    if not font_path.exists():
        raise FileNotFoundError(
            f"Font not found:\n{font_path}")

    text = load_text(input_file)

    if len(text) < 300:
        raise ValueError(
            f"{script}: input text is too short.")

    rng = random.Random(global_seed)

    image_number = 1

    for split, count in SPLITS.items():
        print()
        print(
            f"Generating {count} "
            f"{split} images..."
        )

        for _ in range(count):

            seed = rng.randint(
                1,
                1_000_000_000,)

            chunk = get_random_chunk(
                text,
                min_chars=250,
                max_chars=600,
                seed=seed,)

            generate_image(
                text=chunk,
                image_number=image_number,
                script=script,
                split=split,
                font_path=font_path,
                seed=seed,)

            image_number += 1

def main():

    for index, (script,config) in enumerate(
        SCRIPTS.items()):

        generate_script(
            script=script,
            config=config,
            global_seed=42 + (
                index * 10000),)

    for script in SCRIPTS:
        print(
            f"  {script:12} : 100")


if __name__ == "__main__":
    main()