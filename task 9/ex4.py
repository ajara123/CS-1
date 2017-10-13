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
