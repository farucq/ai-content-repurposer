from sentence_transformers import SentenceTransformer

class EmbeddingGenerator:

    def __init__(self):

        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def create_embedding(self, text):

        embedding = self.model.encode(text)

        return embedding.tolist()