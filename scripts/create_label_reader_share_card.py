#!/usr/bin/env python3

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "label-reader-practice-social.png"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = (
        "/System/Library/Fonts/Supplemental/Verdana Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Verdana.ttf",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    )
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(path, size)
    raise FileNotFoundError("No supported font found")


def main() -> None:
    width, height = 1200, 630
    image = Image.new("RGB", (width, height), "#0d5735")
    pixels = image.load()
    for y in range(height):
        blend = y / (height - 1)
        for x in range(width):
            horizontal = x / (width - 1)
            pixels[x, y] = (
                int(10 + 12 * blend),
                int(61 + 60 * horizontal + 8 * blend),
                int(44 + 37 * horizontal),
            )

    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((64, 58, 1136, 572), radius=34, fill="#f8fbf8")
    draw.rounded_rectangle((106, 98, 458, 148), radius=25, fill="#e2f1e7")
    draw.text((132, 111), "THE LABEL READER PRACTICE", font=font(19, True), fill="#0d5735")

    draw.text((106, 190), "I turn the package", font=font(59, True), fill="#17211b")
    draw.text((106, 262), "around.", font=font(59, True), fill="#16794b")

    body = font(27)
    draw.text((108, 368), "I read what is actually printed.", font=body, fill="#425148")
    draw.text((108, 409), "I keep my own record.", font=body, fill="#425148")
    draw.text((108, 450), "I remember what I read.", font=body, fill="#425148")

    draw.rounded_rectangle((820, 180, 1032, 392), radius=30, outline="#9dcab0", width=5)
    draw.rounded_rectangle((856, 217, 996, 344), radius=18, fill="#e2f1e7")
    draw.line((880, 252, 972, 252), fill="#16794b", width=7)
    draw.line((880, 281, 958, 281), fill="#16794b", width=7)
    draw.line((880, 310, 966, 310), fill="#16794b", width=7)

    draw.text((108, 517), "Ingredio", font=font(23, True), fill="#0d5735")
    draw.text((226, 517), "·  Remember what you read.", font=font(23), fill="#56635b")

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    image.save(OUTPUT, format="PNG", optimize=True)
    print(f"created={OUTPUT}")
    print(f"size={image.size[0]}x{image.size[1]}")


if __name__ == "__main__":
    main()
