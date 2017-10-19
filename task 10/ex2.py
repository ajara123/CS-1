#Exercise 2

#This program counts the distribution of the hour of the day for each of the messages.
#You can pull the hour from the "From" line by finding the time string and then splitting
#that string into parts using the colon character. Once you have accumulated the counts for
#each hour, print out the counts, one per line, sorted by hour as shown below.


fname=input("Enter a file name: ")
fhand=open(fname)
counts=dict()
for line in fhand:
    if line.startswith('From'):
        words=line.split()
        if len(words)>3:
            time=words[5]
            hour=time.split(':')[0]
            counts[hour]=counts.get(hour,0)+1
lst=list(counts.items())
lst.sort()
for h,c in lst:
    print(h,c)
            
