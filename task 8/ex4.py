#Exercise 4

fname=input('Enter file: ')
fhand=open(fname)
total=[]
for line in fhand:
    words=line.split()
    total+=(words)
    total.sort()
print(total)
