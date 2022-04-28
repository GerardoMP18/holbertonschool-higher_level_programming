#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    num = len(argv)
    if num > 1:
        if num == 2:
            a = 1
            print("1 argument:")
            print("{}: {}".format(a, argv[1]))
        else:
            print("{} arguments:".format(num - 1))
            for write in range(1, num):
                print("{}: {}".format(write, argv[write]))
    else:
        print("0 arguments.")
