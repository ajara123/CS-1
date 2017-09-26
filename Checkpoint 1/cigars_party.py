
cigars=input('the number of cigars: ')
is_weekend=input('is the day weekend? ')
if int(cigars)<40:
    print ('False')
elif is_weekend=='yes':
    print ('True')
else:
    if int(cigars)<=60:
        print ('True')
    else:
        print ('False')
