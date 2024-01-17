#!/usr/bin/python3

def uppercase(str):
    result = ""

    for char in str:
        if char >= 'a' and char <= 'z':
            uppercase_ch = chr(ord(char) - 32)
            result += uppercase_ch
        else:
            result += char
    print(result)
