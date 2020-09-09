def count_substring(string, sub_string):
    count_substring = 0

    print("string: ", string, "sub_string: ", sub_string)  # this prints both str

    for i in range(0, len(string)):
        print(string[i])
        # return
    for j in sub_string:
        print(j)

    # string = input().strip()    strip() when empty removes leading/trailing spaces
    # sub_string = input().strip()


if __name__ == "__main__":
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
