#Exercise 1

#Revise a previous program as follows: Read and parse the "From" lines and
#pull out the addresses from the line. Count the number of messages from each
#person using a dictionary.

A#fter all the data has been read, print the person with the most commits by
#creating a list of (count, email) tuples from the dictionary.
#Then sort the list in reverse order and print out the person who has the most commits.


fname=input('Enter a file name: ')
fhand=open(fname)
counts=dict()
for line in fhand:
     if line.startswith('From'):
        words=line.split()
        if len(words)>3:
            email=words[1]
            counts[email]=counts.get(email, 0)+1
            lst=list(counts.items())
            lst.sort(reverse=True)
print(lst[0][0], lst[0][1])

                
