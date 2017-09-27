def alarm_clock(weekday, vacation):
    if vacation=='True':
        if weekday==0 or weekday==6:
            return('off')
        else:
            return('10:00')
    else:
        if weekday==0 or weekday==6:
            return ('10:00')
        else:
            return ('7:00')
print(alarm_clock(1,'False'))
print(alarm_clock(5,'False'))
print(alarm_clock(0,'False'))
print(alarm_clock(6,'False'))
print(alarm_clock(0,'True'))
print(alarm_clock(6,'True'))
