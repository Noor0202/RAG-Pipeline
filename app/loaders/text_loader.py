# RAG_Project\app\loaders\text_loader.py
from langchain_community.document_loaders import TextLoader as LC_TextLoader
from .base_loader import AbstractDocumentLoader

class TextLoader(AbstractDocumentLoader):
    def load_document(self, file_path_or_api: str):
        try:
            loader = LC_TextLoader(file_path_or_api, encoding="utf-8")
            print("document is loaded.. from textloader")
            return loader.load()

        except FileNotFoundError:
            print(f"Error: Text file not found at {file_path_or_api}")
        except PermissionError:
            print(f"Error: Permission denied when accessing the text file at {file_path_or_api}")
        except Exception as e:
            print(f"An unexpected error occurred while loading the text file: {e}")
        
        return None