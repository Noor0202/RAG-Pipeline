# RAG_Project\app\embeddings\base_embedding.py

from abc import ABC, abstractmethod

class AbstractDocumentEmbedding(ABC):
    @abstractmethod
    def embed_document(self, documents: list):
        pass
