# The module to add records in the tables of the database
import mysql.connector
from mysql.connector.connection import MySQLCursor


def doctors(cursor:MySQLCursor, **kwargs) -> None:
    """Add records of doctor to the DOCTORS table.
    """
    if _contains_keys(kwargs,
                      'docId',
                      'docName',
                      'speciality',
                      'age',
                      'salary',
                      'joinDate'):
        cmd = f"""
        INSERT INTO DOCTORS
        VALUES(
            {kwargs['docId']},
            '{kwargs['docName']}',
            '{kwargs['speciality']}',
            {kwargs['age']},
            {kwargs['salary']},
            '{kwargs['joinDate']}'
        );
        """
        try:
            cursor.execute(cmd)
        except mysql.connector.Error as err:
            print(f'\nSomething went wrong!\n{err}')
    else:
        raise mysql.connector.Error('Invalid data')


def patients(cursor:MySQLCursor, **kwargs) -> None:
    """Add records of patient to the PATIENTS table.
    """
    if _contains_keys(kwargs,
                      'pId',
                      'pName',
                      'age',
                      'bloodGrp',
                      'docId',
                      'dept',
                      'admitDate',
                      'roomNum'):
        cmd = f"""
        INSERT INTO PATIENTS
        VALUES(
            {kwargs['pId']},
            '{kwargs['pName']}',
            {kwargs['age']},
            '{kwargs['bloodGrp']}',
            {kwargs['docId']},
            '{kwargs['dept']}',
            '{kwargs['admitDate']}',
            {kwargs['roomNum']}
        );
        """
        try:
            cursor.execute(cmd)
        except mysql.connector.Error as err:
            print(f'\nSomething went wrong!\n{err}')
    else:
        raise mysql.connector.Error('Invalid data')


def _contains_keys(obj:dict, *args) -> bool:
    """Check if the dictionary has the specified keys.
    """
    for key in args:
        if key not in obj.keys():
            return False
    return True
