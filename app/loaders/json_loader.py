# RAG_Project\app\loaders\json_loader.py
from langchain_community.document_loaders import JSONLoader as LC_JSONLoader
from .base_loader import AbstractDocumentLoader

class JSONLoader(AbstractDocumentLoader):
    def load_document(self, file_path_or_api: str):
        try:
            loader = LC_JSONLoader(
                file_path=file_path_or_api,
                jq_schema=".",  
                text_content=False,
                json_lines=False
            )
            
            documents = loader.load()
            return documents

        except FileNotFoundError:
            print(f"Error: JSON file not found at {file_path_or_api}")
        except PermissionError:
            print(f"Error: Permission denied when accessing the JSON file at {file_path_or_api}")
        except ValueError:
            print(f"Error: Failed to parse JSON content from {file_path_or_api}")
        except Exception as e:
            print(f"An unexpected error occurred while loading the JSON file: {e}")
        
        return None