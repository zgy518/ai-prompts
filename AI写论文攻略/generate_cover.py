"""为 AI写论文攻略 生成759×380封面PNG"""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 759, 380
OUT = os.path.join(os.path.dirname(__file__), "cover-paper-guide.png")

# 找中文字体
FONT_PATHS = [
    "C:/Windows/Fonts/msyh.ttc",
    "C:/Windows/Fonts/simhei.ttf",
    "C:/Windows/Fonts/msyhbd.ttc",
]
font_path = None
for fp in FONT_PATHS:
    if os.path.exists(fp):
        font_path = fp
        break
if not font_path:
    raise RuntimeError("未找到中文字体")

def load_font(size, index=0):
    return ImageFont.truetype(font_path, size, index=index)

img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

def gradient_fill(w, h, c1, c2):
    """垂直渐变"""
    for y in range(h):
        r = int(c1[0] + (c2[0] - c1[0]) * y / h)
        g = int(c1[1] + (c2[1] - c1[1]) * y / h)
        b = int(c1[2] + (c2[2] - c1[2]) * y / h)
        draw.line([(0, y), (w, y)], fill=(r, g, b))

# 背景渐变
gradient_fill(W, H, (26, 10, 46), (22, 33, 62))

# 顶部装饰线
for i in range(3):
    y = 20 + i
    r = 218 - i * 30
    g_val = 165 - i * 20
    b = 11 + i * 10
    draw.line([(30 + i * 3, y), (W - 30 - i * 3, y)], fill=(r, g_val, b))

# Title
font_title = load_font(54, 0)
text = "AI写论文攻略"
bbox = draw.textbbox((0, 0), text, font=font_title)
tw = bbox[2] - bbox[0]
# Position left side of center area
title_x = 38
title_y = 110

# Draw "AI" in white
draw.text((title_x, title_y), "AI", fill=(255, 255, 255), font=font_title)
ai_w = draw.textbbox((0, 0), "AI", font=font_title)[2]
# Draw "写论文攻略" in gold
draw.text((title_x + ai_w, title_y), "写论文攻略", fill=(255, 215, 0), font=font_title)

# Subtitle
font_sub = load_font(18, 0)
sub = "从选题到答辩 · 全流程AI辅助指南"
draw.text((title_x + 4, title_y + 72), sub, fill=(210, 210, 220), font=font_sub)

# Divider
draw.line([(title_x + 4, title_y + 100), (title_x + 280, title_y + 100)], fill=(255, 215, 0, 120))

# Stats - right side
stats_x = 570
stat_font_num = load_font(42, 0)
stat_font_label = load_font(14, 0)

stats = [
    ("46", "条提示词"),
    ("6", "章方法论"),
    ("4", "大AI通用"),
]
s_y = 160
for num, label in stats:
    # Number
    nw = draw.textbbox((0, 0), num, font=stat_font_num)[2]
    draw.text((stats_x - nw // 2, s_y), num, fill=(255, 215, 0), font=stat_font_num)
    # Label
    lw = draw.textbbox((0, 0), label, font=stat_font_label)[2]
    draw.text((stats_x - lw // 2, s_y + 50), label, fill=(170, 170, 190), font=stat_font_label)
    stats_x -= 85

# AI tool badges
badges = ["ChatGPT", "Claude", "Kimi", "通义千问", "豆包"]
badge_y = 310
badge_font = load_font(13, 0)
gap = 14
total_badge_w = 0
for b in badges:
    total_badge_w += draw.textbbox((0, 0), b, font=badge_font)[2] + 28 + gap
total_badge_w -= gap
bx = (W - total_badge_w) // 2
for b in badges:
    bw = draw.textbbox((0, 0), b, font=badge_font)[2]
    # Pill badge background
    pad = 14
    draw.rounded_rectangle(
        [bx, badge_y - 4, bx + bw + pad * 2, badge_y + 22],
        radius=16, outline=(255, 255, 255, 35), width=1,
        fill=(255, 255, 255, 12)
    )
    draw.text((bx + pad, badge_y), b, fill=(210, 210, 220), font=badge_font)
    bx += bw + pad * 2 + gap

# Bottom text
font_bottom = load_font(12, 0)
bottom = "本科生/研究生 · 学术论文全流程指南"
bw = draw.textbbox((0, 0), bottom, font=font_bottom)[2]
draw.text(((W - bw) // 2, H - 28), bottom, fill=(150, 150, 170, 140), font=font_bottom)

# 底部装饰线
for i in range(3):
    y = H - 24 + i
    r = 170 - i * 30
    g_val = 130 - i * 20
    b = 15 + i * 10
    draw.line([(30 + i * 3, y), (W - 30 - i * 3, y)], fill=(r, g_val, b))

# 保存
img.save(OUT, "PNG")
print(f"封面已生成: {OUT}  ({W}x{H})")
