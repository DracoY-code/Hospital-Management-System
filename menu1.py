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
    
    c=0
    while True:
        ch2 = int(input("Enter your choice (1/2/3/4) "))

    
        if ch2==1:
            #function
            loading2()
        elif ch2==2:
            #function
            loading2()
        elif ch2==3:
            #func
            loading2()
        elif ch2==4:
            #func
            loading2()
        else:
            print('input wrong')
            c+=1
            if c >5:
                break
            else:
                continue

elif ch1==2:
    load_animation(welcome)
    print('\n \n 1.VIEW DOCTORS DATA \n\n 2.ADD DOCTORS DATA \n\n 3.SEARCH DOCTORS \n\n 4.DELETE DOCTORS')
    
    c=0
    while True:
        ch2= int(input("Enter your choice : "))
        
    
        if ch2==1:
            #function
            loading2()
        elif ch2==2:
            #function
            loading2()
        elif ch2==3:
            #func
            loading2()
        elif ch2==4:
            #func
            loading2()
        else:
            print('input wrong')
            c+=1
            if c >5:
                break
            else:
                continue


    

    
        
