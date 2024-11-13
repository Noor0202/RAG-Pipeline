# RAG_Project\app\cleaners\base_cleaner.py
# Abstract file to load the file and api into RAG Pipeline. 

from abc import ABC, abstractmethod

class AbstractDocumentCleaner(ABC):
    @abstractmethod
    def clean_document(self,file_path_or_api:str):
        pass