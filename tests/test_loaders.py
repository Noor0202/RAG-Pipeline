# RAG_Project\tests\test_loaders.py

import os
from app.loaders.loader_factory import get_loader, get_api_loader

base_dir = r"E:\Project\Flask_Project\Flask_Practtice\RAG_Project\data"

file_paths_or_apis = [
    os.path.join(base_dir, "csv_data.csv"),
    os.path.join(base_dir, "html_data.html"),
    os.path.join(base_dir, "pdf_data.pdf"),
    os.path.join(base_dir, "text_data.txt"),  
    os.path.join(base_dir, "json_data.json"),
    os.path.join(base_dir, "python_data.py"),
    "https://fake-json-api.mock.beeceptor.com/users"  
]

def test_loader(file_path_or_api: str):
    print(f"Loading started for: {file_path_or_api}")

    if file_path_or_api.startswith("http"):
        loader = get_api_loader()
    else:
        loader = get_loader(file_path_or_api)
    
    documents = loader.load_document(file_path_or_api)
    
    if documents:
        print(f"Extension loaded successfully from {file_path_or_api}...")
        print(type(documents))
    else:
        print(f"\nFailed to load documents from {file_path_or_api}")

if __name__ == "__main__":
    for path in file_paths_or_apis:
        test_loader(path)