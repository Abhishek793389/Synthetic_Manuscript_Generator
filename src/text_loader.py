from pathlib import Path
import random


def load_text(path: str) -> str:
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(
            f"Input file not found: {path}")

    text = path.read_text(encoding="utf-8")

    lines = []

    for line in text.splitlines():

        line = line.strip()

        if line.startswith("#"):
            continue

        if line:
            lines.append(line)

    return "\n".join(lines)


def get_random_chunk(
    text: str,
    min_chars: int = 250,
    max_chars: int = 600,
    seed: int | None = None) -> str:

    rng = random.Random(seed)
    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()]

    if not lines:
        return ""

    if len(text) <= max_chars:
        return "\n".join(lines)

    start = rng.randint(0, len(lines) - 1)
    selected = []
    total_chars = 0

    for i in range(start, len(lines)):

        line = lines[i]

        if selected and total_chars + len(line) + 1 > max_chars:
            break

        selected.append(line)
        total_chars += len(line) + 1

        if total_chars >= min_chars:
            break

    if not selected:
        return lines[start]

    return "\n".join(selected)


def get_first_chunk(
    text: str,
    max_chars: int = 500) -> str:

    if len(text) <= max_chars:
        return text

    chunk = text[:max_chars]
    last_space = chunk.rfind(" ")
    if last_space > 0:
        chunk = chunk[:last_space]

    return chunk