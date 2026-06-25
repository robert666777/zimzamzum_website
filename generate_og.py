from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1200, 630

# Color palette
BG = (10, 10, 30)
PURPLE = (108, 99, 255)
WHITE = (255, 255, 255)
LIGHT_PURPLE = (167, 139, 250)
GRAY = (180, 180, 200)
GREEN = (52, 211, 153)

img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# Subtle grid pattern
for x in range(0, W, 60):
    draw.line([(x, 0), (x, H)], fill=(255, 255, 255), width=0)
for y in range(0, H, 60):
    draw.line([(0, y), (W, y)], fill=(255, 255, 255), width=0)

# Background glow blobs
for cx, cy, r, col in [
    (200, 150, 300, (108, 99, 255, 60)),
    (900, 450, 350, (167, 139, 250, 40)),
    (600, 580, 200, (108, 99, 255, 50)),
]:
    blob = Image.new("RGBA", (r * 2, r * 2), (0, 0, 0, 0))
    blob_draw = ImageDraw.Draw(blob)
    for ri in range(r, 0, -4):
        alpha = int((1 - ri / r) * col[3])
        blob_draw.ellipse([r - ri, r - ri, r + ri, r + ri], fill=(col[0], col[1], col[2], alpha))
    img.paste(blob, (cx - r, cy - r), blob)

draw = ImageDraw.Draw(img)

# Left accent bar
draw.rectangle([0, 0, 8, H], fill=PURPLE)

# Top badge "zimzamzum"
badge_text = "zimzamzum"
try:
    badge_font = ImageFont.truetype("arial.ttf", 26)
except:
    badge_font = ImageFont.load_default()
try:
    title_font = ImageFont.truetype("arial.ttf", 90)
except:
    title_font = ImageFont.load_default()
try:
    subtitle_font = ImageFont.truetype("arial.ttf", 34)
except:
    subtitle_font = ImageFont.load_default()
try:
    tag_font = ImageFont.truetype("arial.ttf", 24)
except:
    tag_font = ImageFont.load_default()

# Logo mark (stylized "z" hexagon)
hex_points = [(55, 30), (80, 18), (80, 42), (55, 54), (30, 42), (30, 18)]
draw.polygon(hex_points, fill=PURPLE, outline=PURPLE)

# Badge text beside hexagon
draw.text((95, 30), badge_text, fill=LIGHT_PURPLE, font=badge_font)

# Main title
title = "AI for Your"
bbox = draw.textbbox((0, 0), title, font=title_font)
tw = bbox[2] - bbox[0]
draw.text(((W - tw) // 2, 160), title, fill=WHITE, font=title_font)

title2 = "Assignments"
bbox2 = draw.textbbox((0, 0), title2, font=title_font)
tw2 = bbox2[2] - bbox2[0]
draw.text(((W - tw2) // 2, 260), title2, fill=PURPLE, font=title_font)

# Divider
divider_y = 375
draw.rectangle([300, divider_y, 900, divider_y + 2], fill=PURPLE)

# Subtitle
subtitle = "Automate homework. Track deadlines. Submit on time."
bbox_sub = draw.textbbox((0, 0), subtitle, font=subtitle_font)
sw = bbox_sub[2] - bbox_sub[0]
draw.text(((W - sw) // 2, 400), subtitle, fill=GRAY, font=subtitle_font)

# Tag pills
tags = ["Chaoxing", "Yuketang", "AI Automation", "Free to Start"]
tx = 200
ty = 500
for tag in tags:
    tag_w = draw.textbbox((0, 0), tag, font=tag_font)
    tw_tag = tag_w[2] - tag_w[0] + 40
    draw.rounded_rectangle([tx, ty, tx + tw_tag, ty + 44], radius=22, fill=(108, 99, 255, 100))
    draw.text((tx + 20, ty + 8), tag, fill=WHITE, font=tag_font)
    tx += tw_tag + 20

# Bottom right: version badge
ver_text = "v1.5.5  |  Windows"
bbox_ver = draw.textbbox((0, 0), ver_text, font=tag_font)
vw = bbox_ver[2] - bbox_ver[0]
draw.rounded_rectangle([W - vw - 80, H - 70, W - 30, H - 30], radius=14, fill=(52, 211, 153, 180))
draw.text((W - vw - 70, H - 62), ver_text, fill=(10, 10, 30), font=tag_font)

# Save
out_dir = os.path.join(os.path.dirname(__file__), "assets")
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "og-image.png")
img.save(out_path, "PNG", optimize=True)
print(f"Saved: {out_path}")
print(f"Size: {W}x{H}")
