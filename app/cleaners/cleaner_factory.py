# RAG_Project\app\cleaners\cleaner_factory.py
import os
from .base_cleaner import AbstractDocumentCleaner
from .csv_cleaner import CSVCleaner
from .json_cleaner import JSONCleaner
from .api_cleaner import APICleaner
from .pdf_cleaner import PDFCleaner
from .html_cleaner import HTMLCleaner
from .text_cleaner import TextCleaner


def get_cleaner(file_name: str) -> AbstractDocumentCleaner:
    file_extension = os.path.splitext(file_name)[1].lower().strip('.')
    
    Cleaners = {
        'csv': CSVCleaner(),
        'json': JSONCleaner(),
        'pdf': PDFCleaner(),
        'html': HTMLCleaner(),
        'txt': TextCleaner(),
    }

    if file_extension in Cleaners:
        print(f"\n\nFile Extension is - {file_extension}\n")
        return Cleaners[file_extension]
    else:
        raise ValueError(f"Unsupported file extension: {file_extension}")

def get_api_cleaner(api_url: str) -> AbstractDocumentCleaner:
    if api_url.startswith('http'):
        return APICleaner()
    else:
        raise ValueError(f"Invalid API URL: {api_url}")
