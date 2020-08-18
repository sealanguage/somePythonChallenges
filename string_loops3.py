# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":

    # a, b = input("Enter two of your lucky number: ").split()
    T = int(input())
    S = input().split()

    T = int(input())
    # S = input()
    splits = input().split()

    # trying to get the second string in the input-not working
    for split in splits:
        print(split)

    # use slice [] operator to iterate every other letter
    for letter in split[::2]:
        print(letter, end="")
    # use slice [] operator to get the missing letters
    print(end=" ")
    for letter in split[1::2]:
        print(letter, end="")


#     Traceback (most recent call last):
#   File "Solution.py", line 9, in <module>
#     T = int(input())
# ValueError: invalid literal for int() with base 10: 'Rank'


# # print("S is: ", S)
# # mylist = []
# # for word in S:
# #     mylist.append(word)
# #     # splits = str.split(S)
# #     # for item in splits:
# #     #     print(item, end=' ')
# #     # print('')  # for new line
# # print(mylist)

# #     map_result =  map(getLength, splits)
# #     print("Type of map_result is {}".format(type(map_result)))
# # print(S.split())

# # Function to print the map output
# def show_result(splits):
#     for item in splits:
#         print(item, end=' ')
#     print('')  # for new line

# # show_result(splits)
# # #trying to get the second string in the input-not working
# # for split in splits :
# #     print(split)

# # use slice [] operator to iterate every other letter
# for letter in S[::2]:
#     print(letter, end="")
# # use slice [] operator to get the missing letters
# print(end=" ")
# for letter in S[1::2]:
#     print(letter, end="")

