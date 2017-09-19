speed=int(input('Enter the speed: '))
birthday=input('Is today your birthday? ')
if birthday=='yes':
    if speed<=65:
        print (0)
    if speed>65 and speed<=85:
        print(1)
    if speed>85:
        print (2)
else:
    if speed<=60:
        print(0)
    if speed>60 and speed<=80:
        print(1)
    if speed>80:
        print (2)
