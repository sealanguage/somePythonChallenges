# passes half of the test cases
import sys

for line in sys.stdin:

    # print('1', line)
    # ('1', '5\n')   the number of ints in the input
    # ('1', '12 9 61 5 14')   the actual input

    for line in sys.stdin:
        if any([1 > 0, 1 == 0, 1 < 0]):
            print('True')
        else:
            print('False')

    for line in sys.stdin:
        if (line > 0) and all(['a' < 'b', 'b' < 'c']):
            print('True')
        else:
            print('False')
