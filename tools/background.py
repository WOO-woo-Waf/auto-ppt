from PIL import Image, ImageDraw


def generate_gradient_background(filename, size=(1920, 1080), direction="vertical", start_color="#111111",
                                 end_color="#444444"):
    """
    生成渐变背景图。
    :param filename: 输出文件名
    :param size: 图片尺寸（宽, 高）
    :param direction: 渐变方向 'vertical' 或 'horizontal'
    :param start_color: 起始颜色 hex
    :param end_color: 终止颜色 hex
    """
    width, height = size
    image = Image.new("RGB", size)
    draw = ImageDraw.Draw(image)

    start_rgb = tuple(int(start_color[i:i + 2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_color[i:i + 2], 16) for i in (1, 3, 5))

    if direction == "vertical":
        for y in range(height):
            ratio = y / height
            r = int(start_rgb[0] * (1 - ratio) + end_rgb[0] * ratio)
            g = int(start_rgb[1] * (1 - ratio) + end_rgb[1] * ratio)
            b = int(start_rgb[2] * (1 - ratio) + end_rgb[2] * ratio)
            draw.line([(0, y), (width, y)], fill=(r, g, b))
    else:
        for x in range(width):
            ratio = x / width
            r = int(start_rgb[0] * (1 - ratio) + end_rgb[0] * ratio)
            g = int(start_rgb[1] * (1 - ratio) + end_rgb[1] * ratio)
            b = int(start_rgb[2] * (1 - ratio) + end_rgb[2] * ratio)
            draw.line([(x, 0), (x, height)], fill=(r, g, b))

    image.save(filename)


# 生成几种风格背景图
output_dir = "../assets/backgrounds/"
files = []

gradient_configs = [
    ("tech_dark.png", "#111111", "#333333", "vertical"),
    ("blue_modern.png", "#1F3A93", "#00BCD4", "horizontal"),
    ("soft_grey.png", "#EEEEEE", "#CCCCCC", "vertical"),
    ("green_signal.png", "#006442", "#00FF88", "horizontal"),
    ("sunrise_orange.png", "#FF6F00", "#FFD54F", "vertical")
]

for fname, start, end, direction in gradient_configs:
    path = output_dir + fname
    generate_gradient_background(path, direction=direction, start_color=start, end_color=end)
    files.append(path)
