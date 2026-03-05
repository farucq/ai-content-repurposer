import re

def clean_text(text):

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def split_sections(text):

    sections = text.split("\n")

    return [s.strip() for s in sections if len(s) > 40]