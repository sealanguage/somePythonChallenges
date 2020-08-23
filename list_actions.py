if __name__ == "__main__":
    N = int(input())
    #  print("number of lines ", N)

    mylist = []

    for i in range(N):
        # print(input().split())  #  prints each line of the input
        mylist.append(input().split())
        print(mylist)
