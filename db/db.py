# The module to create the required database in mysql
import mysql.connector
from mysql.connector.connection import MySQLCursor


def create(cursor:MySQLCursor) -> None:
    """Create the hospital database.
    """
    try:
        cursor.execute('CREATE DATABASE IF NOT EXISTS hospital;')
    except mysql.connector.Error as err:
        print(f'\nSomething went wrong!\n{err}')
