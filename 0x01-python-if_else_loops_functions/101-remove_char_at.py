#!/usr/bin/python3

def remove_char_at(str, n):
    result = ""
    i = 0

    for char in str:
        if i != n:
            result += char
        i += 1

    return result
