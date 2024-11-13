import os
import pandas as pd
from app.cleaners.base_cleaner import AbstractDocumentCleaner

class CSVCleaner(AbstractDocumentCleaner):
    def clean_document(self, file_path: str):
        file_path = os.path.abspath(file_path)
        
        if not os.path.isfile(file_path):
            print(f"Error: File not found at {file_path}")
            return
        
        try:
            df = pd.read_csv(file_path)
            cleaned_df = self.clean_csv(df)
            
            base_name = os.path.basename(file_path)
            new_file_name = f"cleaned_{base_name}"
            new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)
            
            cleaned_df.to_csv(new_file_path, index=False)
            
            print(f"Cleaned file saved as: {new_file_path}")
            return 1
        
        except IOError as e:
            print(f"Error: Unable to read or write file at {file_path} - {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def clean_csv(self, df: pd.DataFrame) -> pd.DataFrame:
        df.dropna(how='all', inplace=True)
        
        for col in df.columns:
            if df[col].dtype == 'object':
                # df[col].fillna('_', inplace=True)
                df.fillna({col: '_'}, inplace=True)
            else:
                # df[col].fillna(0, inplace=True)
                df.fillna({col: 0}, inplace=True)
        
        df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
        
        return df

# Example usage
# if __name__ == "__main__":
#     # Path to the actual CSV file in the 'data' directory
#     base_dir = r"E:\Project\Flask_Project\Flask_Practtice\RAG_Project\data"
#     csv_file_path = os.path.join(base_dir, "csv_data.csv")  # Updated to correct file name
    
#     # Check if the file exists before proceeding
#     if os.path.exists(csv_file_path):
#         cleaner = CSVCleaner()
#         cleaner.clean_document(csv_file_path)
#     else:
#         print(f"Error: The file {csv_file_path} does not exist.")