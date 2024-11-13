# Splitters Documentation

## Overview
This document provides an overview of the document splitting mechanisms implemented in the RAG Project. Document splitters are crucial for processing large documents into manageable chunks, facilitating better retrieval and handling in the RAG pipeline.

## Splitting Architecture
The splitting functionality is built around an abstract base class, `AbstractDocumentSplitter`, which defines the interface for all splitter implementations. Each splitter class implements the `split_document` method to handle the splitting of documents based on specific criteria.

## Available Splitter Classes

### AbstractDocumentSplitter
- **Location**: `RAG_Project/app/splitters/base_splitter.py`
- **Description**: An abstract base class that outlines the method for document splitting.
- **Method**:
  - `split_document(self, documents: list, chunk_size: int, chunk_overlap: int)`: Abstract method that must be implemented by subclasses to split documents.

### CharSplitter
- **Location**: `RAG_Project/app/splitters/char_splitter.py`
- **Description**: Splits documents based on character count.
- **Method**:
  - `split_document(self, documents: list, chunk_size: int, chunk_overlap: int)`: Splits the provided documents into chunks based on specified character limits.

### CodeSplitter
- **Location**: `RAG_Project/app/splitters/code_splitter.py`
- **Description**: Splits code files into chunks based on language-specific rules.
- **Method**:
  - `split_document(self, documents: list, chunk_size: int, chunk_overlap: int)`: Splits documents based on the file's programming language.

### HTMLHeaderSplitter
- **Location**: `RAG_Project/app/splitters/html_header_splitter.py`
- **Description**: Splits HTML documents based on header tags.
- **Constructor**:
  - `__init__(self, headers_to_split_on=None)`: Initializes with a list of HTML headers to split on (default: h1-h6).
- **Method**:
  - `split_document(self, documents: list, chunk_size=100, chunk_overlap=10)`: Splits HTML documents based on specified headers.

### MyHTMLSectionSplitter
- **Location**: `RAG_Project/app/splitters/html_section_splitter.py`
- **Description**: Splits HTML documents into sections.
- **Constructor**:
  - `__init__(self, headers_to_split_on=None)`: Initializes with a list of HTML sections to split on (default: "section").
- **Method**:
  - `split_document(self, documents: list, chunk_size=100, chunk_overlap=10)`: Splits HTML documents into sections.

### RCTSSplitter
- **Location**: `RAG_Project/app/splitters/rcts_splitter.py`
- **Description**: Uses recursive character splitting to handle various document types.
- **Method**:
  - `split_document(self, documents: list, chunk_size: int, chunk_overlap: int)`: Splits documents into chunks based on specified character limits and various separators.

## Usage Examples

### Splitting Documents with RCTSSplitter
```python
from app.splitters import get_splitter

# Specify the file path
file_path = "example.txt"

# Get the appropriate splitter
splitter = get_splitter(file_path)

# Example documents to split
documents = [
    Document(page_content="This is the first part of the document.", metadata={"source": "example.txt"}),
    Document(page_content="This is the second part of the document.", metadata={"source": "example.txt"})
]

# Split the documents
split_documents = splitter.split_document(documents, chunk_size=50, chunk_overlap=10)

# Display the split documents
for doc in split_documents:
    print(doc.page_content)
```