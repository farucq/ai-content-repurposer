import chromadb

class ChromaVectorStore:

    def __init__(self):

        self.client = chromadb.Client()

        self.collection = self.client.create_collection(
            name="blog_embeddings"
        )

    def store(self, text, embedding):

        self.collection.add(
            documents=[text],
            embeddings=[embedding],
            ids=[str(hash(text))]
        )

    def search(self, embedding):

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=3
        )

        return results