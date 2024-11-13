# Cleaners Documentation

## Overview
This document provides an overview of the various data cleaning classes implemented in the RAG Project. These cleaners are responsible for processing and normalizing data from different file formats and sources, ensuring that the data is suitable for further processing in the RAG pipeline.

## Cleaner Architecture
The cleaning functionality is implemented using an abstract base class `AbstractDocumentCleaner`, which defines the interface for all specific cleaner implementations. Each cleaner class inherits from this abstract class and implements the `clean_document` method, which performs the specific cleaning operation based on the file type or data source.

## Available Cleaners

### AbstractDocumentCleaner
- **Location**: `RAG_Project/app/cleaners/base_cleaner.py`
- **Description**: An abstract base class that enforces the implementation of the `clean_document` method in all derived cleaners.
- **Method**:
  - `clean_document(self, file_path_or_api: str)`: Abstract method to be implemented by subclasses.

### APICleaner
- **Location**: `RAG_Project/app/cleaners/api_cleaner.py`
- **Description**: Cleans data retrieved from a specified API endpoint.
- **Methods**:
  - `clean_document(self, api_url: str)`: Fetches data from the given API URL, cleans it, and saves the cleaned data to a text file.
  - `clean_text(self, text: str)`: Normalizes and cleans the text data by removing special characters and extra whitespace.

### CSVCleaner
- **Location**: `RAG_Project/app/cleaners/csv_cleaner.py`
- **Description**: Cleans CSV files by handling missing values and normalizing column names.
- **Methods**:
  - `clean_document(self, file_path: str)`: Reads a CSV file, cleans it, and saves the cleaned version.
  - `clean_csv(self, df: pd.DataFrame)`: Performs cleaning operations on the DataFrame.

### JSONCleaner
- **Location**: `RAG_Project/app/cleaners/json_cleaner.py`
- **Description**: Cleans JSON files by normalizing keys and removing empty values.
- **Methods**:
  - `clean_document(self, file_path: str)`: Reads a JSON file, cleans it, and saves the cleaned version.
  - `clean_json(self, data: dict)`: Cleans the provided dictionary.
  - `_clean_dict(self, data: dict)`: Helper method to clean dictionary items.
  - `_clean_list(self, data: list)`: Helper method to clean list items.

### PDFCleaner
- **Location**: `RAG_Project/app/cleaners/pdf_cleaner.py`
- **Description**: Extracts and cleans text from PDF files.
- **Methods**:
  - `clean_document(self, file_path: str)`: Reads a PDF file, extracts text, cleans it, and saves the cleaned version.
  - `clean_pdf_text(self, text: str)`: Normalizes and cleans the extracted text.

### HTMLCleaner
- **Location**: `RAG_Project/app/cleaners/html_cleaner.py`
- **Description**: Cleans HTML files by removing scripts, styles, and extracting text.
- **Methods**:
  - `clean_document(self, file_path: str)`: Reads an HTML file, cleans it, and saves the cleaned version.
  - `clean_html(self, content: str)`: Normalizes and cleans the HTML content.

### TextCleaner
- **Location**: `RAG_Project/app/cleaners/text_cleaner.py`
- **Description**: Cleans plain text files by removing unnecessary whitespace.
- **Methods**:
  - `clean_document(self, file_path: str)`: Reads a text file, cleans it, and saves the cleaned version.
  - `clean_text(self, text: str)`: Normalizes and cleans the text.

## Cleaner Factory
- **Location**: `RAG_Project/app/cleaners/cleaner_factory.py`
- **Description**: Provides a factory function to retrieve the appropriate cleaner based on the file extension or API URL.
- **Functions**:
  - `get_cleaner(file_name: str)`: Returns the appropriate cleaner instance based on the file extension.
  - `get_api_cleaner(api_url: str)`: Returns an `APICleaner` instance if the provided URL is valid.

## Usage Examples

### Cleaning a CSV File
```python
from app.cleaners.cleaner_factory import get_cleaner

cleaner = get_cleaner('data.csv')
cleaner.clean_document('data.csv')
```