import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get database credentials from environment variables
db_host = os.getenv("DATABASE_HOST")
db_port = os.getenv("DATABASE_PORT")
db_user = os.getenv("DATABASE_USER")
db_password = os.getenv("DATABASE_PASSWORD")
db_name = os.getenv("DATABASE_NAME")

# Validate required environment variables
if not all([db_host, db_port, db_user, db_password, db_name]):
    raise ValueError("Missing required database environment variables. Please check your .env file.")

def get_connection():
    """
    Creates and returns a MySQL database connection using PyMySQL.
    Returns None if connection fails.
    """
    try:
        connection = pymysql.connect(
            host=db_host,
            port=int(db_port),
            user=db_user,
            password=db_password,
            database=db_name,
            cursorclass=pymysql.cursors.Cursor,
            charset='utf8mb4',
            autocommit=False,
            ssl={'ssl': True}  # Enable SSL for Railway
        )
        print("✓ Database connected successfully")
        return connection
    except pymysql.Error as err:
        print(f"✗ Database connection error: {err}")
        return None
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return None