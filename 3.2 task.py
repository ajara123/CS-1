#3.2 Task 1 exercise
hours=int(input('Enter hours '))
rate=int(input('Enter rate '))
if hours > 40:
    print ('Pay: ', (40*rate)+(hours-40)*1.5*rate)
else:
    print ('Pay: ', hours*rate)

#2 exercise
hours=input('Enter Hours: ')
rate= input('Enter Rate: ')
try:
    hours=int(hours)
    rate=int(rate)
    print ('Pay: ', hours*rate)
except:
    print('Error, please enter numeric input')
    
#3 exercise
score=input('Enter score: ')
try:
    score=float(score)
    if score>0 and score<1:
        if score<0.6: 
            print ('F')
        if score>=0.6 and score<0.7:
            print ('D')
        if score>=0.7 and score<0.8:
            print ('C')
        if score>=0.8 and score<0.9:
            print ('B')
        if score>=0.9:
            print ('A')
    else:
        print ('Bad score')
except:
    print('Bas score')
