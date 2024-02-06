#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    n = 0
    for element in range(list_length):
        try:
            n = my_list_1[element] / my_list_2[element]
        except TypeError:
            print("wrong type")
            n = 0
        except IndexError:
            print("out of range")
            n = 0
        except ZeroDivisionError:
            print("division by 0")
            n = 0
        finally:
            new_list.append(n)
    return new_list
