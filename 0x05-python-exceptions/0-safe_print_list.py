#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for element in my_list:
            if x > 0:
                count += 1
                print(element, end='')
                x -= 1

        print()
        return count

    except:
        return
