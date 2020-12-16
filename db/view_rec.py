# The module to display the data from the database
import time

import decor.animations
import decor.tabular
import mysql.connector
from mysql.connector.connection import MySQLCursor


def doctors(cursor:MySQLCursor, field:str) -> None:
    """Print records from the DOCTORS table.
    """
    if field == 'all':
        query = 'SELECT * FROM DOCTORS;'
    elif field == 'docId':
        try:
            val = int(input('Enter the doctor id: '))
            if val < 0:
                raise ValueError
            query = f'SELECT * FROM DOCTORS WHERE docId={val};'
        except (TypeError, ValueError):
            print('Please enter a valid id!')
            return
    elif field == 'docName':
        name = input("Enter the doctor's name: ")
        query = f"SELECT * FROM DOCTORS WHERE docName='{name}';"
    elif field == 'speciality':
        dept = input('Enter the department: ')
        query = f"SELECT * FROM DOCTORS WHERE speciality='{dept}';"
    else:
        print('Invalid')
        return

    try:
        cursor.execute(query)
        decor.animations.load_animation()
        decor.tabular.doctors(cursor.fetchall())
        time.sleep(5)
    except mysql.connector.Error as err:
        print(f'\nSomething went wrong!\n{err}')


def patients(cursor:MySQLCursor, field:str) -> None:
    """Print records from the PATIENTS table.
    """
    if field == 'all':
        query = 'SELECT * FROM PATIENTS;'
    elif field == 'pId':
        try:
            val = int(input('Enter the patient id: '))
            if val < 0:
                raise ValueError
            query = f'SELECT * FROM PATIENTS WHERE pId={val};'
        except (TypeError, ValueError):
            print('Please enter a valid id!')
            return
    elif field == 'pName':
        name = input("Enter the patient's name: ")
        query = f"SELECT * FROM PATIENTS WHERE pName='{name}';"
    elif field == 'admitDate':
        date = input('Enter admission date (YYYY-MM-DD): ')
        query = f"SELECT * FROM PATIENTS WHERE admitDate='{date}';"
    elif field == 'roomNum':
        try:
            room = int(input('Enter room number: '))
            if room < 0:
                raise ValueError
            query = f'SELECT * FROM PATIENTS WHERE roomNum={room};'
        except (TypeError, ValueError):
            print('Please enter a valid room number!')
            return
    else:
        print('Invalid')
        return

    try:
        cursor.execute(query)
        decor.animations.load_animation()
        decor.tabular.patients(cursor.fetchall())
        time.sleep(5)
    except mysql.connector.Error as err:
        print(f'\nSomething went wrong!\n{err}')
