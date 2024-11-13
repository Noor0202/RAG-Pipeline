# RAG_Project\app\loaders\code_loader.py
from langchain.schema import Document
from .base_loader import AbstractDocumentLoader

class CodeLoader(AbstractDocumentLoader):
    def load_document(self, file_path_or_api: str):
        try:
            with open(file_path_or_api, 'r') as file:
                content = file.read()

            return [Document(page_content=content, metadata={"source": file_path_or_api})]

        except FileNotFoundError:
            print(f"Error: File not found at {file_path_or_api}")
        except PermissionError:
            print(f"Error: Permission denied when accessing the file at {file_path_or_api}")
        except Exception as e:
            print(f"An unexpected error occurred while loading the file: {e}")
        
        return None