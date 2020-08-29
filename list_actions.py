if __name__ == "__main__":
    N = int(input())
    #  print("number of lines ", N)
    mylist = []
    endlist = []

    for i in range(N):
        inlist = []
        #  this successfully prints the first element in each list
        inlist.append(input().split())
        # print("inlist[0][0] ", inlist[0][0])   # returns position 0 - 12 lines
        # print("inlist[0][1] ", inlist[0][1])   # returns position 1 - till print
        # print("inlist[0][2] ", inlist[0][2])   # returns position 2 - till print
        # mylist.append(inlist[0])
        # if mylist[0][0] == print:
        print(inlist[0])
        # print(inlist[0][0])
        # print(inlist[0][1])
        # print(inlist[0][2])
        endlist[0].insert(inlist[0][5])

        print(endlist)

        # list methods append() , extend() , and insert() to add items to a list

        # print(inlist[i][1] + inlist[i][2])
        # if inlist[0][1] == 0:
        #     print("zero")
        # # print(inlist)
