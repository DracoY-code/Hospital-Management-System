# The module to get details from the user


def doctors() -> dict:
    """Returns the details of the doctor.
    """
    return {
        'docId': int(input('Id '.ljust(11)+'(NUM>0)'.rjust(12)+' : ')),
        'docName': input('Name '.ljust(11)+'(CHARs)'.rjust(12)+' : '),
        'speciality': input('Speciality '.ljust(11)+'(CHARs)'.rjust(12)+' : '),
        'age': int(input('Age '.ljust(11)+'(NUM>0)'.rjust(12)+' : ')),
        'salary': int(input('Salary '.ljust(11)+'(NUM>0)'.rjust(12)+' : ')),
        'joinDate': input('Join date '.ljust(11)+'(YYYY-MM-DD)'.rjust(12)+' : ')
    }


def patients() -> dict:
    """Returns the details of the patient.
    """
    return {
        'pId': int(input('Id '.ljust(15)+'(NUM>0)'.rjust(12)+' : ')),
        'pName': input('Name '.ljust(15)+'(CHARs)'.rjust(12)+' : '),
        'age': int(input('Age '.ljust(15)+'(NUM>0)'.rjust(12)+' : ')),
        'bloodGrp': input('Blood Group '.ljust(15)+'(CHARs)'.rjust(12)+' : '),
        'docId': int(input('Doctor Id '.ljust(15)+'(NUM>0)'.rjust(12)+' : ')),
        'dept': input('Department '.ljust(15)+'(CHARs)'.rjust(12)+' : '),
        'admitDate': input('Admission Date '.ljust(15)+'(YYYY-MM-DD)'.rjust(12)+' : '),
        'roomNum': int(input('Room Number '.ljust(15)+'(NUM>0)'.rjust(12)+' : '))
    }
