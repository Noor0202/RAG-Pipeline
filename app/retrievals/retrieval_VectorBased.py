# RAG_Project\app\retrievals\retrieval_VectorBased.py
from app.retrievals.base_retrieval import AbstractDocumentRetrieval
from langchain_community.vectorstores import PGVector
from app import get_connection_string
from langchain_community.embeddings import SentenceTransformerEmbeddings

class PGVectorRetrieval(AbstractDocumentRetrieval):
    def __init__(self, collection_name, mydb):
        self.collection_name = collection_name
        self.connection_string = get_connection_string()
        
        self.instructor_embeddings = SentenceTransformerEmbeddings(
            model_name="all-MiniLM-L6-v2",
            model_kwargs={"trust_remote_code": True}
        )

        self.db = mydb
        
        self.pgvector_docsearch = PGVector(
            collection_name=self.collection_name,
            connection_string=self.connection_string,
            embedding_function=self.instructor_embeddings,
        )

    def retrieve_document(self, query, top_k=4):
        if not self.db:
            print("PGVector is not initialized. Please initialize it with documents first.")
            return None
        try:
            docs = self.db.similarity_search(query, k=top_k)
            results = [doc.page_content for doc in docs]
            return results
        except Exception as e:
            print(f"Error during PGVector query: {e}")
            return []
