#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "social-preview.png"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial Bold.ttf" if bold else "/Library/Fonts/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


def main() -> None:
    img = Image.new("RGB", (1280, 640), "#0d1117")
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle((70, 70, 1210, 570), radius=30, fill="#f6f8fa")
    draw.text((130, 125), "Goal Task Prompt", fill="#0d1117", font=font(78, True))
    draw.text(
        (132, 220),
        "Turn fuzzy agent requests into verifiable /goal prompts.",
        fill="#24292f",
        font=font(36),
    )

    draw.rounded_rectangle((130, 305, 1150, 470), radius=20, fill="#0d1117")
    draw.text((170, 355), '"make this better"', fill="#7ee787", font=font(30))
    draw.text(
        (170, 410),
        "Goal -> Context -> Boundaries -> Verification -> Stop",
        fill="#f0f6fc",
        font=font(29),
    )

    draw.text(
        (132, 525),
        "Codex skill · Loop Cards · Multi-agent orchestration · Prompt evaluation",
        fill="#57606a",
        font=font(27),
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT, format="PNG", optimize=True)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()

