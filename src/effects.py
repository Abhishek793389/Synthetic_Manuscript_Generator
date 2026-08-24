from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
import random


def _overlay(base, layer):
    return Image.alpha_composite(
        base.convert("RGBA"),
        layer.convert("RGBA"),)


def _add_faded_patches(image, rng):

    width, height = image.size

    layer = Image.new(
        "RGBA",
        image.size,
        (0, 0, 0, 0),)

    draw = ImageDraw.Draw(layer)
    for _ in range(rng.randint(12, 24)):

        x = rng.randint(-100, width + 100)
        y = rng.randint(-100, height + 100)

        rx = rng.randint(40, 220)
        ry = rng.randint(20, 140)

        draw.ellipse(
            (
                x - rx,
                y - ry,
                x + rx,
                y + ry,
            ),
            fill=(
                rng.randint(225, 250),
                rng.randint(205, 235),
                rng.randint(160, 205),
                rng.randint(8, 24),
            ),
        )

    layer = layer.filter(
        ImageFilter.GaussianBlur(35)
    )

    return _overlay(image, layer)


def _add_ink_and_age_spots(image, rng):

    width, height = image.size

    layer = Image.new(
        "RGBA",
        image.size,
        (0, 0, 0, 0),)

    draw = ImageDraw.Draw(layer)

    for _ in range(rng.randint(100, 180)):

        x = rng.randint(15, width - 15)
        y = rng.randint(15, height - 15)

        radius = rng.randint(1, 4)

        draw.ellipse(
            (
                x - radius,
                y - radius,
                x + radius,
                y + radius,
            ),
            fill=(
                rng.randint(55, 110),
                rng.randint(35, 75),
                rng.randint(20, 50),
                rng.randint(8, 35),
            ),
        )

    for _ in range(rng.randint(12, 24)):

        x = rng.randint(-50, width + 50)
        y = rng.randint(-50, height + 50)

        rx = rng.randint(20, 110)
        ry = rng.randint(15, 80)

        color = rng.choice([
            (90, 60, 30, 15),
            (110, 70, 35, 18),
            (75, 55, 35, 14),
            (135, 95, 45, 12),
        ])

        draw.ellipse(
            (
                x - rx,
                y - ry,
                x + rx,
                y + ry,
            ),
            fill=color,
            outline=(
                75,
                50,
                25,
                rng.randint(8, 22),),
            width=rng.randint(1, 3),)

    layer = layer.filter(ImageFilter.GaussianBlur(1.1))

    return _overlay(image, layer)


def _add_paper_fibers(image, rng):

    width, height = image.size
    layer = Image.new(
        "RGBA",
        image.size,
        (0, 0, 0, 0),)

    draw = ImageDraw.Draw(layer)

    for _ in range(rng.randint(700, 1100)):

        x = rng.randint(0, width - 1)
        y = rng.randint(0, height - 1)

        length = rng.randint(3, 18)

        color = rng.choice([
            (80, 55, 30, 15),
            (100, 70, 35, 13),
            (255, 240, 195, 14),
            (120, 90, 50, 12),
        ])

        draw.line((x,y,x + length,y + rng.randint(-2, 2),),fill=color,width=1,)

    return _overlay(image, layer)


def _add_ink_bleed(image, rng):
    width, height = image.size
    layer = Image.new(
        "RGBA",
        image.size,
        (0, 0, 0, 0),)

    draw = ImageDraw.Draw(layer)

    for _ in range(rng.randint(3, 8)):

        x = rng.randint(100, width - 100)
        y = rng.randint(100, height - 100)

        rx = rng.randint(10, 45)
        ry = rng.randint(4, 18)

        draw.ellipse(
            (x - rx, y - ry, x + rx, y + ry,),
            fill=(55,40,28,rng.randint(5, 14),),)

    layer = layer.filter(ImageFilter.GaussianBlur(5))

    return _overlay(image, layer)


def _add_folds_and_creases(image, rng):

    width, height = image.size
    layer = Image.new(
        "RGBA",
        image.size,
        (0, 0, 0, 0),)

    draw = ImageDraw.Draw(layer)

    for _ in range(rng.randint(1, 3)):

        y = rng.randint(
            120,
            height - 120,)

        points = []

        for x in range(
            0,
            width + 1,
            80,):
            points.append(
                (x, y + rng.randint(-7, 7),))

        draw.line(points, fill=(65,45,28, rng.randint(15, 30),),width=rng.randint(3, 7),)

        points_highlight = [
            (x, py - 3)
            for x, py in points]

        draw.line(
            points_highlight,
            fill=(245,225,180,rng.randint(8, 18),),width=2,)

    if rng.random() < 0.45:

        x = rng.randint(150,width - 150,)

        points = []

        for y in range(0, height + 1,80,):
            points.append((x + rng.randint(-5, 5),y,))

        draw.line(points,fill=(65,45,28,rng.randint(10, 22),),width=rng.randint(2, 5),)

    layer = layer.filter(ImageFilter.GaussianBlur(3))

    return _overlay(image, layer)


def _add_edge_wear(image, rng):

    width, height = image.size

    layer = Image.new(
        "RGBA",
        image.size,
        (0, 0, 0, 0),)

    draw = ImageDraw.Draw(layer)
    edge_size = rng.randint(30, 70)

    draw.rectangle(
        (0, 0, width, edge_size),
        fill=(65, 45, 25, rng.randint(25, 55)),)

    draw.rectangle(
        (0, height - edge_size, width, height,),
        fill=(60, 40, 25, rng.randint(30, 60)),)

    draw.rectangle(
        (0, 0, edge_size, height),
        fill=(65, 45, 25, rng.randint(25, 55)),)

    draw.rectangle(
        (width - edge_size,0,width,height,),
        fill=(60, 40, 25, rng.randint(30, 60)),)

    layer = layer.filter(ImageFilter.GaussianBlur(25))

    image = _overlay(image, layer)

    wear = Image.new(
        "RGBA",
        image.size,
        (0, 0, 0, 0),)

    wear_draw = ImageDraw.Draw(wear)

    for _ in range(rng.randint(10, 20)):

        side = rng.choice([
            "left",
            "right",
            "top",
            "bottom",
        ])

        if side == "left":
            x = rng.randint(0, 30)
            wear_draw.line(
                (
                    x,
                    rng.randint(0, height),
                    x + rng.randint(-4, 4),
                    rng.randint(0, height),
                ),
                fill=(65, 45, 25, rng.randint(15, 35)),
                width=rng.randint(2, 6),
            )

        elif side == "right":
            x = rng.randint(
                width - 30,
                width,)
            wear_draw.line(
                (
                    x,
                    rng.randint(0, height),
                    x + rng.randint(-4, 4),
                    rng.randint(0, height),
                ),
                fill=(65, 45, 25, rng.randint(15, 35)),
                width=rng.randint(2, 6),)

        elif side == "top":
            y = rng.randint(0, 30)
            wear_draw.line(
                (
                    rng.randint(0, width),
                    y,
                    rng.randint(0, width),
                    y + rng.randint(-4, 4),
                ),
                fill=(65, 45, 25, rng.randint(15, 35)),
                width=rng.randint(2, 6),)

        else:
            y = rng.randint(
                height - 30,
                height,)
            wear_draw.line(
                (
                    rng.randint(0, width),
                    y,
                    rng.randint(0, width),
                    y + rng.randint(-4, 4),
                ),
                fill=(65, 45, 25, rng.randint(15, 35)),
                width=rng.randint(2, 6),)

    wear = wear.filter(ImageFilter.GaussianBlur(2))

    return _overlay(image, wear)


def _add_surface_variation(image, rng):

    contrast = rng.uniform(0.94,1.06,)

    image_rgb = image.convert("RGB")

    image_rgb = ImageEnhance.Contrast(image_rgb).enhance(contrast)

    color = rng.uniform(0.96,1.04,)

    image_rgb = ImageEnhance.Color(image_rgb).enhance(color)

    return image_rgb.convert("RGBA")


def _add_surface_warp(image, rng):
    width, height = image.size

    if rng.random() > 0.65:
        return image

    shear_x = rng.uniform(
        -0.008,
        0.008,)

    shear_y = rng.uniform(
        -0.004,
        0.004,)

    try:
        warped = image.transform(
            (width, height),
            Image.Transform.AFFINE,
            (
                1,
                shear_x,
                0,
                shear_y,
                1,
                0,
            ),
            resample=Image.Resampling.BICUBIC,
        )

        return warped

    except Exception:
        return image


def _add_page_curl_shadows(image, rng):

    width, height = image.size

    layer = Image.new(
        "RGBA",
        image.size,
        (0, 0, 0, 0),)

    draw = ImageDraw.Draw(layer)
    if rng.random() < 0.35:

        draw.ellipse(
            (
                -100,
                -50,
                100,
                height + 50,
            ),
            fill=(55,40,25,15,),)

    if rng.random() < 0.35:

        draw.ellipse(
            (
                width - 100,
                -50,
                width + 100,
                height + 50,
            ),
            fill=(55,40,25,15,),)

    layer = layer.filter(ImageFilter.GaussianBlur(30))

    return _overlay(image, layer)


def apply_manuscript_effects(
    image,
    seed=42,):
    rng = random.Random(seed)

    image = image.convert("RGBA")

    image = _add_surface_variation(
        image,
        rng,)

    image = _add_paper_fibers(
        image,
        rng,)

    image = _add_faded_patches(
        image,
        rng,)

    image = _add_ink_and_age_spots(
        image,
        rng,)

    image = _add_ink_bleed(
        image,
        rng,)

    image = _add_folds_and_creases(
        image,
        rng,
    )

    image = _add_page_curl_shadows(
        image,
        rng,)

    image = _add_edge_wear(
        image,
        rng,
    )

    image = _add_surface_warp(
        image,
        rng,)

    return image.convert("RGB")