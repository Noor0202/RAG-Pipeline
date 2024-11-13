# RAG_Project\app\loaders\loader_factory.py
import os
from .base_loader import AbstractDocumentLoader
from .csv_loader import CSVLoader
from .json_loader import JSONLoader
from .api_loader import APILoader
from .pdf_loader import PDFLoader
from .code_loader import CodeLoader
from .html_loader import HTMLLoader
from .text_loader import TextLoader

PROGRAMMING_EXTENSIONS = [
    "cpp", "go", "java", "kt", "js", "ts", "php", "proto", "py", "rst", 
    "rb", "rs", "scala", "swift", "md", "tex", "sol", "cs", "c", "lua", 
    "pl", "hs"
]

def get_loader(file_name: str) -> AbstractDocumentLoader:
    
    file_extension = os.path.splitext(file_name)[1].lower().strip('.')
    
    if file_extension in PROGRAMMING_EXTENSIONS:
        return CodeLoader()
    
    loaders = {
        'csv': CSVLoader(),
        'json': JSONLoader(),
        'pdf': PDFLoader(),
        'html': HTMLLoader(),
        'txt': TextLoader(),
    }

    if file_extension in loaders:
        print(f"\n\nFile Extension is - {file_extension}\n")
        return loaders[file_extension]
    else:
        raise ValueError(f"Unsupported file extension: {file_extension}")

def get_api_loader() -> AbstractDocumentLoader:
    return APILoader()