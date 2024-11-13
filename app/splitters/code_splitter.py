# RAG_Project\app\splitters\code_splitter.py
# Import necessary classes
from langchain.schema import Document
from app.splitters.base_splitter import AbstractDocumentSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

class CodeSplitter(AbstractDocumentSplitter):
    def split_document(self, documents: list, chunk_size: int, chunk_overlap: int):
        extension = documents[0].metadata["source"].split(".")[-1]
        
        language_mapping = {
            "cpp": Language.CPP, "go": Language.GO, "java": Language.JAVA,
            "kt": Language.KOTLIN, "js": Language.JS, "ts": Language.TS,
            "php": Language.PHP, "proto": Language.PROTO, "py": Language.PYTHON,
            "rst": Language.RST, "rb": Language.RUBY, "rs": Language.RUST,
            "scala": Language.SCALA, "swift": Language.SWIFT, "md": Language.MARKDOWN,
            "tex": Language.LATEX, "html": Language.HTML, "sol": Language.SOL,
            "cs": Language.CSHARP, "c": Language.C, "lua": Language.LUA,
            "pl": Language.PERL, "hs": Language.HASKELL
        }

        if extension in language_mapping:
            code_splitter = RecursiveCharacterTextSplitter.from_language(
                language=language_mapping[extension],
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap
            )

            split_documents = []
            
            for document in documents:
                if isinstance(document.page_content, str):
                    split_texts = code_splitter.create_documents([document.page_content])
                    
                    for split_doc in split_texts:
                        split_doc.metadata.update(document.metadata)
                        split_documents.append(split_doc)
                else:
                    print(f"Skipping document with invalid content type: {type(document.page_content)}")
            
            return split_documents
        else:
            raise ValueError("Unsupported file format for code splitting.")