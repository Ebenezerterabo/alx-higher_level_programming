#!/usr/bin/python
def search_replace(my_list, search, replace):
    modified_list = [x for x in my_list]
    for i, num in enumerate(my_list):
        if i == search - 1:
            modified_list[i] = replace

    return modified_list
