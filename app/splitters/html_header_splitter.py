# RAG_Project\app\splitters\html_header_splitter.py
from app.splitters.base_splitter import AbstractDocumentSplitter
from langchain.text_splitter import HTMLHeaderTextSplitter

class HTMLHeaderSplitter(AbstractDocumentSplitter):
    def __init__(self, headers_to_split_on=None):
        if headers_to_split_on is None:
            headers_to_split_on = ["h1", "h2", "h3", "h4", "h5", "h6"]
        self.headers_to_split_on = headers_to_split_on
    
    def split_document(self, documents: list, chunk_size=100, chunk_overlap=10):
        html_splitter = HTMLHeaderTextSplitter(headers_to_split_on=self.headers_to_split_on)
        split_documents = []
        for document in documents:
            split_texts = html_splitter.split_text(document.page_content)
            for split_doc in split_texts:
                split_doc.metadata.update(document.metadata)
                split_documents.append(split_doc)

        return split_documents

    def split_url(self, url: str, chunk_size=100, chunk_overlap=10):
        html_splitter = HTMLHeaderTextSplitter(headers_to_split_on=self.headers_to_split_on)
        split_documents = html_splitter.split_text_from_url(url)
        return split_documents