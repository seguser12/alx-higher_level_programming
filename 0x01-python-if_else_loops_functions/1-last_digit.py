#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = number % -10
else:
    last_digit = number % 10
strn = f"Last digit of {number} is {last_digit} "
condit = ["and is greater than 5", "and is 0", "and is less than 6 and not 0"]

if last_digit > 5:
    print(strn + condit[0])
elif last_digit == 0:
    print(strn + condit[1])
elif last_digit < 0:
    print(strn + condit[2])
