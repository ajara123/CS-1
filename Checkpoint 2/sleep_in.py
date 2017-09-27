def sleep_in(weekday, vacation):
    if vacation=='True':
        return ('True')
    else:
        if weekday=='False':
            return ('True')
        else:
            return ('False')

print (sleep_in('False','True'))
print (sleep_in('False', 'False'))
print (sleep_in('True', 'False'))
print (sleep_in('True', 'True'))
