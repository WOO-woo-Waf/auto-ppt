import re
from typing import List, Optional, Tuple


def parse_tags(text: str) -> Tuple[str, List[str]]:
    """Return remaining text and list of leading tags."""
    tags: List[str] = []
    remaining = text
    while True:
        match = re.match(r"^【([^】]+)】", remaining)
        if not match:
            break
        tags.append(match.group(1))
        remaining = remaining[match.end() :]
    return remaining.strip(), tags


def get_illustration_keyword(tags: List[str], fallback: str) -> Optional[str]:
    """Extract illustration keyword from tags."""
    for tag in tags:
        if tag.startswith("插图") or tag.startswith("图片"):
            parts = tag.split(":", 1)
            if len(parts) == 2 and parts[1].strip():
                return parts[1].strip()
            return fallback.strip() if fallback else None
    return None


def get_color_from_tags(tags: List[str]) -> Optional[str]:
    """Return hex color code specified by tags if any."""
    for tag in tags:
        if tag in ("红色", "red"):
            return "#FF0000"
        if tag in ("蓝色", "blue"):
            return "#0000FF"
        match = re.match(r"(?:颜色|color)[:：]?(.+)", tag, re.IGNORECASE)
        if match:
            color = match.group(1).strip()
            if not color.startswith("#"):
                mapping = {
                    "red": "#FF0000",
                    "blue": "#0000FF",
                    "green": "#00AA00",
                }
                color = mapping.get(color.lower(), "")
            if color:
                if len(color) == 4:
                    color = "#" + color[1] * 2 + color[2] * 2 + color[3] * 2
                return color if len(color) == 7 else None
    return None


def is_emphasis(tags: List[str]) -> bool:
    """Whether tags request emphasised text."""
    return "重点" in tags or "强调" in tags


def extract_illustration_keyword(text: str) -> Optional[str]:
    remaining, tags = parse_tags(text)
    return get_illustration_keyword(tags, remaining)

