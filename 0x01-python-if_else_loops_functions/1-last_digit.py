#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
fig = abs(number) % 10
if number < 0:
    fig = -fig
print("Last digit of {} is {} and ".format(number, fig), end="")
if fig > 5:
    print("is greater than 5")
elif fig == 0:
    print("is 0")
else:
    print("is less than 6 and not 0")
