# RAG_Project/app/splitters/splitter_factory.py

from .base_splitter import AbstractDocumentSplitter
from .rcts_splitter import RCTSSplitter
from .html_header_splitter import HTMLHeaderSplitter
from .html_section_splitter import MyHTMLSectionSplitter
from .char_splitter import CharSplitter
from .code_splitter import CodeSplitter

def get_splitter(file_path: str):
    # Extract file extension from the file path
    extension = file_path.split(".")[-1].lower()
    
    # Mapping of file extensions to splitters
    splitter_mapping = {
        "txt": RCTSSplitter(),
        "csv": RCTSSplitter(),
        "json": RCTSSplitter(),
        "pdf": RCTSSplitter(),
        "html": HTMLHeaderSplitter(),
        "md": CharSplitter(),
        "py": CodeSplitter(),
        "js": CodeSplitter(),
        "java": CodeSplitter(),
        "cpp": CodeSplitter()
    }

    if extension in splitter_mapping:
        return splitter_mapping[extension]
    else:
        raise ValueError(f"Unsupported file type: {extension}")