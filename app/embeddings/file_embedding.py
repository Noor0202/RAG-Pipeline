# RAG_Project\app\embeddings\file_embedding.py

import os
import json
import uuid
from .base_embedding import AbstractDocumentEmbedding
from langchain_community.embeddings import SentenceTransformerEmbeddings

class FILEEmbedding(AbstractDocumentEmbedding):

    def __init__(self):
        self.instructor_embeddings = SentenceTransformerEmbeddings(
            model_name="all-MiniLM-L6-v2",
            model_kwargs={"trust_remote_code": True}
        )

    def embed_document(self, documents: list):
        base_dir = r"E:\Project\Flask_Project\Flask_Practtice\RAG_Project\data\embeddings"
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)

        embeddings_file = os.path.join(base_dir, 'embeddings.txt')

        with open(embeddings_file, 'w') as file:
            for document_chunk in documents:
                embedding = self.instructor_embeddings.embed_documents([document_chunk.page_content])[0]
                embedding_data = {
                    "id": str(uuid.uuid4()),
                    "content": document_chunk.page_content,
                    "meta": document_chunk.metadata,
                    "embedding": embedding  
                }
                file.write(json.dumps(embedding_data) + '\n')

        print(f"File Embeddings saved successfully in {embeddings_file}")
