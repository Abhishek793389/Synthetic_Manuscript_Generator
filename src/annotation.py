from pathlib import Path


def save_annotation(
    path,
    script,
    material,
    source_text,
    bounding_boxes,
):
    content = f"""# Manuscript Annotation

## Source Text

{source_text}


"""

    Path(path).write_text(
        content,
        encoding="utf-8"
    )