str1 = 'X-DSPAM-Confidence:0.8475'
string=str1.find(':')
number=float(str1[string+1:])
print(number)


string="hello World"
lower=string.lower()
print(lower)

upper=string.upper()
print(upper)

cap=string.capitalize()
print(cap)


