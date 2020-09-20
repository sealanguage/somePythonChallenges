import random

# print random.randint(0, 5)    # prints a random value, a roll of the die
num_die = int(input("how many die?"))
dice = []

for face in range(num_die):
    die = random.randint(1, 6)
    dice.append(die)
print(dice)

