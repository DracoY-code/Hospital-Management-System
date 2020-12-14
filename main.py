import db.add_rec
import db.connector
import db.del_rec
import db.view_rec
import decor.details
import decor.animations
import mysql.connector


if conn:=db.connector.connect():
    cursor = conn.cursor()

    decor.animations.loading()  #ADDED
    print("DATATRIX - Hospital Database Management System")

    print("\n1 - Access Doctor's data")
    print("2 - Access Patient's data")
    print("0 - Exit\n")

    choice = input('Choose the database: ')
    miss = 0

    if choice == '1':
        # Doctors
        print('\n1 - View All')
        print('2 - View (by id)')
        print('3 - View (by name)')
        print('4 - View (by department)')
        print('5 - Add Doctor')
        print('6 - Delete Doctor')
        print('0 - Exit')

        while miss < 5:
            option = input('\nSelect operation (0 to exit): ')
            if option == '1':
                
                # View all
                decor.animations.load_animation()  #ADDED
                db.view_rec.doctors(cursor, 'all')
            elif option == '2':

                # By id
                db.view_rec.doctors(cursor, 'docId')
                decor.animations.load_animation()  #ADDED
            elif option == '3':
                # By name
                db.view_rec.doctors(cursor, 'docName')
                decor.animations.load_animation()  #ADDED
            elif option == '4':
                # By department
                db.view_rec.doctors(cursor, 'speciality')
                decor.animations.load_animation()  #ADDED
            elif option == '5':
                # Add doctor
                print('\nPlease enter details of the doctor!\n')
                try:
                    details = decor.details.doctors()
                except TypeError as err:
                    print(f'\nSomething went wrong!\n{err}')
                    continue
                try:
                    db.add_rec.doctors(cursor, **details)
                    conn.commit()
                except mysql.connector.Error:
                    conn.rollback()
            elif option == '6':
                # Remove doctor
                try:
                    idx = int(input('Enter the doctor id: '))
                    if idx < 0:
                        raise ValueError
                    try:
                        db.del_rec.doctors(cursor, idx)
                        conn.commit()
                    except mysql.connector.Error:
                        conn.rollback()
                except (TypeError, ValueError):
                    print('Please enter a valid id!')
            elif option == '0':
                decor.animations.load_animation('Exiting...👋')
                break
            else:
                miss += 1
                print(f'Invalid! {5-miss} bad inputs left!')

    elif choice == '2':
        # Patients
        print('\n1 - View All')
        print('2 - View (by id)')
        print('3 - View (by name)')
        print('4 - View (by admission date)')
        print('5 - View (by room number)')
        print('6 - Add Patient')
        print('7 - Delete Patient')
        print('0 - Exit')
        
        while miss < 5:
            option = input('\nSelect operation (0 to exit): ')
            if option == '1':
                # View all
                db.view_rec.patients(cursor, 'all')
            elif option == '2':
                # By id
                db.view_rec.patients(cursor, 'pId')
            elif option == '3':
                # By name
                db.view_rec.patients(cursor, 'pName')
            elif option == '4':
                # By admission date
                db.view_rec.patients(cursor, 'admitDate')
            elif option == '5':
                # By room number
                db.view_rec.patients(cursor, 'roomNum')
            elif option == '6':
                # Add patient
                print('\nPlease enter details of the patient!\n')
                try:
                    details = decor.details.patients()
                except TypeError as err:
                    print(f'\nSomething went wrong!\n{err}')
                    continue
                try:
                    db.add_rec.patients(cursor, **details)
                    conn.commit()
                except mysql.connector.Error:
                    conn.rollback()
            elif option == '7':
                # Remove patient
                try:
                    idx = int(input('Enter the patient id: '))
                    if idx < 0:
                        raise ValueError
                    try:
                        db.del_rec.patients(cursor, idx)
                        conn.commit()
                    except mysql.connector.Error:
                        conn.rollback()
                except (TypeError, ValueError):
                    print('Please enter a valid id!')
            elif option == '0':
                print('Exiting...👋')
                break
            else:
                miss += 1
                print(f'Invalid! {5-miss} bad inputs left!')

    elif choice == '0':
        print('Exiting...👋')

    else:
        print('Invalid ❌❌❌')

    if miss >= 5:
        print('\nPlease try again later!')

    conn.close()
