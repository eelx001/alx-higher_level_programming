#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    New_list = []
    if len(my_list) == 0:
        return None
    for i in range(len(my_list)):
        if (my_list[i] % 2) == 0:
            New_list.append(True)
        else:
            New_list.append(False)
    return New_list
