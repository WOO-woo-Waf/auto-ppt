from pptx.util import Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

def get_style_by_path(style_config, path):
    """
    从多层级样式配置中获取对应配置。
    示例路径： "content.bullet_text"
    """
    keys = path.split(".")
    for k in keys:
        style_config = style_config.get(k, {})
    return style_config


def dynamic_font_size(text, base_size, max_length=25, min_size=16):
    """
    根据文本长度自动调整字体大小，超过 max_length 时按比例缩小。
    """
    if len(text) <= max_length:
        return Pt(base_size)
    scale = max(min_size / base_size, 1 - (len(text) - max_length) * 0.02)
    return Pt(max(min_size, int(base_size * scale)))


def set_font(paragraph, style_config, path="content.bullet_text", alignment=None, is_title=False):
    """
    设置段落字体样式，包含动态字号计算、颜色、粗体等。

    :param alignment:
    :param paragraph: pptx 段落对象
    :param style_config: 从 style.json 加载的完整 style 字典
    :param path: 字体样式路径，如 "title.title_text"
    """
    style = get_style_by_path(style_config, path)
    run = paragraph.add_run()
    run.text = paragraph.text.strip()
    paragraph.clear()
    r = paragraph.add_run()
    r.text = run.text
    if alignment:
        if alignment == "center":
            paragraph.alignment = PP_ALIGN.CENTER
        elif alignment == "right":
            paragraph.alignment = PP_ALIGN.RIGHT
        else:
            paragraph.alignment = PP_ALIGN.LEFT

    if is_title:
        # 动态字体大小逻辑
        base_size = style.get("font_size", 24)
        max_len = style.get("max_char", 25)  # 可选配置
        min_size = style.get("min_font_size", 16)
        r.font.size = dynamic_font_size(r.text, base_size, max_len, min_size)
    else:
        # 设置默认字体大小
        r.font.size = Pt(style.get("font_size", 18))

    # 样式设置
    r.font.bold = style.get("bold", False)
    r.font.name = style.get("font_name", "微软雅黑")

    color_hex = style.get("font_color", "#000000")
    if color_hex.startswith("#") and len(color_hex) == 7:
        r.font.color.rgb = RGBColor(
            int(color_hex[1:3], 16),
            int(color_hex[3:5], 16),
            int(color_hex[5:7], 16)
        )
