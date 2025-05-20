import re


def extract_illustration_keyword(text: str) -> str | None:
    """Extract the keyword after the illustration tag."""
    match = re.search(r"【插图】(.*)", text)
    return match.group(1).strip() if match else None
