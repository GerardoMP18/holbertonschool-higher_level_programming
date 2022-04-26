#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = "Last digit of"
greater = "and is greater than 5"
zero = "and is 0"
less = "and is less than 6 and not 0"
if (number % 10 > 5):
    print("{} {} is {} {}".format(string, number, number % 10, greater))
elif (number % 10 == 0):
    print("{} {} is {} {}".format(string, number, number % 10, zero))
elif (number < 0):
    print("{} {} is -{} {}".format(string, number, (number * -1) % 10, less))
else:
    print("{} {} is {} {}".format(string, number, number % 10, less))
