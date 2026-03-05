import re
from utils.embeddings import EmbeddingGenerator


class SemanticAnalyzer:

    def __init__(self):
        self.embedder = EmbeddingGenerator()

    def analyze(self, content):

        text = content["text"]

        embedding = self.embedder.create_embedding(text)

        sentences = text.split(".")

        key_points = sentences[:5]

        # Extract topic keywords
        words = re.findall(r'\b[A-Za-z]{4,}\b', text)

        topic = " ".join(words[:4])

        return {
            "topic": topic,
            "key_points": key_points,
            "embedding": embedding
        }