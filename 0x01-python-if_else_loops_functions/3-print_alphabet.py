#!/usr/bin/python3

for char in range(ord('a'), ord('z') + 1):
    if chr(char) in ('e', 'q'):
        continue
    print("{}".format(chr(char)), end='')
