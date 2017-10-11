#Exercise 6

numbers=[]
while True:
    NumInput=input('Enter a number: ')
    if NumInput!='done':
        numbers.append(NumInput)
        continue
    else: break
print ('Maximum:',max(numbers))
print ('Minimum:', min(numbers))
    
    
