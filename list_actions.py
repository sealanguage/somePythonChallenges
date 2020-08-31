if __name__ == "__main__":
    N = int(input())
    #  print("number of lines ", N)
    mylist = []
    # endlist = []
    mylist.insert(0, 5)  # insert int 5 at position 0, this is how insert works
    print("mylist.insert: ", mylist)

    for i in range(N):
        inlist = []

        #  this successfully prints the first element in each list
        inlist.append(input().split())
        # mylist.insert(inlist[0][1], inlist[0][2])
        print("inlist[0][0] ", inlist[0][0])  # returns position 0 - 12 lines
        print("inlist[0][1] ", inlist[0][1])  # returns position 1 - till print
        print("inlist[0][2] ", inlist[0][2])  # returns position 2 - till print
        mylist.append(inlist[0])

        # list methods append() , extend() , and insert() to add items to a list

        # print(inlist[i][1] + inlist[i][2])
        # if inlist[0][1] == 0:
        #     print("zero")
        # # print(inlist)
