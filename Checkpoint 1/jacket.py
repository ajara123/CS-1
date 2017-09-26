#a program to accept the temperature and to tell a person whether or not based on tempperature

degree=input('Enter temperature: ')
if int(degree)<20:
    print('Please, bring heavy jacket')
if int(degree)>20 and int(degree)<30:
    print('PLease, bring light jacket')
if int(degree)>30:
    print('Do not bring any jacket')
