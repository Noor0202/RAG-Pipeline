# Flask_Practtice\RAG_Project\app\retrievals\base_retrieval.py
# Abstract file to load the file and api into RAG Pipeline. 

from abc import ABC, abstractmethod

class AbstractDocumentRetrieval(ABC):
    @abstractmethod
    def retrieve_document(self, query):
        pass
