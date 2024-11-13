# RAG_Project\app\loaders\base_loader.py
# Abstract file to load the file and api into RAG Pipeline. 

from abc import ABC, abstractmethod

class AbstractDocumentLoader(ABC):
    @abstractmethod
    def load_document(self, file_path_or_api: str):
        pass