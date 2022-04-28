#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    suma = 0
    for x in range(1, len(argv)):
        suma = suma + int(argv[x])
    print(suma)
