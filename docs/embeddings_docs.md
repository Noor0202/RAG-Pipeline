# Embeddings Documentation

## Overview
This document provides an overview of the embedding classes implemented in the RAG Project. These classes are responsible for generating embeddings from various document sources and storing them in different formats or databases.

## Embedding Architecture
The embedding functionality is structured around an abstract base class, `AbstractDocumentEmbedding`, which defines the interface for all specific embedding implementations. Each embedding class inherits from this abstract class and implements the `embed_document` method, which performs the specific embedding operation based on the document source.

## Available Embeddings

### AbstractDocumentEmbedding
- **Location**: `RAG_Project/app/embeddings/base_embedding.py`
- **Description**: An abstract base class that defines the method for embedding documents.
- **Method**:
  - `embed_document(self, documents: list)`: Abstract method that must be implemented by subclasses to generate embeddings for the provided documents.

### DBEmbedding
- **Location**: `RAG_Project/app/embeddings/db_embedding.py`
- **Description**: Generates embeddings and stores them in a PostgreSQL database using the PGVector vector store.
- **Constructor**:
  - `__init__(self, COLLECTION_NAME)`: Initializes the DBEmbedding class with a specified collection name and establishes a connection string.
- **Methods**:
  - `embed_document(self, documents: list)`: Generates embeddings for the provided documents and inserts them into the specified PGVector collection.

### JSONEmbedding
- **Location**: `RAG_Project/app/embeddings/json_embedding.py`
- **Description**: Generates embeddings and stores them in a PostgreSQL database in JSON format.
- **Constructor**:
  - `__init__(self)`: Initializes the JSONEmbedding class and establishes a database connection.
- **Methods**:
  - `embed_document(self, documents: list)`: Generates embeddings for the provided documents and inserts them into a PostgreSQL table.
  - `_create_table(self, table_query)`: Helper method to create the embeddings table in the database if it does not exist.

### FILEEmbedding
- **Location**: `RAG_Project/app/embeddings/file_embedding.py`
- **Description**: Generates embeddings and saves them to a text file.
- **Constructor**:
  - `__init__(self)`: Initializes the FILEEmbedding class.
- **Methods**:
  - `embed_document(self, documents: list)`: Generates embeddings for the provided documents and saves them in a specified text file.

## Usage Examples

### Embedding Documents and Storing in a Database
```python
from app.embeddings.db_embedding import DBEmbedding

db_embedding = DBEmbedding(COLLECTION_NAME='my_collection')
documents = [...]  # List of document chunks
db_embedding.embed_document(documents)
```