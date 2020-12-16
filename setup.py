# The setup to install the database in the local system
import json

import db.add_rec
import db.connector
import db.create_table
import db.db
import mysql.connector


if root:=db.connector.connect_to_root():
    cursor = root.cursor()

    try:
        db.db.create(cursor)
        print('\nDatabase initialized! ✔\n')
    except mysql.connector.Error as err:
        print(f'\nSomething went wrong!\n{err}')

    # Close the connection to root
    root.close()

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

        # Close connection to the mysql database
        conn.close()
