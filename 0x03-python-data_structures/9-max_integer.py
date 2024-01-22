#!/usr/bin/python3
def max_integer(my_list=[]):
    max_num = float('-inf')
    if not my_list:
        return None
    else:
        for element in my_list:
            if element > max_num:
                max_num = element

        return max_num
