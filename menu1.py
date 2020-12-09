from ksn import load_animation
import sys
from functions import loading2


welcome = 'database loading....'

sys.stdout.write('M E N U')
print("\n \n \n \n 1. Access Patient Database  \n 2. Access Doctors' Database")
print("\n\n ENTER CHOICE")

ch1= int(input('Enter your choice (1/2) '))
loading2()

if ch1==1:
    load_animation(welcome)
    print('\n \n 1.VIEW PATIENT DATA \n\n 2.ADD PATIENT DATA \n\n 3.SEARCH PATIENT \n\n 4.DELETE PATIENT')
elif ch1==2:
    load_animation(welcome)
    print('\n \n 1.VIEW DOCTORS DATA \n\n 2.ADD DOCTORS DATA \n\n 3.SEARCH DOCTORS \n\n 4.DELETE DOCTORS')

    

    
        
