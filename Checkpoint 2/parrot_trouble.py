def parrot_trouble(parrot, hour):
    if parrot=='True' and hour<7 or hour>20:
        return True
    else:
        return False

print (parrot_trouble('True', 25))
print (parrot_trouble('True', 7))
print (parrot_trouble('False', 6))
