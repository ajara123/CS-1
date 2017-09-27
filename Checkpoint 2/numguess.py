import random
random_number=random.randint(1,9)
while True:
    guess=int(input('Enter number from 1 to 9: '))
    if random_number!=guess:
        continue
    if random_number==guess:
        break
print ('Well guessed')
exit()

