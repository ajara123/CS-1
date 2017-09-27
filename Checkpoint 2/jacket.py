def jacket(temp):
    if temp<20:
        return ('Bring heavy jacket')
    if temp>=20 and temp<=30:
        return ('Bring light jacket')
    if temp>30:
        return ('Do not bring any jacket')

print(jacket(25))
print (jacket(14))
print (jacket(35))
