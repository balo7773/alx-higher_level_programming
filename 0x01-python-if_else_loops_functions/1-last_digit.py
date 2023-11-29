#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    y = (-1*number) % 10
    if y < 6 and y != 0:
        print(f"Last digit of {number} is -{y} and is less than 6 and not 0")
if number > 0:
    x = number % 10
    if x > 5:
        print(f"Last digit of {number} is {x} and is greater than 5")
    elif x == 0:
        print(f"Last digit of {number} is {x} and is 0")
