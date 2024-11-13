# RAG_Project\app\loaders\csv_loader.py
from langchain_community.document_loaders.csv_loader import CSVLoader as LC_CSVLoader
from .base_loader import AbstractDocumentLoader

class CSVLoader(AbstractDocumentLoader):
    def load_document(self, file_path_or_api: str):
        try:
            loader = LC_CSVLoader(file_path=file_path_or_api)
            documents = loader.load()
            
            return documents

        except FileNotFoundError:
            print(f"Error: CSV file not found at {file_path_or_api}")
        except PermissionError:
            print(f"Error: Permission denied when accessing the CSV file at {file_path_or_api}")
        except Exception as e:
            print(f"An unexpected error occurred while loading the CSV file: {e}")
        
        return None