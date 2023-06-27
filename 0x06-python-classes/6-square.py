#!/usr/bin/python3
""" Module 6-square: class Square. """


class Square():
    """
        Square: defines a square.
        Attributes:
            size (int): size of square.
            position(int tuple): position of square.
        Method:
                __init__ : init of size attribute for each instance.
    """

    def __init__(self, size=0, position=(0, 0)):

        """ Initialization of attributes for instances
            Args:
                size (int): size of the square.
                position (int tuple): position of the square.
        """
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Getter function for private attribute size.
            Returns:
                size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter function for private attribute size.
            Args:
                value: size value to set to.
        """
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Getter function for private attribute position.
            Returns:
                position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
            Setter function for private attribute position.
            Args:
                value: position value to set to.
        """
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ Area of the square. """
        return self.__size * self.__size

    def my_print(self):
        """
            Prints the square with character #
        """
        if self.__size == 0:
            print()
            return
        for y in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()
