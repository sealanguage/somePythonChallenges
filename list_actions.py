if __name__ == "__main__":
    N = int(input())
    #  print("number of lines ", N)
    mylist = []
    testlist = []
    # testlist.insert(0, 5)   # insert int 5 at position 0, this is how insert works
    # testlist.insert(1, 10)
    # testlist.insert(0, 6)

    # print("testlist.insert: ", testlist)

    for i in range(N):
        inlist = []

        #  this successfully prints the first element in each list
        inlist.append(input().split())
        # mylist.insert(inlist[0][1], inlist[0][2])

        # # print("inlist[0][0] ", inlist[0][0])   # returns position 0 - 12 lines
        # print(inlist[0][0])   # returns position 0 - 12 lines
        # # print("inlist[0][1] ", inlist[0][1])   # returns position 1 - till print
        # print(inlist[0][1])
        # # print("inlist[0][2] ", inlist[0][2])   # returns position 2 - till print
        # print(inlist[0][2])
        # mylist.append(inlist[0])

        if inlist[0][0] == "insert":
            # mylist.inlist[0][0](inlist[0][1], inlist[0][2])
            mylist.insert(int(inlist[0][1]), int(inlist[0][2]))
            # print(mylist)
        if inlist[0][0] == "print":
            print(mylist)
        if inlist[0][0] == "remove":
            mylist.remove(int(inlist[0][1]))
        if inlist[0][0] == "append":
            mylist.append(int(inlist[0][1]))
        if inlist[0][0] == "sort":
            mylist.sort()
        if inlist[0][0] == "pop":
            mylist.pop()
        if inlist[0][0] == "reverse":
            mylist.sort(reverse=True)

