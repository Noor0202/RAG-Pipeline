# Retrievals Documentation

## Overview
This document provides an overview of the retrieval mechanism implemented in the RAG Project. The retrieval system allows for efficient document retrieval based on queries, leveraging vector-based similarity search techniques.

## Retrieval Architecture
The retrieval functionality is built on an abstract base class, `AbstractDocumentRetrieval`, which defines the interface for all retrieval implementations. Each retrieval class implements the `retrieve_document` method to handle query-based document retrieval.

## Available Retrieval Classes

### AbstractDocumentRetrieval
- **Location**: `RAG_Project/app/retrievals/base_retrieval.py`
- **Description**: An abstract base class that outlines the method for document retrieval.
- **Method**:
  - `retrieve_document(self, query)`: Abstract method that must be implemented by subclasses to retrieve documents based on a provided query.

### PGVectorRetrieval
- **Location**: `RAG_Project/app/retrievals/retrieval_VectorBased.py`
- **Description**: Implements vector-based retrieval using PostgreSQL with PGVector. This class allows querying a vector store to find documents similar to the input query.
- **Constructor**:
  - `__init__(self, collection_name, mydb)`: Initializes the PGVectorRetrieval with a collection name and a database connection.
- **Methods**:
  - `retrieve_document(self, query, top_k=4)`: Retrieves documents that are most similar to the input query. Returns a list of the top `k` document contents.

## Usage Examples

### Retrieving Documents with PGVector
```python
from app.retrievals import PGVectorRetrieval
from app import get_connection  # Assuming you have a function to get DB connection

# Initialize the database connection and collection name
mydb = get_connection()
collection_name = "my_document_collection"

# Create an instance of PGVectorRetrieval
retriever = PGVectorRetrieval(collection_name=collection_name, mydb=mydb)

# Retrieve documents based on a query
query = "What are the benefits of using vector databases?"
results = retriever.retrieve_document(query, top_k=4)

# Display the retrieved documents
for doc in results:
    print(doc)
```