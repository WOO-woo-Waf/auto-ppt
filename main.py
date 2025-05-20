import argparse
import json
import os
from pptx import Presentation

from tools.slide_types import (
    add_title_slide,
    add_section_slide,
    add_content_slide,
    add_closing_slide,
)
from tools.background_utils import set_background


# ---------- 载入模板文件 ----------
def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    parser = argparse.ArgumentParser(description="Generate PPT from templates")
    parser.add_argument("--template", default="slides/夜游宫.json", help="slide template JSON")
    parser.add_argument("--style", default="styles/style1.json", help="style JSON")
    parser.add_argument("--output_dir", default="output", help="directory for generated ppt")
    parser.add_argument("--image_dir", default="images", help="directory for slide images")
    args = parser.parse_args()

    template = load_json(args.template)
    style_data = load_json(args.style)
    style = style_data["style"]

    template_name = os.path.splitext(os.path.basename(args.template))[0]
    style_name = os.path.splitext(os.path.basename(args.style))[0]
    output_file = f"{template_name}_{style_name}.pptx"
    output_path = os.path.join(args.output_dir, output_file)

    prs = Presentation()

    for slide_data in template["slides"]:
        s_type = slide_data["type"]

        if s_type == "title":
            slide = add_title_slide(prs, slide_data, style)
        elif s_type == "section":
            slide = add_section_slide(prs, slide_data, style)
        elif s_type == "content":
            slide = add_content_slide(prs, slide_data, style, image_dir=args.image_dir)
        elif s_type == "closing":
            slide = add_closing_slide(prs, slide_data, style)
        else:
            continue

        bg_config = style["background"].get(s_type, {"type": "solid", "color": "#FFFFFF"})
        set_background(slide, bg_config, prs)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    prs.save(output_path)
    print(f"PPT 生成成功: {output_path}")


if __name__ == "__main__":
    main()
