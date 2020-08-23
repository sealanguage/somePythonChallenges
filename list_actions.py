if __name__ == "__main__":
    N = int(input())
    #  print("number of lines ", N)

    #  this separates each line of input into single list
    for i in range(N):
        mylist = []
        mylist.append(input().split())
        print(mylist)
