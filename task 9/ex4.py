#Exercise 4


#Add code to the above program to figure out who has the most messages in the file.
#After all the data has been read and the dictionary has been created, 
#look through the dictionary using a maximum loop (see Section [maximumloop]) to find who has the most messages 
#and print how many messages the person has.



fname=input('Enter a file name: ')
fhand=open(fname)
counts=dict()
for line in fhand:
    if line.startswith('From'):
        words=line.split()
        if len(words)>3:
            email=words[1]
            counts[email]=counts.get(email,0)+1
bigcount=None
bigword=None
for email,count in counts.items():
    if bigcount is None or count>bigcount:
        bigword=email
        bigcount=count

print(bigword, bigcount)
