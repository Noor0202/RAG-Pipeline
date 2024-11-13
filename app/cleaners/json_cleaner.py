# RAG_Project\app\cleaners\json_cleaner.py

import os
import json
from app.cleaners.base_cleaner import AbstractDocumentCleaner

class JSONCleaner(AbstractDocumentCleaner):
    def clean_document(self, file_path: str):
        file_path = os.path.abspath(file_path)

        if not os.path.isfile(file_path):
            print(f"Error: File not found at {file_path}")
            return

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            cleaned_data = self.clean_json(data)

            base_name = os.path.basename(file_path)
            new_file_name = f"cleaned_{base_name}"
            new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)

            with open(new_file_path, 'w', encoding='utf-8') as file:
                json.dump(cleaned_data, file, indent=4)
            
            print(f"Cleaned file saved as: {new_file_path}")
            return 1

        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON format in file {file_path} - {e}")
        except IOError as e:
            print(f"Error: Unable to read or write file at {file_path} - {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def clean_json(self, data: dict) -> dict:
        cleaned_data = self._clean_dict(data)
        return cleaned_data

    def _clean_dict(self, data: dict) -> dict:
        cleaned_dict = {}
        for key, value in data.items():
            cleaned_key = key.strip().lower().replace(' ', '_')

            if isinstance(value, dict):
                cleaned_value = self._clean_dict(value)
            elif isinstance(value, list):
                cleaned_value = self._clean_list(value)
            else:
                cleaned_value = value if value not in [None, ""] else "_"
            
            cleaned_dict[cleaned_key] = cleaned_value

        return cleaned_dict

    def _clean_list(self, data: list) -> list:
        cleaned_list = []
        for item in data:
            if isinstance(item, dict):
                cleaned_item = self._clean_dict(item)
            elif isinstance(item, list):
                cleaned_item = self._clean_list(item)
            else:
                cleaned_item = item if item not in [None, ""] else "_"

            cleaned_list.append(cleaned_item)

        return cleaned_list

# Example usage
# if __name__ == "__main__":
#     # Path to the actual JSON file in the 'data' directory
#     base_dir = r"E:\Project\Flask_Project\Flask_Practtice\RAG_Project\data"
#     json_file_path = os.path.join(base_dir, "json_data.json")  # Correct JSON file name

#     # Check if the file exists before proceeding
#     if os.path.exists(json_file_path):
#         cleaner = JSONCleaner()
#         cleaner.clean_document(json_file_path)
#     else:
#         print(f"Error: The file {json_file_path} does not exist.")
