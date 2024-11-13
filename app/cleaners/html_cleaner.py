# RAG_Project\app\cleaners\html_cleaner.py

import os
from bs4 import BeautifulSoup
from app.cleaners.base_cleaner import AbstractDocumentCleaner

class HTMLCleaner(AbstractDocumentCleaner):
    def clean_document(self, file_path: str):
        file_path = os.path.abspath(file_path)

        if not os.path.isfile(file_path):
            print(f"Error: File not found at {file_path}")
            return
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            cleaned_content = self.clean_html(content)

            base_name = os.path.basename(file_path)
            new_file_name = f"cleaned_{base_name}"
            new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)

            with open(new_file_path, 'w', encoding='utf-8') as file:
                file.write(cleaned_content)
            
            print(f"Cleaned file saved as: {new_file_path}")
            return 1
        
        except IOError as e:
            print(f"Error: Unable to read or write file at {file_path} - {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def clean_html(self, content: str) -> str:
        soup = BeautifulSoup(content, 'html.parser')

        for script_or_style in soup(['script', 'style']):
            script_or_style.decompose() 

        cleaned_text = soup.get_text()

        lines = (line.strip() for line in cleaned_text.splitlines())
        cleaned_lines = [line for line in lines if line]
        
        return "\n".join(cleaned_lines)

# Example usage
# if __name__ == "__main__":
#     # Path to the actual HTML file in the 'data' directory
#     base_dir = r"E:\Project\Flask_Project\Flask_Practtice\RAG_Project\data"
#     html_file_path = os.path.join(base_dir, "html_data.html")  # Updated to correct file name
    
#     # Check if the file exists before proceeding
#     if os.path.exists(html_file_path):
#         cleaner = HTMLCleaner()
#         cleaner.clean_document(html_file_path)
#     else:
#         print(f"Error: The file {html_file_path} does not exist.")
