
#exercise 4 - the answer D
#exercise 5 - the answer D

#exercise 6
def computepay(hours, rate):
    if hours>40:
        return ((hours-40)*1.5+40)*rate
    else:
        return hours*rate

print (computepay (45,10))

#exercise 7
def computegrade(score):
    if type(score)==str:
        return ('Bad score')
    else:
        if score<0.6: 
            return ('F')
        if score>=0.6 and score<0.7:
            return ('D')
        if score>=0.7 and score<0.8:
            return ('C')
        if score>=0.8 and score<0.9:
            return ('B')
        if score>=0.9 and score<=1:
            return ('A')
        
print(computegrade('perfect'))



