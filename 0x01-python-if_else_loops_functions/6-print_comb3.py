#!/usr/bin/python3

for num1 in range(10):
    for num2 in range(num1, 10):
        if num1 == 8 and num2 == 9:
            print("{}{}".format(num1, num2), end='\n')
        elif num1 != num2:
            print("{}{}".format(num1, num2), end=', ')
