import re

def clean_text(text: str) -> str:
    text = text.strip()
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\w\s]", "", text)
    return text

text = "   I NEED HELP!!!   "
print(clean_text(text))
