# 0x06. Python - Classes and Objects
Object Oriented Programming(**OOP**) in python

## 0-square.py
* An empty class `Square` that defines a square

## 1-square.py
A class Square that defines a square by: (based on 0-square.py) \n Private instance attribute: size Instantiation with size (no type/value verification)

## 2-square.py
* A class `Square` that defines a square by: (based on `1-square.py`)
* Private instance attribute: `size`
* Instantiation with optional size: `def __init__(self, size=0):`
* Size must be an integer, otherwise raise a TypeError exception with \n the message `size must be an integer`
* If size is less than 0, raise a ValueError exception with the message \n `size must be >= 0`

## 3-square.py
* A class `Square` that defines a square by: (based on `2-square.py`)
* Instantiation with optional size: `def __init__(self, size=0):`
* size must be an integer, otherwise raise a `TypeError` exception \n with the message `size must be an integer`

## 4-square.py
* A class Square that defines a square by: (based on 3-square.py)
* Private instance attribute: `size`
* property `def size(self):` to retrieve it
* property setter `def size(self, value):` to set it:
  * `size` must be an integer, otherwise raise a `TypeError` exception with \n the message size must be an `integer`
  * if `size` is less than `0`, raise a `ValueError` exception with the \n message `size must be >= 0`

## 5-square.py
* A class Square that defines a square by: (based on `4-square.py`)
* private instance attribute: `size`
* property `def size(self):` to retrieve it
* property setter def size(self, value): to set it
  * `size` must be an integer, otherwise raise a `TypeError` exception with \n the message `size must be an integer`
  * if `size` is less than `0`, raise a `ValueError` exception with the \n message `size must be >= 0`
* Instantiation with optional size: `def __init__(self, size=0):`
* Public instance method: `def area(self):` that returns the current \n square area
* Public instance method: `def my_print(self):` that prints in stdout \n the square with the character `#`:
  * if `size` is equal to 0, print an empty line

## 6-square.py
* A class`Square` that defines a square by: (based on `5-square.py`)

* Private instance attribute: `size:`

* property `def size(self):` to retrieve it

* property setter `def size(self, value):` to set it:

  * `size` must be an integer, otherwise raise a `TypeError` exception with \n the message `size must be an integer`
  * if `size` is less than 0, raise a `ValueError` exception with the \n message `size must be >= 0`
* Private instance attribute:`position:`

  * property def position(self): to retrieve it
  * property setter `def position(self, value):` to set it:
    * position must be a tuple of 2 positive integers, otherwise raise a \n `TypeError` exception with the message `position must be a tuple of 2 positive integers`
* Instantiation with optional `size` and optional position: \n `def __init__(self, size=0, position=(0, 0)):`

* Public instance method: `def area(self):` that returns the current \n square area

* Public instance method: `def my_print(self):` that prints in stdout the \n square with the character `#`:

* if `size`
