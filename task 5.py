#task 5
#exersize 1
zero=0
count=0
numbers=[4,5,'bad data', 7,'done']
for i in numbers:
    print (i)
    try:
        i=int(i)
        zero=i+zero
        count=count+1
    except:
        if i != 'done':
            print ('Invalid input')
        else:
            print (zero, count, zero/count)

#exersize 2
numbers=[4,5,7,9,3]
smallest=None
biggest=None
summa=0
for i in numbers:
    summa=summa+i
    if smallest is None or i<smallest:
        smallest=i
    if biggest is None or i>biggest:
        biggest=i
print ('Smallest:', smallest,'Biggest:', biggest, 'Sum', summa)
        
        
            
