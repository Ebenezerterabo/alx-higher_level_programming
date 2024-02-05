#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for element in my_list:
            if x > 0 and isinstance(element, int):
                print("{:d}".format(element), end='')
                count += 1
                x -= 1
        print()
        return count

    except (IndexError, ValueError, TypeError):
        return count
