# RAG_Project\tests\test_embeddings.py
import os
from app.embeddings.base_embedding import AbstractDocumentEmbedding
from app.embeddings.db_embedding import DBEmbedding
from app.embeddings.file_embedding import FILEEmbedding
from app.embeddings.json_embedding import JSONEmbedding
from app.loaders.loader_factory import get_loader
from app.splitters.splitter_factory import get_splitter

base_dir = r"E:\Project\Flask_Project\Flask_Practtice\RAG_Project\data"

file_paths = [
    os.path.join(base_dir, "csv_data.csv"),
    os.path.join(base_dir, "html_data.html"),
    os.path.join(base_dir, "pdf_data.pdf"),
    os.path.join(base_dir, "text_data.txt"),
    os.path.join(base_dir, "json_data.json"),
    os.path.join(base_dir, "python_data.py"),
]

embedding_types = {
    "db": DBEmbedding(),
    "file": FILEEmbedding(),
    "json": JSONEmbedding(),
}

def test_loader(file_path):
    loader = get_loader(file_path)
    documents = loader.load_document(file_path)
    
    if documents:
        print(f"Documents loaded successfully from {file_path}...")
        return documents
    else:
        print(f"Failed to load documents from {file_path}")
        return None

def split_documents(documents):
    splitter = get_splitter()  
    split_docs = splitter.split_documents(documents)
    
    if split_docs:
        print("Documents split successfully.")
        return split_docs
    else:
        print("Failed to split documents.")
        return None

def generate_embeddings(documents, file_path):
    for embedding_name, embedding_generator in embedding_types.items():
        embeddings = embedding_generator.generate_embeddings(documents)
        
        if embeddings:
            print(f"Embeddings generated successfully for {file_path} using {embedding_name} embedding.")
        else:
            print(f"Failed to generate embeddings for {file_path} using {embedding_name} embedding.")

if __name__ == "__main__":
    for path in file_paths:
        print(f"\n\n\t\t Starting Embedding Process for {path}\n\n")
        
        documents = test_loader(path)
        
        if documents:
            split_docs = split_documents(documents)

            if split_docs:
                generate_embeddings(split_docs, path)
            else:
                print(f"Skipping embedding generation for {path} due to failed splitting.")
        else:
            print(f"Skipping embedding generation for {path} due to failed loading.")
