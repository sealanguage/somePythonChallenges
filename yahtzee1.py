import random

# from operator import setitem

dice = []
reroll = []
dienums = random.randint(1, 6)
all_dice = 5


for value in range(all_dice):
    dice.append(random.randint(1, 6))

print (dice)

shopList = []
maxLengthList = 6
while len(shopList) < maxLengthList:
    item = input("Enter your Item to the List: ")
    shopList.append(item)
print "That's your Shopping List"
print (shopList)


# n = int(input("reroll which sep by space? "))
# reroll = n.split()
# print(reroll)

# for value in range(reroll):
#     reroll.append(n)

# print(reroll)
dice[n] = random.randint(1, 6)

print (dice)
