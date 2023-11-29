#!/usr/bin/python3
for y in range(0, 10):
    for x in range(0, 10):
        if y == x:
            continue
        if y < x and y != 8:
            print("{}{}".format(y, x), end=", ")
        elif y == 8 and x == 9:
            print("{}{}".format(y, x))

