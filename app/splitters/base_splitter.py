# RAG_Project\app\splitters\base_splitter.py
# Abstract file to load the file and api into RAG Pipeline. 

from abc import ABC, abstractmethod

class AbstractDocumentSplitter(ABC):
    @abstractmethod
    def split_document(self,documents:list,chunk_size:int,chunk_overlap:int):
        pass