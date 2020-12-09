# The module to display records from the table


def doctors(records:list) -> None:
    """Print records from the DOCTORS table.
    """
    x = '-'
    margin = f'+{x*7}+{x*32}+{x*32}+{x*7}+{x*12}+{x*12}+'
    print(f'\n{margin}')
    print('| '+'docId'.rjust(5)+' | '
          +'docName'.ljust(30)+' | '
          +'speciality'.ljust(30)+' | '
          +'age'.rjust(5)+' | '
          +'salary'.rjust(10)+' | '
          +'joinDate'.ljust(10)+' |')
    print(margin)
    for row in records:
        print('| '+str(row[0]).rjust(5)+' | '
              +str(row[1]).ljust(30)+' | '
              +str(row[2]).ljust(30)+' | '
              +str(row[3]).rjust(5)+' | '
              +str(row[4]).rjust(10)+' | '
              +str(row[5]).ljust(10)+' |')
    print(margin)


def patients(records:list) -> None:
    """Print records from the PATIENTS table.
    """
    x = '-'
    margin = f'+{x*7}+{x*32}+{x*7}+{x*10}+{x*7}+{x*32}+{x*12}+{x*9}+'
    print(f'\n{margin}')
    print('| '+'pId'.rjust(5)+' | '
          +'pName'.ljust(30)+' | '
          +'age'.rjust(5)+' | '
          +'bloodGrp'.ljust(8)+' | '
          +'docId'.rjust(5)+' | '
          +'dept'.ljust(30)+' | '
          +'admitDate'.ljust(10)+' | '
          +'roomNum'.rjust(7)+' |')
    print(margin)
    for row in records:
        print('| '+str(row[0]).rjust(5)+' | '
              +str(row[1]).ljust(30)+' | '
              +str(row[2]).rjust(5)+' | '
              +str(row[3]).ljust(8)+' | '
              +str(row[4]).rjust(5)+' | '
              +str(row[5]).ljust(30)+' | '
              +str(row[6]).ljust(10)+' | '
              +str(row[7]).rjust(7)+' |')
    print(margin)
