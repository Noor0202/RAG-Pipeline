# RAG_Project\app\cleaners\api_cleaner.py

import requests
from bs4 import BeautifulSoup
import re
import os
from app.cleaners.base_cleaner import AbstractDocumentCleaner 

class APICleaner(AbstractDocumentCleaner):
    def clean_document(self, api_url: str) -> str:
        try:
            response = requests.get(api_url, timeout=10)
            response.raise_for_status()

            api_data = response.json()
            
            raw_data = str(api_data)
            
            soup = BeautifulSoup(raw_data, 'html.parser')
            
            # Removing unnecessary tags and metadata
            for tag in soup(['script', 'style']):
                tag.decompose()
            
            # Getting the cleaned text
            cleaned_text = soup.get_text()
            
            # Cleaning text data
            cleaned_text = self.clean_text(cleaned_text)
            
            # Define file path
            base_dir = os.path.join(os.path.dirname(__file__), '../../data')
            os.makedirs(base_dir, exist_ok=True)
            file_path = os.path.join(base_dir, 'api_clean.txt')
            
            # Write cleaned data to file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(cleaned_text)
            
            print(f"Cleaned data has been saved to {file_path}")
            return file_path
        
        except requests.RequestException as e:
            print(f"Request error occurred while requesting {api_url}: {e}")
        except ValueError:
            print(f"Error: Unable to parse JSON from the response at {api_url}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        return None

    def clean_text(self, text: str) -> str:
        # Remove special characters and extra whitespace
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'[^\w\s]', '', text)
        
        # Additional text normalization (lowercasing)
        text = text.lower()
        
        return text
    
# # Example usage
# if __name__ == "__main__":
#     api_url = "https://fake-json-api.mock.beeceptor.com/users"  # Replace with your API URL
#     cleaner = APICleaner()
#     cleaner.clean_document(api_url)