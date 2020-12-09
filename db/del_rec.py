# The module to delete records from the database
import mysql.connector
from mysql.connector.connection import MySQLCursor


def doctors(cursor:MySQLCursor, idx:int) -> None:
    """Delete records from the DOCTORS table.
    """
    try:
        cursor.execute(f'DELETE FROM DOCTORS WHERE docId={idx};')
        print('Doctor deleted! ❌')
    except mysql.connector.Error as err:
        print(f'\nSomething went wrong!\n{err}')


def patients(cursor:MySQLCursor, idx:int) -> None:
    """Delete records from the PATIENTS table.
    """
    try:
        cursor.execute(f'DELETE FROM PATIENTS WHERE pId={idx};')
        print('Patient deleted! ❌')
    except mysql.connector.Error as err:
        print(f'\nSomething went wrong!\n{err}')
