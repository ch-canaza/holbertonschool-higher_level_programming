#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
str1 = "Last digit of"
if last > 5:
    str2 = "and is greater than 5"
elif last == 0:
    str2 = "and is 0"
else:
    str2 = "and is less than 6 and not 0"
print(str1, "{:d}" .format(number), "is", "{:d}" .format(last), str2)
