from PIL import Image, ImageDraw, ImageFilter
import random


def create_aged_paper(
    width=1600,
    height=1200,
    seed=42,):

    random.seed(seed)

    paper_color = random.choice([
        (218, 194, 145),
        (225, 205, 165), 
        (210, 185, 135), 
        (232, 215, 180),  
        (202, 178, 130), 
        (220, 198, 155),  
    ])

    image = Image.new(
        "RGB",
        (width, height),
        paper_color,)

    noise = Image.effect_noise((width, height),18,).convert("L")

    noise = noise.filter(ImageFilter.GaussianBlur(0.6))

    noise_layer = Image.new(
        "RGB",(width, height),(125, 105, 70),)

    image = Image.blend(
        image,
        noise_layer,
        0.08,)

    texture = Image.new(
        "RGBA",
        (width, height),
        (0, 0, 0, 0),)

    draw = ImageDraw.Draw(texture)

    for _ in range(45):

        x = random.randint(-200,width + 200,)

        y = random.randint( -200,height + 200,)

        rx = random.randint(80,350,)

        ry = random.randint(40,220,)

        color = random.choice([
            (120, 85, 45, 18),
            (160, 120, 65, 15),
            (245, 225, 170, 18),
            (95, 70, 40, 10),
        ])

        draw.ellipse(
            (
                x - rx,
                y - ry,
                x + rx,
                y + ry,
            ),fill=color,)

    texture = texture.filter(ImageFilter.GaussianBlur(45))

    image = Image.alpha_composite(
        image.convert("RGBA"),
        texture,)

    stains = Image.new(
        "RGBA",
        (width, height),
        (0, 0, 0, 0),)

    stain_draw = ImageDraw.Draw(stains)

    for _ in range(28):

        x = random.randint(-100,width + 100,)

        y = random.randint( -100, height + 100,)

        rx = random.randint(25,130,)

        ry = random.randint(15,100,)

        stain_draw.ellipse(
            (
                x - rx,
                y - ry,
                x + rx,
                y + ry,
            ),
            fill=(
                random.randint(90, 145),
                random.randint(65, 100),
                random.randint(35, 60),
                random.randint(12, 35),
            ),
            outline=(
                100,
                70,
                35,
                random.randint(15, 35),
            ),
            width=random.randint(1, 4),
        )

    stains = stains.filter(ImageFilter.GaussianBlur(7))

    image = Image.alpha_composite(
        image,
        stains,)


    edges = Image.new(
        "RGBA",
        (width, height),
        (0, 0, 0, 0),)

    edge_draw = ImageDraw.Draw(edges)

    edge_size = random.randint(35,70,)

    edge_draw.rectangle(
        (0, 0, width, edge_size),
        fill=(75, 50, 25, 65),)

    edge_draw.rectangle(
        (0,height - edge_size,
            width,
            height,),
        fill=(65, 45, 25, 75),)

    edge_draw.rectangle(
        (0, 0, edge_size, height),
        fill=(70, 45, 25, 70),)

    edge_draw.rectangle(
        ( width - edge_size,
            0,
            width,
            height,
        ),
        fill=(65, 45, 25, 75),)

    edges = edges.filter(ImageFilter.GaussianBlur(28))

    image = Image.alpha_composite(image,edges,)

    fibers = Image.new(
        "RGBA",
        (width, height),
        (0, 0, 0, 0),)

    fiber_draw = ImageDraw.Draw(fibers)

    for _ in range(900):

        x = random.randint(0,width - 1,)

        y = random.randint(0, height - 1,)

        length = random.randint(3,18,)

        fiber_color = random.choice([
            (90, 65, 35, 20),
            (255, 240, 195, 20),
            (120, 90, 50, 16),
        ])

        fiber_draw.line(
            (
                x,
                y,
                x + length,
                y + random.randint(-2, 2),
            ),
            fill=fiber_color,
            width=1,
        )

    image = Image.alpha_composite(image,fibers,)

    border = Image.new(
        "RGBA",
        (width, height),
        (0, 0, 0, 0),)

    border_draw = ImageDraw.Draw(border)

    margin = random.randint(55,85,)

    border_color = (105,55,30,105,)

    border_draw.rectangle(
        (
            margin,
            margin,
            width - margin,
            height - margin,
        ),
        outline=border_color,
        width=2,
    )

    border_draw.rectangle(
        (
            margin + 12,
            margin + 12,
            width - margin - 12,
            height - margin - 12,
        ),
        outline=(120,75,40,45,),width=1,)

    image = Image.alpha_composite(image,border,)

    ruling = Image.new(
        "RGBA",
        (width, height),
        (0, 0, 0, 0),)

    ruling_draw = ImageDraw.Draw(ruling)

    if random.random() < 0.75:

        ruling_x = random.randint(
            width - 330,
            width - 180,)

        ruling_draw.line(
            (
                ruling_x,
                70,
                ruling_x + random.randint(-3, 3),
                height - 70,
            ),
            fill=(125,55,45,100,),width=2,)

        if random.random() < 0.5:

            ruling_draw.line(
                (
                    ruling_x + 8,
                    70,
                    ruling_x + 8,
                    height - 70,
                ),
                fill=(135,60,45,55,),
                width=1,
            )

    image = Image.alpha_composite(image,ruling,)

    folds = Image.new(
        "RGBA",
        (width, height),
        (0, 0, 0, 0),)

    fold_draw = ImageDraw.Draw(folds)

    for _ in range(random.randint(1, 3)):

        y = random.randint(
            100,
            height - 100,
        )

        points = []

        for x in range(
            0,
            width + 1,
            80,
        ):
            points.append(
                (
                    x,
                    y + random.randint(-8, 8),
                )
            )

        fold_draw.line(
            points,
            fill=(90,60,35,30,
            ),
            width=random.randint(2, 5),
        )

    folds = folds.filter(
        ImageFilter.GaussianBlur(3)
    )

    image = Image.alpha_composite(
        image,
        folds,
    )

    return image.convert("RGB")