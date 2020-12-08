# The module to create the tables for the database
import mysql.connector
from mysql.connector.connection import MySQLCursor


def doctors(cursor:MySQLCursor) -> None:
    """Create the DOCTORS table.
    """
    try:
        cursor.execute('DROP TABLE IF EXISTS DOCTORS;')
        cmd = """
        CREATE TABLE DOCTORS
        (
            docId INT PRIMARY KEY,
            docName VARCHAR(30),
            speciality VARCHAR(30),
            age INT,
            salary INT,
            joinDate DATE
        );
        """
        cursor.execute(cmd)
    except mysql.connector.Error as err:
        print(f'\nSomething went wrong!\n{err}')


def patients(cursor:MySQLCursor) -> None:
    """Create the PATIENTS table.
    """
    try:
        cursor.execute('DROP TABLE IF EXISTS PATIENTS;')
        cmd = """
        CREATE TABLE PATIENTS
        (
            pId INT PRIMARY KEY,
            pName VARCHAR(30),
            age INT,
            bloodGrp VARCHAR(3),
            docId INT REFERENCES DOCTORS(docId),
            dept VARCHAR(40),
            admitDate DATE,
            roomNum INT
        );
        """
        cursor.execute(cmd)
    except mysql.connector.Error as err:
        print(f'\nSomething went wrong!\n{err}')
