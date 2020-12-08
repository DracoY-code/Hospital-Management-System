# The setup to install the database in the local system
import json

import db.add_rec
import db.connector
import db.create_table
import mysql.connector


if conn:=db.connector.connect():
    cursor = conn.cursor()

    try:
        db.create_table.doctors(cursor)
        db.create_table.patients(cursor)

        with open('blindData.json') as file:
            data = json.load(file)

        for doctor in data['doctors']:
            db.add_rec.doctors(cursor, **doctor)

        for patient in data['patients']:
            db.add_rec.patients(cursor, **patient)

        conn.commit()
        print('\nSetup complete. ✔')
    except mysql.connector.Error as err:
        conn.rollback()
        print(f'\nSomething went wrong!\n{err}')

    conn.close()
