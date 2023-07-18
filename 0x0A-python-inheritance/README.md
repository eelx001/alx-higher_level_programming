# 0x0A. Python - Inheritance
# Resources🧵
### Read or watch:
* [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
* [Multiple inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)
* [Inheritance in Python](https://www.geeksforgeeks.org/inheritance-in-python/)
* [Learn to Program 10 : Inheritance Magic Methods](https://www.youtube.com/watch?v=d8kCdLCi6Lk)
# Tasks 📃
*Of course, a language feature would not be worthy of the name **`“class”`** without supporting inheritance.*
## 0-lookup.py
A function that returns the list of available attributes and methods of an object:
* Prototype: `def lookup(obj):`
* Returns a `list` object
* You are not allowed to import any module

## 1-my_list.py, tests/1-my_list.txt
A class `MyList` that inherits from `list`:
* Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)
* You can assume that all the elements of the list will be of type `int`
* You are not allowed to import any module

## 2-is_same_class.py
A function that returns `True` if the object is exactly an instance of the specified class ; otherwise `False`.
* Prototype: `def is_same_class(obj, a_class):`
* You are not allowed to import any module

## 3-is_kind_of_class.py
A function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False`.
* Prototype: `def is_kind_of_class(obj, a_class):`
* You are not allowed to import any module

## 4-inherits_from.py
A function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`.
* Prototype: `def inherits_from(obj, a_class):`
* You are not allowed to import any module

## 5-base_geometry.py
An empty class **`BaseGeometr`**.
* You are not allowed to import any module

## 6-base_geometry.py
A class `BaseGeometry` (based on **`5-base_geometry.py`**).
* Public instance method: `def area(self):` that raises an `Exception` with the message **`area() is not implemented`**
* You are not allowed to import any module

## 7-base_geometry.py, tests/7-base_geometry.txt
A class `BaseGeometry` (based on **`6-base_geometry.py`**).
* Public instance method: `def area(self):` that raises an `Exception` with the message **`area() is not implemented`**
* Public instance method: `def integer_validator(self, name, value):` that validates `value:`
  * you can assume **`name`** is always a string
  * if `value` is not an integer: raise a `TypeError` exception, with the message **`<name> must be an integer`**
  * if `value` is less or equal to 0: raise a `ValueError` exception with the message **`<name> must be greater than 0`**
* You are not allowed to import any module

## 8-rectangle.py
A class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`).
* Instantiation with `width` and `height`: `def __init__(self, width, height):`
  * `width` and `height` must be private. No getter or setter
  * `width` and `height` must be positive integers, validated by **`integer_validator`**
 
## 9-rectangle.py
A class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`). (task based on `8-rectangle.py`)
* Instantiation with `width` and `height`: `def __init__(self, width, height):`:
  * `width` and `height` must be private. No getter or setter
  * `width` and `height` must be positive integers validated by `integer_validator`
* the `area()` method must be implemented
* `print()` should print, and `str()` should return, the following rectangle description: **`[Rectangle] <width>/<height>`**

## 10-square.py
A class `Square` that inherits from `Rectangle` (`9-rectangle.py`):
* Instantiation with size: def __init__(self, size)::
  * `size` must be private. No getter or setter
  * `size` must be a positive integer, validated by **`integer_validator`**
* the `area()` method must be implemented

## 11-square.py
A class `Square` that inherits from `Rectangle` (`9-rectangle.py`). (task based on `10-square.py`).
* Instantiation with `size`: `def __init__(self, size):`:
 * `size` must be private. No getter or setter
 * `size` must be a positive integer, validated by `integer_validator`
* the `area()` method must be implemented
* `print()` should print, and `str()` should return, the square description: **`[Square] <width>/<height>`**

## 100-my_int.py 
A class `MyInt` that inherits from `int`:
* `MyInt` is a rebel. **`MyInt`** has `==` and `!=` operators inverted
* You are not allowed to import any module

## 101-add_attribute.py
A  function that adds a new attribute to an object if it’s possible:
* Raise a `TypeError` exception, with the message `can't add new attribute` if the object can’t have new attribute
* You are not allowed to use **`try/except`**
* You are not allowed to import any module
