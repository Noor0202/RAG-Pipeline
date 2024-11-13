# RAG_Project\app\splitters\char_splitter.py
# Import necessary classes
from app.splitters.base_splitter import AbstractDocumentSplitter
from langchain_text_splitters import CharacterTextSplitter

class CharSplitter(AbstractDocumentSplitter):
    def split_document(self, documents: list, chunk_size: int, chunk_overlap: int):
        text_splitter = CharacterTextSplitter(
            separator="\n\n",
            chunk_size = chunk_size,
            chunk_overlap = chunk_overlap,
            length_function = len,
            is_separator_regex=False,
        )
        split_documents = []
        
        for document in documents:
            if isinstance(document.page_content, str):
                split_texts = text_splitter.create_documents([document.page_content])
                for split_doc in split_texts:
                    split_doc.metadata.update(document.metadata)
                    split_documents.append(split_doc)
            else:
                print(f"Skipping document with invalid content type: {type(document.page_content)}")
        return split_documents