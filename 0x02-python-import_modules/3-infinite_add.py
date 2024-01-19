#!/usr/bin/python3
import sys


def main():
    num_args = len(sys.argv) - 1
    total = 0

    if num_args == 0:
        print("{}".format(total))
    else:
        for i in range(1, len(sys.argv)):
            total += int(sys.argv[i])
        print("{}".format(total))


if __name__ == "__main__":
    main()
