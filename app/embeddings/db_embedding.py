# RAG_Project\app\embeddings\db_embedding.py

from .base_embedding import AbstractDocumentEmbedding
from langchain_community.vectorstores import PGVector
from app import get_connection_string
from langchain_community.embeddings import SentenceTransformerEmbeddings

class DBEmbedding(AbstractDocumentEmbedding):

    def __init__(self, COLLECTION_NAME):
        self.collection_name = COLLECTION_NAME
        self.connection_string = get_connection_string()

        self.instructor_embeddings = SentenceTransformerEmbeddings(
            model_name="all-MiniLM-L6-v2",
            model_kwargs={"trust_remote_code": True}
        )

    def embed_document(self, documents: list):
        document_texts = [doc.page_content for doc in documents]
        
        print(f"Generating embeddings for {len(document_texts)} documents...")
        text_embeddings = self.instructor_embeddings.embed_documents(document_texts)

        db = PGVector.from_texts(
            texts=document_texts,
            embedding=self.instructor_embeddings,
            collection_name=self.collection_name,
            connection_string=self.connection_string,
            pre_delete_collection=True
        )

        print(f"Embeddings inserted into PGVector collection '{self.collection_name}' successfully!")
        
        return (self.collection_name, db)
