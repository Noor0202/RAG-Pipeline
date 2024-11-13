# RAG_Project\tests\test_cleaners.py

import os
from app.cleaners.cleaner_factory import get_cleaner, get_api_cleaner


base_dir = r"E:\Project\Flask_Project\Flask_Practtice\RAG_Project\data"

file_paths_or_apis = [
    os.path.join(base_dir, "csv_data.csv"),
    os.path.join(base_dir, "html_data.html"),
    os.path.join(base_dir, "pdf_data.pdf"),
    os.path.join(base_dir, "text_data.txt"),  
    os.path.join(base_dir, "json_data.json"),
    "https://fake-json-api.mock.beeceptor.com/users"  
]

def test_cleaner(file_path_or_api: str):
    print(f"cleaning started for: {file_path_or_api}")

    if file_path_or_api.startswith("http"):
        cleaner = get_api_cleaner(file_path_or_api)
    else:
        cleaner = get_cleaner(file_path_or_api)
    
    # clean the documents
    status = cleaner.clean_document(file_path_or_api)
    
    if status:
        print(f"Extension cleaned successfully from {file_path_or_api}...")
    else:
        print(f"\nFailed to clean documents from {file_path_or_api}")

if __name__ == "__main__":
    for path in file_paths_or_apis:
        test_cleaner(path)