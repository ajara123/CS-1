vacation=input('Are you on vacation? ')
weekday=int(input('what day of the week? '))
if vacation=='yes':
    if weekday==0 or weekday==6:
        print('off')
    else:
        print('10:00')
else:
    if weekday==0 or weekday==6:
        print('10:00')
    else:
        print('7:00')
