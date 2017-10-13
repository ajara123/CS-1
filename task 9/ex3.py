#Exercise 3
#Write a program to read through a mail log, build a histogram using a dictionary
#to count how many messages have come from each email address, and print the dictionary


fname=input('Enter a file name: ')
fhand=open(fname)
new=dict()
for line in fhand:
    if line.startswith('From'):
        words=line.split()
        if len(words)>3:
            email=words[1]
            if email not in new:
                new[email]=1
            else:
                new[email]+=1
print(new)
        
