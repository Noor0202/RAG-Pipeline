# RAG_Project\app\embeddings\json_embedding.py
import json
import uuid
from .base_embedding import AbstractDocumentEmbedding
from app import get_connection_string, get_connection
from langchain_community.embeddings import SentenceTransformerEmbeddings

class JSONEmbedding(AbstractDocumentEmbedding):

    def __init__(self):
        self.conn = get_connection()
        self.connection_string = get_connection_string()
        self.instructor_embeddings = SentenceTransformerEmbeddings(
            model_name="all-MiniLM-L6-v2",
            model_kwargs={"trust_remote_code": True}
        )

    def embed_document(self, documents: list):
        if not self.conn:
            print("Database connection failed.")
            return

        create_json_table_query = """
        CREATE TABLE IF NOT EXISTS embeddings_json (
            id TEXT PRIMARY KEY,
            meta TEXT,
            content TEXT NOT NULL,
            embedding JSONB NOT NULL
        );
        """
        self._create_table(create_json_table_query)

        insert_query = """
        INSERT INTO embeddings_json (id, meta, content, embedding)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING;
        """
        cursor = self.conn.cursor()

        for document_chunk in documents:
            embedding = self.instructor_embeddings.embed_documents([document_chunk.page_content])[0]
            embedding_data = {
                "id": str(uuid.uuid4()),
                "content": document_chunk.page_content,
                "meta": document_chunk.metadata,
                "embedding": embedding  
            }

            cursor.execute(insert_query, (
                embedding_data["id"], 
                json.dumps(embedding_data["meta"]), 
                embedding_data["content"], 
                json.dumps(embedding_data["embedding"])
            ))
            self.conn.commit()

        cursor.close()
        self.conn.close()
        print("JSON Embeddings inserted into PostgreSQL successfully!")

    def _create_table(self, table_query):
        cursor = self.conn.cursor()
        cursor.execute(table_query)
        self.conn.commit()
        cursor.close()
