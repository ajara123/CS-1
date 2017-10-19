#Exercise 3

# Write a program that reads a file and prints the letters in decreasing order
#of frequency. Your program should convert all the input to lower case and only
#count the letters a-z. Your program should not count spaces, digits,
#punctuation, or anything other than the letters a-z. Find text samples from
#several different languages and see how letter frequency varies between
#languages. Compare your results with the tables at wikipedia.org/wiki/Letter_frequencies.


fname=input('Enter a file name:')
fhand=open(fname)
counts=dict()
l=list()
for line in fhand:
    line=line.lower()
    line=line.rstrip()
    t=tuple(line)
    k=list(t)
    tup=tuple(k)
    for letter in tup:
        counts[letter]=counts.get(letter, 0)+1
lst=list(counts.items())
for letters, count in lst:
    l.append((count,letters))
    l.sort(reverse=True)
for c,le in l[1:]:
    print(c, le)


