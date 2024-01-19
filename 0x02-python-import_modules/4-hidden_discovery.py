#!/usr/bin/python3
import hidden_4 as hid


def main():
    names = sorted(dir(hid))
    for name in names:
        if name[0] != "_":
            print("{}".format(name))


if __name__ == "__main__":
    main()
