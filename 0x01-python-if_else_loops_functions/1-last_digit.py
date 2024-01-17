#!/usr/bin/python3
import random
number = random.randint(-1000, 1000)

last_dig = abs(number) % 10

if number < 0:
    last_dig = -last_dig

if last_dig > 5:
    print(f"Last digit of {number:d} is {last_dig:d} and is greater than 5")
elif last_dig < 6 and last_dig != 0:
    print(f"Last digit of {number:d} is {last_dig:d}"
          f" and is less than 6 and not 0")
else:
    print(f"Last digit of {number:d} is {last_dig:d} and is 0")
