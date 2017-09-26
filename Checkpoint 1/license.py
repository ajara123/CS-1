# a program simulating driver's license provision
age=input('Enter age: ') 
practice_hours=input('Enter practise hours: ')
if int(age)>16:
    if int(practice_hours)>200:
        print ('License to be printed')
    else:
        print ('Sorry, license cannot be printed')
else:
    print ('Sorry, license cannot be printed')

    
