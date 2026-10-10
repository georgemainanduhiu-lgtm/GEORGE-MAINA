"""Generate a placeholder Kindle cover (1600x2560, the KDP-recommended ratio).

Typography over a stylized soccer pitch. No player photos, likenesses, club
crests, or trademarks are used. Replace with a professionally designed cover
before publishing if you can.
"""
import sys
from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 2560
OUT = sys.argv[1] if len(sys.argv) > 1 else "dist/cover.jpg"

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

img = Image.new("RGB", (W, H))
d = ImageDraw.Draw(img)

# Mowed-grass stripes
stripe = 160
for i, y in enumerate(range(0, H, stripe)):
    d.rectangle([0, y, W, y + stripe], fill=(34, 120, 52) if i % 2 == 0 else (40, 134, 60))

# Pitch markings
line = (235, 245, 235)
lw = 10
d.rectangle([80, 80, W - 80, H - 80], outline=line, width=lw)
d.line([80, H // 2, W - 80, H // 2], fill=line, width=lw)
r = 260
d.ellipse([W // 2 - r, H // 2 - r, W // 2 + r, H // 2 + r], outline=line, width=lw)
d.ellipse([W // 2 - 18, H // 2 - 18, W // 2 + 18, H // 2 + 18], fill=line)
# Penalty boxes
d.rectangle([W // 2 - 420, H - 80 - 330, W // 2 + 420, H - 80], outline=line, width=lw)
d.rectangle([W // 2 - 420, 80, W // 2 + 420, 80 + 330], outline=line, width=lw)

# Soccer ball in the center circle
bx, by, br = W // 2, H // 2, 150
d.ellipse([bx - br, by - br, bx + br, by + br], fill=(250, 250, 250), outline=(20, 20, 20), width=8)
pent = [(bx, by - 62), (bx + 59, by - 19), (bx + 37, by + 50), (bx - 37, by + 50), (bx - 59, by - 19)]
d.polygon(pent, fill=(20, 20, 20))
for (px, py) in pent:
    ex = bx + (px - bx) * 2.3
    ey = by + (py - by) * 2.3
    d.line([px, py, ex, ey], fill=(20, 20, 20), width=8)


def centered(text, y, font, fill, shadow=True):
    w = d.textlength(text, font=font)
    x = (W - w) / 2
    if shadow:
        d.text((x + 5, y + 5), text, font=font, fill=(10, 50, 20))
    d.text((x, y), text, font=font, fill=fill)


# Title banner (top)
d.rectangle([0, 250, W, 1000], fill=(12, 40, 80))
title_font = ImageFont.truetype(BOLD, 170)
centered("SOCCER", 300, title_font, (255, 215, 0))
centered("HEROES", 480, title_font, (255, 255, 255))
sub_font = ImageFont.truetype(BOLD, 86)
centered("WHO NEVER", 680, sub_font, (255, 255, 255))
centered("GAVE UP", 790, sub_font, (255, 215, 0))

# Subtitle (bottom)
d.rectangle([0, 1560, W, 2230], fill=(12, 40, 80))
s_font = ImageFont.truetype(BOLD, 64)
centered("12 True Stories of", 1610, s_font, (255, 255, 255), shadow=False)
centered("Courage, Teamwork,", 1700, s_font, (255, 255, 255), shadow=False)
centered("and Big Dreams", 1790, s_font, (255, 255, 255), shadow=False)
age_font = ImageFont.truetype(BOLD, 58)
centered("FOR KIDS AGES 8–12", 1905, age_font, (255, 215, 0), shadow=False)
n_font = ImageFont.truetype(REG, 40)
centered("Messi • Ronaldo • Yamal • Mbappé • Haaland • Salah", 2030, n_font, (220, 230, 240), shadow=False)
centered("Vinícius Jr. • Bellingham • Saka • Dembélé • Yıldız • Modrić", 2090, n_font, (220, 230, 240), shadow=False)

author_font = ImageFont.truetype(BOLD, 72)
centered("GEORGE MAINA", 2330, author_font, (255, 255, 255))

img.save(OUT, "JPEG", quality=92)
print(f"wrote {OUT}")
