#!/usr/bin/python3
def search_replace(my_list, search, replace):
    modified_list = [x for x in my_list]
    for i, num in enumerate(my_list):
        if num == search:
            modified_list[i] = replace

    return modified_list
