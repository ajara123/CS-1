#Exercize 2
fhand=open('mbox-short.txt')
for line in fhand:
    words=line.split()
    if len(words)<3: continue #guarding for number of elements to be in a line
    if words[0] != 'From':continue
    print(words[2])

