# RAG_Project\app\loaders\api_loader.py
import requests
from requests.exceptions import RequestException
from langchain.schema import Document
from .base_loader import AbstractDocumentLoader

class APILoader(AbstractDocumentLoader):
    def load_document(self, api_path: str):
        try:
            response = requests.get(api_path, timeout=10)

            # Checking HTTP Error
            response.raise_for_status()

            # Parsing response as JSON
            api_data = response.json()

            return [Document(page_content=str(api_data), metadata={"source": api_path})]

        except (requests.Timeout, requests.HTTPError, requests.RequestException) as e:
            print(f"Request error occurred while requesting {api_path}: {e}")
        except ValueError:
            print(f"Error: Unable to parse JSON from the response at {api_path}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        return None