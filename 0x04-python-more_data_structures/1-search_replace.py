#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if search >= 1 and search >= len(my_list):
        return my_list

    modified_list = [x for x in my_list]
    for i, num in enumerate(my_list):
        if i == search - 1:
            modified_list[i] = replace

    return modified_list
