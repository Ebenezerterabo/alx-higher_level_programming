#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tp1 = tuple_a + (0, 0)
    tp2 = tuple_b + (0, 0)
    new_tuple = tp1[0] + tp2[0], tp1[1] + tp2[1]

    return new_tuple
