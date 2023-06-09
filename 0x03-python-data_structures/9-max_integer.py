#!/usr/bin/python3
def max_integer(my_list=[]):
    max_value = my_list[0]
    if len(my_list) == 0:
        return None
    for i in my_list:
        if i > max_value:
            max_value = i
        else:
            continue
    return max_value
