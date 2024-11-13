# Loaders Documentation

## Overview
This document provides an overview of the document loaders implemented in the RAG Project. These loaders facilitate the retrieval of documents from various formats and sources, making them accessible for further processing.

## Loader Architecture
The loader functionality is based on an abstract base class, `AbstractDocumentLoader`, which defines the interface for all document loader implementations. Each loader class inherits from this abstract class and implements the `load_document` method, which handles the loading of documents from different sources and formats.

## Available Loaders

### AbstractDocumentLoader
- **Location**: `RAG_Project/app/loaders/base_loader.py`
- **Description**: An abstract base class that outlines the method for loading documents.
- **Method**:
  - `load_document(self, file_path_or_api: str)`: Abstract method that must be implemented by subclasses to load a document from a specified file path or API.

### APILoader
- **Location**: `RAG_Project/app/loaders/api_loader.py`
- **Description**: Loads documents from a specified API endpoint.
- **Methods**:
  - `load_document(self, api_path: str)`: Sends a GET request to the API path and retrieves the response as a JSON object. Returns a list of Document instances or logs errors.

### CSVLoader
- **Location**: `RAG_Project/app/loaders/csv_loader.py`
- **Description**: Loads documents from CSV files.
- **Methods**:
  - `load_document(self, file_path_or_api: str)`: Loads documents using the `langchain_community` CSV loader and handles potential file access errors.

### CodeLoader
- **Location**: `RAG_Project/app/loaders/code_loader.py`
- **Description**: Loads documents from code files (e.g., .py, .java).
- **Methods**:
  - `load_document(self, file_path_or_api: str)`: Reads the contents of a specified file and returns it as a Document instance.

### HTMLLoader
- **Location**: `RAG_Project/app/loaders/html_loader.py`
- **Description**: Loads documents from HTML files.
- **Methods**:
  - `load_document(self, file_path_or_api: str)`: Loads documents using the `BeautifulSoup` and handles errors related to file access.
  
### JSONLoader
- **Location**: `RAG_Project/app/loaders/json_loader.py`
- **Description**: Loads documents from JSON files.
- **Methods**:
  - `load_document(self, file_path_or_api: str)`: Loads JSON data using the `langchain_community` JSON loader and returns Document instances.

### PDFLoader
- **Location**: `RAG_Project/app/loaders/pdf_loader.py`
- **Description**: Loads documents from PDF files.
- **Methods**:
  - `load_document(self, file_path_or_api: str)`: Uses the `langchain_community` PDF loader to read and split PDF documents into text.

### TextLoader
- **Location**: `RAG_Project/app/loaders/text_loader.py`
- **Description**: Loads plain text documents.
- **Methods**:
  - `load_document(self, file_path_or_api: str)`: Loads documents from text files with UTF-8 encoding.

## Loader Factory
- **Location**: `RAG_Project/app/loaders/loader_factory.py`
- **Description**: Contains utility functions to obtain appropriate loaders based on file extensions.
- **Functions**:
  - `get_loader(file_name: str)`: Determines the appropriate loader based on the file extension. Raises a ValueError for unsupported extensions.
  - `get_api_loader()`: Returns an instance of `APILoader` for loading documents from API endpoints.

## Usage Examples

### Loading a Document from an API
```python
from app.loaders import get_api_loader

api_loader = get_api_loader()
documents = api_loader.load_document("https://apihere")
```