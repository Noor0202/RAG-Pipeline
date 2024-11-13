# RAG_Project/scripts/run_pipeline.py

import os
from app.loaders.loader_factory import get_loader
from app.splitters.splitter_factory import get_splitter
from app.embeddings.db_embedding import DBEmbedding
from app.embeddings.file_embedding import FILEEmbedding
from app.embeddings.json_embedding import JSONEmbedding
from app.retrievals import PGVectorRetrieval

base_dir = r"E:\Project\Flask_Project\Flask_Practtice\RAG_Project\data"

def document_loader(file_name):
    print(f"Starting to load documents from {file_name}...")
    loader = get_loader(file_name)
    documents = loader.load_document(file_name)
    print(documents)
    if documents:
        print(f"\tDocuments loaded successfully from {file_name}.")
    else:
        raise Exception(f"Failed to load documents from {file_name}.")
    
    return documents

def document_spliter(file,documents):
    print("Starting to split documents...")
    splitter = get_splitter(file)
    chunk_size = int(input("Enter Chunk Size - "))
    chunk_over = int(input("Enter Chunk Overlap - "))
    split_docs = splitter.split_document(documents, chunk_size, chunk_over) 
    
    if split_docs:
        print("\tDocuments split successfully.")
        return split_docs
    else:
        raise Exception("Failed to split documents.")

def generate_embeddings(documents, collection_name, embedding_type):
    print(f"Starting to generate embeddings for {collection_name} using {embedding_type} embedding...")
    
    if embedding_type == "db":
        embedding_generator = DBEmbedding(collection_name)
    elif embedding_type == "file":
        embedding_generator = FILEEmbedding(collection_name)
    elif embedding_type == "json":
        embedding_generator = JSONEmbedding(collection_name)
    else:
        raise Exception("Invalid embedding type selected.")

    embeddings = embedding_generator.embed_document(documents)
    
    if embeddings:
        print(f"Embeddings generated successfully for {collection_name} using {embedding_type} embedding.")
        return embeddings
    else:
        raise Exception(f"Failed to generate embeddings using {embedding_type}.")

def document_retriever(retriever, query):
    print(f"Starting to retrieve documents for query: '{query}'...")
    
    retriever = PGVectorRetrieval(retriever[0],retriever[1])
    if retriever:
        return retriever.retrieve_document(query)
    else:
        return None
    
def run_pipeline():
    print("\n--- Welcome to the RAG Pipeline ---\n")
    
    file_name = input("Enter file name - ")
    file = os.path.join(base_dir,file_name)
        
    print("\nDocument loaded start......")
    document = document_loader(file)
    if document:
        print("\tDocument loaded successfull...")
    else:
        print("\tDocument loaded unsuccessfull...")

    
    print("\nDocument spliter start......")
    split_doc = document_spliter(file,document)
    if split_doc:
        print("\tDocument split successfull...")
    else:
        print("\tDocument ssplit unsuccessfull...")
    
    print("\nDocument embedding start......")
    collect_name = input("Enter Collection name - ")
    embed_doc = generate_embeddings(split_doc,collect_name,"db")
    if embed_doc:
        print("\tDocument embed successfull...")
    else:
        print("\tDocument embed unsuccessfull...")
    
    print("\nDocument retrieval start......")
    query = input("Enter your query here - ")
    result = document_retriever(embed_doc,query)
    if result:
        print("\tDocument retreive successfull...\n\n")
        for i in result:
            print(i)
    else:
        print("\tDocument embed unsuccessfull...")
    
    print("\n\n\t Pipeline Successfull...")

if __name__ == "__main__":
    run_pipeline()
