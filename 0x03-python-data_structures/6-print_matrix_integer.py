#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for y in range(len(x)):
            if y == 0:
                print("{}".format(x[y]), end='')
            else:
                print(" {}".format(x[y]), end='')
        print()
