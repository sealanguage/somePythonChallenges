if __name__ == "__main__":
    T = int(input())
    S = input()
    string = S
    print(T)
    # for letter in range(S):
    #         print(letter)

    # for word in T :
    # print(word)

    # use slice [] operator to iterate every other letter
    for letter in string[::2]:
        print(letter, end="")
    # use slice [] operator to get the missing letters
    for letter in string[1::2]:

        print(letter, end="")

