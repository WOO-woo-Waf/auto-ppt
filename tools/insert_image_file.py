import os
from difflib import get_close_matches
from pptx.util import Inches
from tools.tag_utils import extract_illustration_keyword


def find_matching_image(keyword, folder="images"):
    if not keyword or not os.path.exists(folder):
        return None
    candidates = os.listdir(folder)
    matches = get_close_matches(keyword.replace(" ", "").lower(), [f.lower() for f in candidates], n=1, cutoff=0.4)
    if matches:
        for candidate in candidates:
            if candidate.lower() == matches[0]:
                return os.path.join(folder, candidate)
    return None


def insert_image(slide, image_path):
    if not image_path:
        return
    left = Inches(5.5)
    top = Inches(2)
    width = Inches(3.5)
    try:
        slide.shapes.add_picture(image_path, left, top, width=width)
    except Exception as e:
        print(f"插图失败：{image_path}", e)
