# RAG_Project\app\splitters\html_section_splitter.py
from app.splitters.base_splitter import AbstractDocumentSplitter
from langchain_text_splitters import HTMLSectionSplitter

class MyHTMLSectionSplitter(AbstractDocumentSplitter):
    def __init__(self, headers_to_split_on=None):
        if headers_to_split_on is None:
            headers_to_split_on = ["section"]
        self.headers_to_split_on = headers_to_split_on

    def split_document(self, documents: list, chunk_size=100, chunk_overlap=10):
        html_splitter = HTMLSectionSplitter(headers_to_split_on=self.headers_to_split_on)
        split_documents = []
        for document in documents:
            split_texts = html_splitter.split_text(document.page_content)
            for split_doc in split_texts:
                split_doc.metadata.update(document.metadata)
                split_documents.append(split_doc)

        return split_documents

    def split_url(self, url: str, chunk_size=100, chunk_overlap=10):
        html_splitter = HTMLSectionSplitter(headers_to_split_on=self.headers_to_split_on)
        split_documents = html_splitter.split_text_from_url(url)
        return split_documents 