#!/usr/bin/python3
"""
Module 1-my_list
Contains class MyList
inherits from list; has public instance method to print sorted
"""


class MyList(list):
    """ Class that inherits the attributes references of class list
    Args:
        list: class list
    """

    def print_sorted(self):
        """ Method that prints the sorted list """
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
