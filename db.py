import mysql.connector
import os
from dotenv import load_dotenv


load_dotenv()

db_password = os.getenv("DATABASE_PASSWORD")
db_name = os.getenv("DATABASE_NAME")

if not db_password or not db_name:
    raise ValueError("Missing database environment variables")

def get_connection():
    try:
        db = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            passwd=db_password,
            database=db_name,
            auth_plugin="mysql_native_password",
        )
        print("Connected successfully")
        return db   # <--- return the connection here
    except mysql.connector.Error as err:
        print("Error:", err)
        return None
