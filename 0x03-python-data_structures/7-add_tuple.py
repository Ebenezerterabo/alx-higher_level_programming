#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    max_len = max(len(tuple_a), len(tuple_b))
    result = []

    for i in range(max_len):
        tp1 = tuple_a[i] if i < len(tuple_a) else 0
        tp2 = tuple_b[i] if i < len(tuple_b) else 0
        result.append(tp1 + tp2)
    return tuple(result)
