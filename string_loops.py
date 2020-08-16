if __name__ == "__main__":
    T = int(input())
    S = input()
    splits = S.split()

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

