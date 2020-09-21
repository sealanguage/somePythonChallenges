import random
from operator import setitem

# numdie = int(input("How many die to roll?"))
numdie = 5
dice = []  # limit to 5 max dice
# roll = random.randint(1, 5)

for roll in range(numdie):
    roll = random.randint(1, 6)
    dice.append(roll)
print("First roll: ", dice)

#  reroll just 1st die
reroll_die = []
reroll = int(input("Die to reroll: "))

# operator.setitem(a, b, c)    Set the value of a at index b to c.
dice.insert(reroll, roll)  #  (i, elem) i = index   elem = replace with this
print("dice ", dice)
