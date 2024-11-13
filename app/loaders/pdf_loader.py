# RAG_Project\app\loaders\pdf_loader.py
from langchain_community.document_loaders import PyPDFLoader
from .base_loader import AbstractDocumentLoader

class PDFLoader(AbstractDocumentLoader):
    def load_document(self, file_path_or_api: str):
        try:
            loader = PyPDFLoader(file_path_or_api)
            
            documents = loader.load_and_split()
            return documents

        except FileNotFoundError:
            print(f"Error: PDF file not found at {file_path_or_api}")
        except PermissionError:
            print(f"Error: Permission denied when accessing the PDF file at {file_path_or_api}")
        except Exception as e:
            print(f"An unexpected error occurred while loading the PDF file: {e}")
        
        return None