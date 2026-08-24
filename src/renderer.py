from pathlib import Path
import random

from PIL import Image, ImageDraw, ImageFont, ImageFilter


def _ink():
    return random.choice([
        (42, 32, 23),
        (48, 35, 24),
        (55, 39, 25),
        (62, 44, 27),
        (70, 49, 29),
        (78, 55, 32),])

def _draw_highlight(
    image,
    box,):

    layer = Image.new(
        "RGBA",
        image.size,
        (0, 0, 0, 0),)

    draw = ImageDraw.Draw(layer)
    x1, y1, x2, y2 = box
    draw.rounded_rectangle(
        (
            x1 - 8,
            y1 - 5,
            x2 + 8,
            y2 + 5,),
        radius=5,
        fill=(145, 105, 45, 45),)

    layer = layer.filter(
        ImageFilter.GaussianBlur(2))

    image.paste(
        layer,
        (0, 0),
        layer,)


def _render_line(
    image,
    text,
    font,
    x,
    y,
    boxes,
    text_type="main_text",
    highlight=False,):

    draw = ImageDraw.Draw(image)

    jitter_x = random.randint(-4, 4)
    jitter_y = random.randint(-3, 3)

    draw_x = x + jitter_x
    draw_y = y + jitter_y

    ink_variants = [
        (42, 32, 23),
        (48, 35, 24),
        (55, 39, 25),
        (62, 44, 27),
        (70, 49, 29),
        (78, 55, 32),
    ]

    color = random.choice(ink_variants)

    bbox = draw.textbbox(
        (draw_x, draw_y),
        text,
        font=font,
    )

    if highlight:
        _draw_highlight(image,bbox,)

    draw = ImageDraw.Draw(image)

    draw.text(
        (draw_x, draw_y),
        text,
        font=font,
        fill=color,)

    boxes.append({
        "text": text,
        "bbox": [
            bbox[0],
            bbox[1],
            bbox[2],
            bbox[3],
        ],
        "type": text_type,})


    if random.random() < 0.22:
        layer = Image.new(
            "RGBA",
            image.size,
            (0, 0, 0, 0),)

        bleed_draw = ImageDraw.Draw(layer)
        bleed_draw.text(
            (
                draw_x + random.choice([-1, 0, 1]),
                draw_y + random.choice([-1, 0, 1]),
            ),
            text,
            font=font,
            fill=(
                color[0],
                color[1],
                color[2],
                random.randint(12, 30),
            ),
        )

        layer = layer.filter(
            ImageFilter.GaussianBlur(1.0)
        )

        image.paste(
            layer,
            (0, 0),
            layer,
        )

    return bbox


def _wrap_text(
    draw,
    text,
    font,
    max_width,):

    words = text.split()

    lines = []
    current = ""

    for word in words:

        candidate = (
            f"{current} {word}".strip())

        bbox = draw.textbbox(
            (0, 0),
            candidate,
            font=font,)

        if bbox[2] - bbox[0] <= max_width:
            current = candidate

        else:

            if current:
                lines.append(current)

            current = word

    if current:
        lines.append(current)

    return lines


def render_text(
    image,
    text,
    font_path,
    font_size=46,
    margin=140,
    seed=42,):

    random.seed(seed)

    font_path = Path(font_path)

    if not font_path.exists():
        raise FileNotFoundError(
            f"Font not found: {font_path}")

    font = ImageFont.truetype(
        str(font_path),
        font_size,)

    side_font = ImageFont.truetype(
        str(font_path),
        max(22, int(font_size * 0.55)),)

    draw = ImageDraw.Draw(image)

    width, height = image.size

    boxes = []

    main_left = margin
    main_right = width - margin - 210

    main_width = (
        main_right - main_left)

    y = margin

    line_spacing = int(
        font_size * 1.55)

    paragraphs = [
        p.strip()
        for p in text.split("\n")
        if p.strip()
    ]


    for paragraph_index, paragraph in enumerate(
        paragraphs):

        lines = _wrap_text(
            draw,
            paragraph,
            font,
            main_width,)

        for line_index, line in enumerate(lines):

            if y + line_spacing >= height - margin:
                break

            highlight = (
                random.random() < 0.08)

            _render_line(
                image=image,
                text=line,
                font=font,
                x=main_left,
                y=y,
                boxes=boxes,
                text_type="main_text",
                highlight=highlight,)

            y += (
                line_spacing
                + random.randint(-2, 2))

        y += random.randint(
            12,
            30,)

        if y >= height - margin:
            break

    marker_y = min(
        height - margin - 80,
        y + 10,)

    marker = random.choice([
        "॥",
        "॰",
        "✦",
        "❖",
        "॥ २ ॥",
    ])

    marker_bbox = draw.textbbox(
        (0, 0),
        marker,
        font=font,)

    marker_width = (
        marker_bbox[2]
        - marker_bbox[0])

    marker_x = (
        width // 2
        - marker_width // 2)

    _render_line(
        image=image,
        text=marker,
        font=font,
        x=marker_x,
        y=marker_y,
        boxes=boxes,
        text_type="section_marker",)

    if random.random() < 0.75:

        side_text = random.choice([
            "टीका",
            "व्याख्या",
            "टिप्पणी",
            "पाठ",
        ])

        side_x = width - margin - 150

        side_y = margin + random.randint(
            80,
            260,)

        side_bbox = _render_line(
            image=image,
            text=side_text,
            font=side_font,
            x=side_x,
            y=side_y,
            boxes=boxes,
            text_type="marginal_note",)

    return boxes