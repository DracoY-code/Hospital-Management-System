import csv
import datetime
import getpass

import db.config
import mysql.connector
from mysql.connector.connection import MySQLConnection


def connect() -> MySQLConnection:
    """Connect to the mysql hospital database.
    """
    user = input('Username: ')
    passwd = getpass.getpass('Password: ')
    now = f'{datetime.datetime.now():%Y-%m-%d %H:%M:%S}'

    if _logged_in(user, passwd):
        try:
            connection = mysql.connector.connect(**db.config.get_creds())
            if connection.is_connected():
                print('\nSuccessfully connected to the database! 🐬')
                _write_log(user, now, True)
                return connection
        except mysql.connector.Error as err:
            print(f'\nSomething went wrong!\n{err}')
            _write_log(user, now, False)
    else:
        print('\nLogin unsuccessful.')
        _write_log(user, now, False)


def connect_to_root() -> MySQLConnection:
    """Returns a root connection to the database.
    """
    try:
        root_pass = getpass.getpass('ROOT PASSWORD: ')
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd=root_pass
        )
        if connection.is_connected():
            db.config.write_creds(root_pass)
            print('Connected as root!')
            return connection
    except mysql.connector.Error as err:
        print(f'\nSomething went wrong!\{err}')


def _logged_in(user:str, passwd:str) -> bool:
    """Check login credentials of the user.
    """
    with open('./login/users.csv') as login_data:
        reader = csv.reader(login_data)
        for row in reader:
            if row[0].lower()==user.lower() and row[1]==passwd:
                return True
    return False


def _write_log(user:str, time:str, logged:bool) -> None:
    """Writes log file after each login.
    """
    with open('./login/login.log', 'a') as log_file:
        if logged:
            msg = f'[{time}] {user} PASS\n'
        else:
            msg = f'[{time}] {user} FAIL\n'
        log_file.write(msg)
