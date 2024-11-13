# File: RAG_Project\tests\test_splitters.py

import os
from app.splitters.splitter_factory import get_splitter
from app.loaders.loader_factory import get_loader

base_dir = r"E:\Project\Flask_Project\Flask_Practtice\RAG_Project\data"

file_paths_or_apis = [
    os.path.join(base_dir, "csv_data.csv"),
    os.path.join(base_dir, "html_data.html"),
    os.path.join(base_dir, "pdf_data.pdf"),
    os.path.join(base_dir, "text_data.txt"),  
    os.path.join(base_dir, "json_data.json"),
    os.path.join(base_dir, "python_data.py"),
    os.path.join(base_dir, "README.md")
]

def test_loader(file_path_or_api: str):
    loader = get_loader(file_path_or_api)
    documents = loader.load_document(file_path_or_api)
    
    if documents:
        print(f"Documents loaded successfully from {file_path_or_api}...")
        return documents
    else:
        print(f"Failed to load documents from {file_path_or_api}")
        return None

def test_splitter(documents, file_path_or_api, chunk_size=30, chunk_overlap=5):
    print(f"Splitting started for: {file_path_or_api}")
    splitter = get_splitter(file_path_or_api)

    if splitter is None:
        print(f"No suitable splitter found for {file_path_or_api}")
        return

    try:
        split_docs = splitter.split_document(documents, chunk_size, chunk_overlap)
        print(split_docs[0].page_content)
        print("Document Split Successfully...!")

    except ValueError as e:
        print(f"Error splitting document from {file_path_or_api}: {e}")

if __name__ == "__main__":
    for path in file_paths_or_apis:
        print(f"\n\n\t\t Starting Process for {path}\n\n")
        
        documents = test_loader(path)
        
        if documents:
            test_splitter(documents, path)
        else:
            print(f"Skipping splitter test for {path} due to failed loading.")
