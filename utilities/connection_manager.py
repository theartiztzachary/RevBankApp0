from psycopg import OperationalError, connect
from utilities.custom_exceptions import DatabaseConnection
import os

def create_connection():
    try:
        conn = connect(
            host=os.environ.get("HOST"),
            dbname=os.environ.get("DBNAME"),
            user=os.environ.get("USER"),
            password=os.environ.get("PASSWORD"),
            port=os.environ.get("PORT")
        )
        return conn
    except OperationalError as exception:
        raise DatabaseConnection("Cannot connect to database.")

connection = create_connection()