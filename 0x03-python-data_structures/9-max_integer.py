#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        Biggest = my_list[0]
        for i in my_list:
            if i > Biggest:
                Biggest = i
        return Biggest
    else:
        return None
