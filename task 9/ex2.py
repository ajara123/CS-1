#Exercise 2
#Write a program that categorizes each mail message by which day of the weel the commit was done.
#To do this look for lines that start with "From", then look for the third word and keep a running count of each of the days of the week.
#At the end of the program print out the contents of your dictionary (order does not matter)

fname=input('Enter a file name: ')
fhand=open(fname)
count=0
counts=dict()
for line in fhand:
    if line.startswith('From'):
        words=line.split() #split into items
        if len(words)>3: #guarding for the line with more than 3 items in the line
            day=words[2]
            if day not in counts: 
                counts[day]=1
            else:
                counts[day]+=1 #summing up
print(counts)
        
