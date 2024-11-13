# **RAG Pipeline**

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline to process various document types, generate embeddings, and perform efficient document retrieval. It integrates document loaders, cleaners, splitters, embedding mechanisms, retrieval systems, and chatbots using modular and extensible design patterns, with a focus on **SOLID** principles and **OOP** design.

## **Project Structure**

### **1. app/**
The core application logic, including document loading, cleaning, splitting, embedding, retrieval, and chatbot interaction.

- **`__init__.py`**: Initializes the app (dependency injection, settings).
- **`config.py`**: Contains configuration settings like database connections and API keys.

#### **1.1. loaders/**
Modules responsible for loading various document formats.
- **`base_loader.py`**: Abstract base class for all loaders.
- **`csv_loader.py`**: Loader for CSV files.
- **`json_loader.py`**: Loader for JSON data.
- **`api_loader.py`**: Loader for API data.
- **`pdf_loader.py`**: Loader for PDF files.
- **`code_loader.py`**: Loader for programming code files (e.g., `.py`, `.cpp`).
- **`html_loader.py`**: Loader for HTML documents.
- **`text_loader.py`**: Loader for plain text files.

#### **1.2. cleaners/**
Modules to clean the loaded documents.
- **`base_cleaner.py`**: Abstract base class for all cleaners.
- **`csv_cleaner.py`**: Cleans CSV data (removes noise, formats data).
- **`html_cleaner.py`**: Cleans HTML content (removes tags, scripts).
- **`json_cleaner.py`**: Cleans JSON data.
- **`pdf_cleaner.py`**: Cleans PDF text content.
- **`text_cleaner.py`**: Cleans raw text files.
- **`code_cleaner.py`**: Cleans code files (removes comments, structures code).

#### **1.3. splitters/**
Document splitting strategies to divide documents into manageable chunks.
- **`base_splitter.py`**: Abstract base class for splitting mechanisms.
- **`rcts_splitter.py`**: Implements Recursive Character Text Splitter (RCTS).
- **`html_splitter.py`**: Splits HTML content based on headers and sections.

#### **1.4. embeddings/**
Modules related to embedding generation and storage.
- **`base_embedding.py`**: Abstract base class for embedding strategies.
- **`file_embedding.py`**: Stores embeddings in local files.
- **`db_embedding.py`**: Stores embeddings in a PostgreSQL database using **pgvector**.
- **`json_embedding.py`**: Stores embeddings in the database in **JSON** format.

#### **1.5. retrievals/**
Mechanisms for retrieving stored embeddings.
- **`retrieval_base.py`**: Abstract base class for retrieval methods.
- **`retrieval_model.py`**: Retrieval using pre-trained models (like **Langchain**).
- **`retrieval_json.py`**: Retrieval for embeddings stored in **JSON**.
- **`retrieval_file.py`**: Retrieval for file-stored embeddings.
- **`retrieval_pgvector.py`**: Retrieval for embeddings stored in **pgvector**.

#### **1.6. chatbots/**
Chatbot logic and interfaces.
- **`base_chatbot.py`**: Base class for chatbot interactions.
- **`langchain_bot.py`**: Chatbot implementation using **Langchain**.
- **`free_api_bot.py`**: Chatbot integration using free APIs.

#### **1.7. utils/**
Utility modules for general purposes.
- **`logger.py`**: Logging setup for the entire application.
- **`helpers.py`**: General helper methods and functions.

---

### **2. tests/**
Unit tests for each module in the pipeline to ensure functionality and integrity.
- **`test_loaders.py`**: Unit tests for document loaders.
- **`test_cleaners.py`**: Unit tests for document cleaners.
- **`test_splitters.py`**: Unit tests for document splitting mechanisms.
- **`test_embeddings.py`**: Unit tests for embedding generation and storage.
- **`test_retrievals.py`**: Unit tests for retrieval systems.
- **`test_chatbots.py`**: Unit tests for chatbot interactions.

---

### **3. scripts/**
Standalone Python scripts to run key pipeline tasks.
- **`run_pipeline.py`**: Script to run the entire pipeline from loading to retrieval.
- **`run_retrieval.py`**: Script for document retrieval from stored embeddings.

---

### **4. docs/**
Documentation for each key aspect of the project.
- **`loaders_docs.md`**: Documentation for document loaders.
- **`cleaners_docs.md`**: Documentation for document cleaners.
- **`splitters_docs.md`**: Documentation for document splitting strategies.
- **`embeddings_docs.md`**: Documentation for embedding generation and storage.
- **`retrievals_docs.md`**: Documentation for retrieval mechanisms (JSON, file, pgvector).
- **`chatbots_docs.md`**: Documentation for chatbot integration.
- **`utils_docs.md`**: Documentation for utility functions.
- **`design_overview.md`**: Overview of design principles like **OOP** and **SOLID**.
- **`API_docs.md`**: API documentation for chatbots and retrieval systems.

---

### **5. Configuration and Setup Files**
- **`requirements.txt`**: List of all project dependencies.
- **`setup.py`**: Setup configuration for package installation.
- **`README.md`**: Overview of the project (this file).

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/username/RAG_pipeline_project.git
cd RAG_pipeline_project
```

### **2. Install Dependencies**
Install the required dependencies by running:
```bash
pip install -r requirements.txt
```

### **3. Configure the Project**
Edit the **`app/config.py`** file to configure database settings, API keys, and other paths.

### **4. Run the Pipeline**
You can run the pipeline using the provided script:
```bash
python scripts/run_pipeline.py --document_path "path_to_document"
```

### **5. Run Unit Tests**
To ensure everything works, run the test suite:
```bash
pytest tests/
```

---

## **Key Features**
- **Document Loaders**: Supports CSV, JSON, API, PDF, code, HTML, and text documents.
- **Cleaning**: Custom cleaners for different file formats to ensure clean data for embedding.
- **Splitting**: Divide documents into manageable chunks using strategies like RCTS and HTML-based splitting.
- **Embedding Storage**: Store embeddings in local files, PostgreSQL (using pgvector), or JSON format.
- **Retrieval**: Retrieve document chunks using JSON, file, or pgvector-based methods.
- **Chatbots**: Integrate free chatbot APIs for conversational question-answering based on document embeddings.

---

## **Future Enhancements**
- Add support for additional document formats like **DOCX**.
- Expand chatbot integration with other free APIs and advanced models.
- Implement caching mechanisms for faster retrieval.