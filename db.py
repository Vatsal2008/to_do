import mysql.connector
import os
from dotenv import load_dotenv


load_dotenv()

db_password = os.getenv("DATABASE_PASSWORD")
db_name = os.getenv("DATABASE_NAME")
db_user = os.getenv("DATABASE_USER")
db_port = os.getenv("DATABASE_PORT")
db_host = os.getenv("DATABASE_HOST")

if not db_password or not db_name:
    raise ValueError("Missing database environment variables")

def get_connection():
    try:
        db = mysql.connector.connect(
            host=db_host,
            port=db_port,
            user=db_user,
            passwd=db_password,
            database=db_name,
            auth_plugin="mysql_native_password",
        )
        print("Connected successfully")
        return db   # <--- return the connection here
    except mysql.connector.Error as err:
        print("Error:", err)
        return None
