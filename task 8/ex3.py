#Exercise 3

#rewrite the guardian code in the above example(exercise 2) without two if.
#Instead use a compound logical expression using the and logical operator with single if statement

fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    #print ('Debug:', words)
    if len(words)>2 and words[0] == 'From':  #rewriting
        print(words[2])
