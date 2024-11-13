# RAG_Project\app\cleaners\pdf_cleaner.py

import os
import PyPDF2
from app.cleaners.base_cleaner import AbstractDocumentCleaner

class PDFCleaner(AbstractDocumentCleaner):
    def clean_document(self, file_path: str):
        file_path = os.path.abspath(file_path)

        if not os.path.isfile(file_path):
            print(f"Error: File not found at {file_path}")
            return

        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""

                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    text += page.extract_text()

            cleaned_text = self.clean_pdf_text(text)

            base_name = os.path.basename(file_path)
            new_file_name = f"cleaned_{base_name.replace('.pdf', '.txt')}"
            new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)

            with open(new_file_path, 'w', encoding='utf-8') as file:
                file.write(cleaned_text)

            print(f"Cleaned file saved as: {new_file_path}")
            return 1

        except PyPDF2.errors.PdfReadError as e:
            print(f"Error: Unable to read PDF file at {file_path} - {e}")
        except IOError as e:
            print(f"Error: Unable to read or write file at {file_path} - {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def clean_pdf_text(self, text: str) -> str:
        cleaned_text = ' '.join(text.split())
        cleaned_text = cleaned_text.replace('\n', ' ').replace('\r', '')
        return cleaned_text

# # Example usage
# if __name__ == "__main__":
#     # Path to the actual PDF file in the 'data' directory
#     base_dir = r"E:\Project\Flask_Project\Flask_Practtice\RAG_Project\data"
#     pdf_file_path = os.path.join(base_dir, "pdf_data.pdf")  # Correct PDF file name

#     # Check if the file exists before proceeding
#     if os.path.exists(pdf_file_path):
#         cleaner = PDFCleaner()
#         cleaner.clean_document(pdf_file_path)
#     else:
#         print(f"Error: The file {pdf_file_path} does not exist.")
