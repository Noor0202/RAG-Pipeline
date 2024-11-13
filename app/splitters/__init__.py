# RAG_Project\app\splitters\__init__.py

# Import all splitters to make them available when the package is imported
from .base_splitter import AbstractDocumentSplitter
from .html_header_splitter import HTMLHeaderSplitter
from .html_section_splitter import MyHTMLSectionSplitter
from .rcts_splitter import RCTSSplitter
from .char_splitter import CharSplitter
from .code_splitter import CodeSplitter
from .splitter_factory import get_splitter

__all__ = [
    "AbstractDocumentSplitter",
    "HTMLHeaderSplitter",
    "MyHTMLSectionSplitter",
    "RCTSSplitter"
    "CharSplitter",
    "CodeSplitter",
    "get_splitter"
    # "get_api_splitter"
]
