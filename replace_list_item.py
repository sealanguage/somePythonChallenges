import random

list = [0, 1, 2, 3, 4]
print("list is; ", list)

change = int(input("number change at index : "))

list[change] = random.randint(10, 15)  # randint(low value, high value)
print("new list: ", list)

change_many = int(input("number change at index separate with space : "))

list[change_many] = random.randint(10, 15)
print("multi change list: ", list)
