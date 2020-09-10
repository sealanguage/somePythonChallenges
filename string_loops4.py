if __name__ == "__main__":

    # a, b = input("Enter two of your lucky number: ").split()
    T = int(input())
    S = input()
    #  loop grab input run it and then grab the next
    splits = S.split()

    print("The original string is : " + S)

    S = input()
    #  loop grab input run it and then grab the next
    splits = S.split()

    print("The original string is : " + S)

    # while (splits < T):
    print("splits is ", splits)

    # trying to get the second string in the input-not working
    for split in splits:
        print("split is: ", split)

    # use slice [] operator to iterate every other letter
    for letter in split[::2]:
        print(letter, end="")
    # use slice [] operator to get the missing letters
    print(end=" ")
    for letter in split[1::2]:
        print(letter, end="")
