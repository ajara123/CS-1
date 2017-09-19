
vacation=input('Are you on vacation? ')
day=input('Enter day: ')
weekday=('Monday','Tuesday','Wednesday','Thursday','Friday')
weekend=('Sunday', 'Saturday')
if vacation=='no':
    for i in weekday:
        if day==i:
            print('False')
    for e in weekend:
        if day==e:
            print ('True')
else:
    print('True')
