fname=input('Enter a file name: ')
fhand=open(fname)
new=dict()

for line in fhand:
    words=line.split()
    print (words)
    for word in words:
        new[word]=word
print (new)
    
