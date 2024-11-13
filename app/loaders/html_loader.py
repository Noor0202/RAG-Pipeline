# RAG_Project\app\loaders\html_loader.py
from langchain_community.document_loaders import BSHTMLLoader
from .base_loader import AbstractDocumentLoader
from bs4 import BeautifulSoup

class HTMLLoader(AbstractDocumentLoader):
    def load_document(self, file_path_or_api: str):
        try:
            loader = BSHTMLLoader(file_path_or_api)
            documents = loader.load()

            return documents

        except FileNotFoundError:
            print(f"Error: HTML file not found at {file_path_or_api}")
        except PermissionError:
            print(f"Error: Permission denied when accessing the HTML file at {file_path_or_api}")
        except Exception as e:
            print(f"An unexpected error occurred while loading the HTML file: {e}")

        return None

class HTMLTagLoader(AbstractDocumentLoader):
    def __init__(self, tags):
        self.tags = tags

    def load_document(self, file_path_or_api: str):
        try:
            html_loader = BSHTMLLoader(file_path_or_api)
            content = html_loader.load()
            
            soup = BeautifulSoup(content[0].page_content, 'html.parser')
            
            filtered_content = []

            for tag in self.tags:
                filtered_content.extend(soup.find_all(tag))

            documents = [doc.get_text() for doc in filtered_content]

            return [BeautifulSoup(content, 'html.parser').get_text() for content in documents]

        except FileNotFoundError:
            print(f"Error: HTML file not found at {file_path_or_api}")
        except PermissionError:
            print(f"Error: Permission denied when accessing the HTML file at {file_path_or_api}")
        except Exception as e:
            print(f"An unexpected error occurred while processing HTML tags: {e}")

        return None