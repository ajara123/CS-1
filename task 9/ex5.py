#Exercise 5

#This program records the domain name (instead of the address) where the message was sent from instead
#of who the mail came from (i.e., the whole email address). 
#At the end of the program, print out the contents of your dictionary.

fname=input('Enter a file name: ')
fhand=open(fname)
counts=dict()
for line in fhand:
    if line.startswith('From'):
        words=line.split()
        if len(words)>3:
            email=words[1]
            position=email.find('@')
            address=email[position+1:]
            counts[address]=counts.get(address,0)+1
print (counts)
