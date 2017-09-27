def caught_speeding(speed, birthday):
    if birthday=='True':
        if speed<=65:
            return (0)
        if speed>65 and speed<=85:
            return(1)
        if speed>85:
            return (2)
    else:
        if speed<=60:
            return(0)
        if speed>60 and speed<=80:
            return(1)
        if speed>80:
            return (2)

print(caught_speeding(60, 'False'))
print(caught_speeding(65, 'False'))
print(caught_speeding(65, 'True'))
print(caught_speeding(85, 'False'))
