#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    temp = (-1)*number
    last = temp % 10
    last *= -1
else:
    last = number % 10
if last > 5:
    str = "greater than 5"
elif last < 6 and last != 0:
    str = "less than 6 and not 0"
else:
    str = "0"

print(f"Last digit of {number} is {last} and is {str}")
