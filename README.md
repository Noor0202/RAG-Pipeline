# **RAG Pipeline**

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline designed to process various document types, generate embeddings, and perform efficient document retrieval. It integrates document loaders, cleaners, splitters, embedding mechanisms, retrieval systems, and chatbots, adhering to modular and extensible design patterns based on **SOLID** principles and **OOP** design.

## **Project Structure**

### **1. app/**
The core application logic, encompassing document loading, cleaning, splitting, embedding, retrieval, and chatbot interaction.

- **`__init__.py`**: Initializes the app (dependency injection, settings).
- **`config.py`**: Contains configuration settings such as database connections and API keys.

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
- **`html_header_splitter.py`**: Splits HTML content based on headers.
- **`html_section_splitter.py`**: Splits HTML content based on sections.
- **`char_splitter.py`**: Splits text into chunks based on character count.
- **`code_splitter.py`**: Specialized splitter for programming code files.

#### **1.4. embeddings/**
Modules related to embedding generation and storage.
- **`base_embedding.py`**: Abstract base class for embedding strategies.
- **`file_embedding.py`**: Stores embeddings in local files.
- **`db_embedding.py`**: Stores embeddings in a PostgreSQL database using **pgvector**.
- **`json_embedding.py`**: Stores embeddings in the database in **JSON** format.

#### **1.5. retrievals/**
Mechanisms for retrieving stored embeddings.
- **`base_retrieval.py`**: Abstract base class for retrieval methods.
- **`retrieval_VectorBased.py`**: Implements vector-based retrieval using **pgvector**.
- **`retrieval_KeywordBased.py`**: Keyword-based retrieval method.
- **`retrieval_DenseBased.py`**: Implements dense retrieval methods.
- **`retrieval_HybridBased.py`**: Hybrid retrieval combining multiple strategies.
- **`retrieval_SequentialBased.py`**: Sequential retrieval strategy.
- **`retrieval_ContextualBased.py`**: Contextual retrieval method.
- **`retrieval_DensePassageBased.py`**: Dense passage retrieval.
- **`retrieval_DocumentBased.py`**: Document-based retrieval approach.
- **`retrieval_PseudoRelevanceFeedbackBased.py`**: Retrieval with pseudo-relevance feedback.

#### **1.6. chatbots/ coming soon**
Chatbot logic and interfaces.
- **`base_chatbot.py`**: Base class for chatbot interactions.
- **`openai_bot.py`**: Chatbot implementation using **OpenAI**.
- **`free_api_bot.py`**: Chatbot integration using free APIs.

---

### **2. tests/**
Unit tests for each module in the pipeline to ensure functionality and integrity.
- **`test_loaders.py`**: Unit tests for document loaders.
- **`test_cleaners.py`**: Unit tests for document cleaners.
- **`test_splitters.py`**: Unit tests for document splitting mechanisms.
- **`test_embeddings.py`**: Unit tests for embedding generation and storage.
- **`test_retrievals.py`**: coming soon.
- **`test_chatbots.py`**: coming soon.

---

### **3. scripts/**
Standalone Python scripts to run key pipeline tasks.
- **`run_pipeline.py`**: Script to run the entire pipeline from loading to retrieval.
- **`run_retrieval.py`**: coming soon.

---

### **4. docs/**
Documentation for each key aspect of the project.
- **`loaders_docs.md`**: Documentation for document loaders.
- **`cleaners_docs.md`**: Documentation for document cleaners.
- **`splitters_docs.md`**: Documentation for document splitting strategies.
- **`embeddings_docs.md`**: Documentation for embedding generation and storage.
- **`retrievals_docs.md`**: Documentation for retrieval mechanisms (JSON, file, pgvector).
- **`chatbots_docs.md`**: coming soon.
- **`design_overview.md`**: Overview of design principles like **OOP** and **SOLID**.
- **`API_docs.md`**: coming soon.

---

### **Setup Instructions**

1. **Set Up the Environment**
   Edit the **`app/__init__.py`** file to configure database settings, API keys, and other paths.

2. **Set Your Path**
   Set the PYTHONPATH to the project directory:
   ```bash
   set PYTHONPATH=your_path/RAG_Project
   ```

3. **Run the Pipeline**
   You can run the pipeline using the provided script:
   ```bash
   python scripts/run_pipeline.py
   ```

4. **Run Unit Tests**
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

--- 