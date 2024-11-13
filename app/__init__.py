# from langchain.vectorstores import PGVector
from langchain_community.vectorstores import PGVector
import psycopg2

# Define database parameters
mydriver = "psycopg2"
myhost = "localhost"
myport = 5432
mydatabase = "Sample_DataBase"
myuser = "postgres"
mypassword = "root"

def get_connection_string():
    try:
        connection_string = PGVector.connection_string_from_db_params(
            driver=mydriver,
            host=myhost,
            port=myport,
            database=mydatabase,
            user=myuser,
            password=mypassword
        )
        print("Connection string generated successfully.")
        return connection_string
    except Exception as e:
        print(f"Error generating connection string: {e}")
        return None

def get_connection():
    try:
        conn = psycopg2.connect(
            dbname = mydatabase,
            user = myuser,
            password = mypassword,
            host = myhost,
            port = myport
        )
        print("Database connection established successfully.")
        return conn
    except psycopg2.OperationalError as e:
        print(f"Error: Could not connect to the database. Reason: {e}")
        return None

def initialize_app():
    print("Initializing the application...")

initialize_app()
