#!/usr/bin/python3
for i in reversed(range(ord('a'), ord('z') + 1)):
    print("{}".format(chr(i if(i % 2 == 0) else (i - 32))), end="")
