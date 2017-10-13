#Exercise 5
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
