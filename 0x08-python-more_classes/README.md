# 0x08. Python - More Classes and Objects
This project entails more examples on how use classes in Python.

## 0-rectangle.py
An empty class `Rectangle` that defines a rectangle.

## 1-rectangle.py
A class Rectangle that defines a rectangle by:
* Private instance attribute: `width`:
  * property `def width(self):` to retrieve it
  * property setter `def width(self, value):` to set it:
    * width must be an integer, otherwise a `TypeError` exception with the message `width must be an integer` is raised.
    * if `width` is less than 0, a `ValueError` exception with the message `width must be >= 0` is raised.
* Private instance attribute: `height`:
  * property `def height(self):` to retrieve it
  * property setter `def height(self, value):` to set it:
    * `height` must be an integer, otherwise a `TypeError` exception with the message `height must be an integer` is raised.
    * if `height` is less than 0, a `ValueError` exception with the message `height must be >= 0` is raised.
* Instantiation with optional width and height: `def __init__(self, width=0, height=0):`

## 2-rectangle.py
A class Rectangle that defines a rectangle by:
* Private instance attribute: `width:` * property `def width(self):` to retrieve it * property setter `def width(self, value):` to set it: - `width` must be an integer, otherwise a `TypeError` exception with the message `width must be an integer` is raised. - if `width` is less than `0`, a `ValueError` exception with the message `width must be >= 0` is raised.
* Private instance attribute: `height`: * property `def height(self):` to retrieve it * property setter `def height(self, value):` to set it: - `height` must be an integer, otherwise a `TypeError` exception with the message `height must be an integer` is raised. - if `height` is less than `0`, a `ValueError` exception with the message `height must be >= 0` is raised.
* Instantiation with optional width and height: `def __init__(self, width=0, height=0):`
* Public instance method: `def area(self):` that returns the rectangle area.
* Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  * if `width` or `height` is equal to 0, perimeter is equal to 0

## 3-rectangle.py
A class Rectangle that defines a rectangle by:
* Private instance attribute: `width`: * property `def width(self):` to retrieve it * property setter `def width(self, value):` to set it: - `width` must be an integer, otherwise a `TypeError` exception with the message `width must be an integer` is raised. - if `width` is less than 0, a `ValueError` exception with the message `width must be >= 0` is raised.
* Private instance attribute: `height`: * property `def height(self):` to retrieve it * property setter `def height(self, value):` to set it: - `height` must be an integer, otherwise a `TypeError` exception with the message `height must be an integer` is raised. - if `height` is less than 0, a `ValueError` exception with the message `height must be >= 0` is raised.
* Instantiation with optional width and height: `def __init__(self, width=0, height=0):`
* Public instance method: `def area(self):` that returns the rectangle area.
* Public instance method: `def perimeter(self):` that returns the rectangle perimeter: * if `width` or `height` is equal to 0, perimeter is equal to 0
* `print()` and `str()` should print the rectangle with the character #:
  * if `width` or `height` is equal to 0, return an empty string

## 4-rectangle.py
A class Rectangle that defines a rectangle by:
* Private instance attribute: `width`: * property `def width(self):` to retrieve it * property setter `def width(self, value):` to set it: - `width` must be an integer, otherwise a `TypeError` exception with the message `width must be an integer` is raised. - if width is less than 0, a ValueError exception with the message width must be >= 0 is raised.
* Private instance attribute: `height`: * property `def height(self):` to retrieve it * property setter `def height(self, value): to set it:` - `height` must be an integer, otherwise a `TypeError` exception with the message `height must be an integer` is raised. - if `height` is less than 0, a `ValueError` exception with the message `height must be >= 0` is raised.
* Instantiation with optional width and height: `def __init__(self, width=0, height=0):`
* Public instance method: `def area(self):` that returns the rectangle area.
* Public instance method: `def perimeter(self):` that returns the rectangle perimeter: * if `width` or `height` is equal to 0, perimeter is equal to 0
* `print()` and `str()` should print the rectangle with the character #: * if `width` or `height` is equal to 0, return an empty string
* `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`

## 5-rectangle.py
A class Rectangle that defines a rectangle by:
* Private instance attribute: `width`: * property `def width(self):` to retrieve it * property setter `def width(self, value):` to set it: - `width` must be an integer, otherwise a `TypeError` exception with the message `width must be an integer` is raised. - if `width` is less than 0, a `ValueError` exception with the message `width must be >= 0` is raised.
* Private instance attribute: `height`: * property `def height(self):` to retrieve it * property setter `def height(self, value):` to set it: - `height` must be an integer, otherwise a `TypeError` exception with the message `height must be an integer` is raised. - if `height` is less than 0, a `ValueError` exception with the message `height must be >= 0` is raised.
* Instantiation with optional width and height: `def __init__(self, width=0, height=0):`
* Public instance method: `def area(self):` that returns the rectangle area.
* Public instance method: `def perimeter(self):` that returns the rectangle perimeter: * if width or height is equal to 0, perimeter is equal to 0
* print() and str() should print the rectangle with the character #: * if `width` or `height` is equal to 0, return an empty string
* `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
* Print the message `Bye rectangle...` (`...` are 3 dots not ellipsis) when an instance of `Rectangle` is deleted.

## 6-rectangle.py
A class Rectangle that defines a rectangle by:
* Private instance attribute: `width`: * property `def width(self):` to retrieve it * property setter `def width(self, value):` to set it: - `width` must be an integer, otherwise a `TypeError` exception with the message `width must be an intege`r is raised. - if `width` is less than 0, a `ValueError` exception with the message `width must be >= 0` is raised.
* Private instance attribute:`height`: * property `def height(self):` to retrieve it * property setter `def height(self, value):` to set it: - `height` must be an integer, otherwise a `TypeError` exception with the message `height must be an integer` is raised. - if `height` is less than 0, a `ValueError` exception with the message `height must be >= 0` is raised.
* Public class attribute `number_of_instances:`
  * Initialized to 0
  * Incremented during each new instance instantiation
  * Decremented during each instance deletion
* Instantiation with optional **width** and **height**: `def __init__(self, width=0, height=0):`
* Public instance method: `def area(self):` that returns the rectangle area.
* Public instance method: `def perimeter(self):` that returns the rectangle perimeter: * if `width` or `height` is equal to 0, perimeter is equal to 0
* `print()` and `str()` should print the rectangle with the character #: * if `width` or `height` is equal to 0, return an empty string
* `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
* Print the message `Bye rectangle...` (`...` are 3 dots not ellipsis) when an instance of `Rectangle` is deleted.
## 7-rectangle.py
A class Rectangle that defines a rectangle by:
* Private instance attribute: `width`: * property `def width(self):` to retrieve it * property setter `def width(self, value):` to set it: - `width` must be an integer, otherwise a `TypeError` exception with the message `width must be an integer` is raised. - if `width` is less than 0, a `ValueError` exception with the message `width must be >= 0` is raised.
* Private instance attribute: `height`: * property `def height(self):` to retrieve it * property setter `def height(self, value):` to set it: - `height` must be an integer, otherwise a TypeError exception with the message height must be an integer is raised. - if height is less than 0, a `ValueError` exception with the message `height must be >= 0` is raised.
* Public class attribute `number_of_instances:`
  * Initialized to `0`
  *  Incremented during each new instance instantiation
  * Decremented during each instance deletion
* Public class attribute `print_symbol`:
  * Initialized to `#`
  * Used as symbol for string representation
  * Can be any type
* Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
* Public instance method: `def area(self):` that returns the rectangle area.
* Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  * if `width` or `height` is equal to 0, perimeter is equal to `0`
* `print()` and `str()` should print the rectangle with the character(s) stored in `print_symbol`:
  * if `width` or `height` is equal to 0, return an empty string
* `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
* Print the message `Bye rectangle...` (`...` are 3 dots not ellipsis) when an instance of `Rectangle` is deleted.

## 8-rectangle.py
A class `Rectangle` that defines a rectangle by: (based on `7-rectangle.py`)
* Private instance attribute: `width`:
  * property `def width(self):` to retrieve it
  * property setter `def width(self, value):` to set it:
    * `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    * if `width` is less than 0, raise a `ValueError` exception with the message `width must be >= 0`
* Private instance attribute: `height`:
  * property `def height(self):` to retrieve it
  * property setter `def height(self, value):` to set it:
    * `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
    * if `height` is less than 0, raise a `ValueError` exception with the message `height must be >= 0`
* Public class attribute `number_of_instances`:
  * Initialized to `0`
  * Incremented during each new instance instantiation
  * Decremented during each instance deletion
* Public class attribute `print_symbol`:
  * Initialized to `#`
  * Used as symbol for string representation
  * Can be any type
* Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
* Public instance method: `def area(self):` that returns the rectangle area
* Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  * if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
* `print()` and `str()` should print the rectangle with the character `#`:
  * if `width` or `height` is equal to 0, return an empty string
* `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
* Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
* Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
  * `rect_1` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_1 must be an instance of Rectangle`
  * `rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_2 must be an instance of Rectangle`
  * Returns `rect_1` if both have the same area value

## 9-rectangle.py
A class `Rectangle` that defines a rectangle by: (based on `8-rectangle.py`)

* Private instance attribute: `width`:
  * property `def width(self):` to retrieve it
  * property setter `def width(self, value):` to set it:
    * `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    * if `width` is less than 0, raise a `ValueError` exception with the message `width must be >= 0`
* Private instance attribute: `height`:
  * property `def height(self):` to retrieve it
  * property setter `def height(self, value):` to set it:
    * `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
    * if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
* Public class attribute `number_of_instances`:
  * Initialized to `0`
  * Incremented during each new instance instantiation
  * Decremented during each instance deletion
* Public class attribute `print_symbol`:
  * Initialized to `#`
  * Used as symbol for string representation
  * Can be any type
* Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
* Public instance method: `def area(self):` that returns the rectangle area
* Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  * if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
* `print()` and `str()` should print the rectangle with the character #:
  * if `width` or `height` is equal to 0, return an empty string
* `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using eval()
* Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
* Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
  * `rect_`1 must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_1 must be an instance of Rectangle`
  * `rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_2 must be an instance of Rectangle`
  * Returns `rect_1` if both have the same area value
* Class method `def square(cls, size=0):` that returns a new Rectangle instance with `width == height == size`

# N.B: we were not allowed to import any module for all those `MANDATORY TASKS`.

## 10. N queens
![Judit-photo1_602x433](https://github.com/elyse502/alx-higher_level_programming/assets/125453474/be3529ce-6e3d-447f-8aca-efb2db90fe80)

_Chess grandmaster [Judit Polgár](https://en.wikipedia.org/wiki/Judit_Polg%C3%A1r), the strongest female chess player of all time_

The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

* Usage: `nqueens N`
  * If the user called the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with the status `1`
* where N must be an integer greater or equal to `4`
  * If N is not an integer, print `N must be a number`, followed by a new line, and exit with the status `1`
  * If N is smaller than 4, print `N must be at least 4`, followed by a new line, and exit with the status `1`
* The program should print every possible solution to the problem
  * One solution per line
  * Format: see example
  * You don’t have to print the solutions in a specific order
* You are only allowed to import the `sys` module
Read: [Queen](https://en.wikipedia.org/wiki/Queen_%28chess%29), [Backtracking](https://en.wikipedia.org/wiki/Backtracking)
