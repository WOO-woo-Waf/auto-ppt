import json
from pptx import Presentation
import os

from tools.slide_types import (
    add_title_slide,
    add_section_slide,
    add_content_slide,
    add_closing_slide
)
from tools.background_utils import set_background


# ---------- 载入模板文件 ----------
def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


template_file = "slides/aicode.json"
style_file = "styles/style1.json"

template_name = os.path.splitext(os.path.basename(template_file))[0]
style_name = os.path.splitext(os.path.basename(style_file))[0]

output_file = f"{template_name}_{style_name}.pptx"
output_path = os.path.join("output", output_file)

template = load_json(template_file)
style_data = load_json(style_file)
style = style_data["style"]

# ---------- 生成幻灯片 ----------
prs = Presentation()

for slide_data in template["slides"]:
    s_type = slide_data["type"]

    if s_type == "title":
        slide = add_title_slide(prs, slide_data, style)
    elif s_type == "section":
        slide = add_section_slide(prs, slide_data, style)
    elif s_type == "content":
        slide = add_content_slide(prs, slide_data, style)
    elif s_type == "closing":
        slide = add_closing_slide(prs, slide_data, style)
    else:
        continue

    bg_config = style["background"].get(s_type, {"type": "solid", "color": "#FFFFFF"})
    set_background(slide, bg_config, prs)

# ---------- 保存文件 ----------
os.makedirs(os.path.dirname(output_path), exist_ok=True)
prs.save(output_path)
print(f"PPT 生成成功: {output_path}")
