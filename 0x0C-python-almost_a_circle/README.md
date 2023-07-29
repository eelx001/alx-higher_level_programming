# 0x0C. Python - Almost a circle
# Background Context
The AirBnB project is a big part of the Higher level curriculum. This project will help you be ready for it.
_In this project, you will review everything about Python:_
* Import
* Exceptions
* Class
* Private attribute
* Getter/Setter
* Class method
* Static method
* Inheritance
* Unittest
* Read/Write file

You will also learn about:
* `args` and `kwargs`
* Serialization/Deserialization
* JSON

https://github.com/elyse502/alx-higher_level_programming/assets/125453474/4b840456-33f2-42cc-a6f9-a3b720712ab7

# Resources🧵
### Read or watch:
* [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
* [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
* [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)
# Tasks 📃 OVERVIEW📝
In this project, I encapsulated skills in Python object-oriented programming by coding three connected classes to represent rectangles and squares. I wrote my own test suite using the `unittest` module to test all functionality for each class.

The three classes involved utilizing the following Python tools:

* Import
* Exceptions
* Private attributes
* Getter/setter
* Class/static methods
* Inheritance
* File I/O
* `args`/`kwargs`
* JSON and CSV serialization/deserialization
* Unittesting
## Tests ✔️
[tests/test_models](https://github.com/elyse502/alx-higher_level_programming/tree/master/0x0C-python-almost_a_circle/tests/test_models): Folder containing the following independently-developed test files:
  * [test_base.py](https://github.com/elyse502/alx-higher_level_programming/blob/master/0x0C-python-almost_a_circle/tests/test_base.py)
  * [test_rectangle.py](https://github.com/elyse502/alx-higher_level_programming/blob/master/0x0C-python-almost_a_circle/tests/test_rectangle.py)
  * [test_square.py](https://github.com/elyse502/alx-higher_level_programming/blob/master/0x0C-python-almost_a_circle/tests/test_square.py)
## Classes 🆑
### Base
Represents the "base" class for all other classes in the project. Includes:
* Private class attribute `__nb_objects = 0`.
* Public instance attribute `id`.
* Class constructor `def __init__(self, id=None):`
  * If `id` is `None`, increments `__nb_objects` and assigns its value to the public instance attribute `id`.
  * Otherwise, sets the public instance attribute `id` to the provided `id`.
* Static method `def to_json_string(list_dictionaries):` that returns the JSON string serialization of a list of dictionaries.
  * If `list_dictionaries` is `None` or empty, returns the string `"[]"`.
* Class method `def save_to_file(cls, list_objs):` that writes the JSON serialization of a list of objects to a file.
  * The parameter `list_objs` is expected to be a list of `Bas`e-inherited instances.
  * If  `list_objs` is `None`, the function saves an empty list.
  * The file is saved with the name `<cls name>.json` (ie. `Rectangle.json`)
  * Overwrites the file if it already exists.
* Static method `def from_json_string(json_string):` that returns a list of objects deserialized from a JSON string.
  * The parameter `json_string` is expected to be a string representing a list of dictionaries.
  * If `json_string` is `None` or empty, the function returns an empty list.
* Class method `def create(cls, **dictionary):` that instantiates an object with provided attributes.
  * Instantiates an object with the attributes given in `**dictionary`.
* Class method `def load_from_file(cls):` that returns a list of objects instantiated from a JSON file.
  * Reads from the JSON file `<cls name>.json` (ie. `Rectangle.json`)
  * If the file does not exist, the function returns an empty list.
* Class method `def save_to_file_csv(cls, list_objs):` that writes the CSV serialization of a list of objects to a file.
  * The parameter `list_objs` is expected to be a list of `Base`-inherited instances.
  * If `list_objs` is `None`, the function saves an empty list.
  * The file is saved with the name `<cls name>.csv` (ie. `Rectangle.csv`)
  * Serializes objects in the format `<id>,<width>,<height>,<x>,<y>` for `Rectangle` objects and `<id>,<size>,<x>,<y>` for `Square` objects.
* Class method `def load_from_file_csv(cls):` that returns a list of objects instantiated from a CSV file.
  * Reads from the CSV file `<cls name>.csv` (ie. `Rectangle.csv`)
  * If the file does not exist, the function returns an empty list.
* Static method `def draw(list_rectangles, list_squares):` that draws `Rectangle` and `Square` instances in a **GUI** window using the `turtle` module.
  * The parameter `list_rectangles` is expected to be a list of `Rectangle` objects to print.
  * The parameter `list_squares` is expected to be a list of `Square` objects to print.

### Rectangle
Represents a rectangle. Inherits from `Base` with:
* Private instance attributes `__width`, `__height`, `__x`, and `__y`.
  * Each private instance attribute features its own getter/setter.
* Class constructor `def __init__(self, width, height, x=0, y=0, id=None):`
  * If either of `width`, `height`, `x`, or `y` is not an integer, raises a `TypeError` exception with the message `<attribute> must be an integer`.
  * If either of `width` or `height` is >= 0, raises a `ValueError` exception with the message `<attribute> must be > 0`.
  * If either of `x` or `y` is less than 0, raises a `ValueError` exception with the message `<attribute> must be >= 0`.
* Public method `def area(self):` that returns the area of the `Rectangle` instance.
* Public method `def display(self):` that prints the `Rectangle` instance to `stdout` using the `#` character.
  * Prints new lines for the `y` coordinate and spaces for the `x` coordinate.
* Overwrite of `__str__` method to print a `Rectangle` instance in the format `[Rectangle] (<id>) <x>/<y>`.
* Public method `def update(self, *args, **kwargs):` that updates an instance of a `Rectangle` with the given attributes.
  * `*args` must be supplied in the following order:
    * 1st: `id`
    * 2nd: `width`
    * 3rd: `height`
    * 4th: `x`
    * 5th: `y`
   * `**kwargs` is expected to be a double pointer to a dictionary of new key/value attributes to update the `Rectangle` with.
   * `**kwargs` is skipped if `*args` exists.
* Public method `def to_dictionary(self):` that returns the dictionary representation of a `Rectangle` instance.

### Square
Represents a square. Inherits from `Rectangle` with:
* Class constructor `def __init__(self, size, x=0, y=0, id=None):`
  * The `width` and `height` of the `Rectangle` superclass are assigned using the value of `size`.
* Overwrite of `__str__` method to print a `Square` instance in the format `[Square] (<id>) <x>/<y>`.
* Public method `def update(self, *args, **kwargs):` that updates an instance of a `Square` with the given attributes.
  * `*args` must be supplied in the following order:
    * 1st: `id`
    * 2nd: `size`
    * 3rd: `x`
    * 4th: `y`
  * `**kwargs` is expected to be a double pointer to a dictoinary of new key/value attributes to update the `Square` with.
  * `**kwargs` is skipped if `*args` exists.
* Public method `def to_dictionary(self):` that returns the dictionary representation of a `Square`.

# Tasks 📃
## If it's not tested it doesn't work: 0. tests/
All your files, classes and methods must be unit tested and be PEP 8 validated.
```
guillaume@ubuntu:~/$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/$
```
_Note that this is just an example. The number of tests you create can be different from the above example._

## 1. Base class: models/base.py, models/__init__.py
The  first class `Base`:

Create a folder named `models` with an empty file `__init__.py` inside - with this file, the folder will become a Python package

Create a file named `models/base.py:`
* Class `Base`:
  * private class attribute `__nb_objects = 0`
  * class constructor: `def __init__(self, id=None):`:
    * if `id` is not `None`, assign the public instance attribute id with this argument value - you can assume `id` is an integer and you don’t need to test the type of it
    * otherwise, increment `__nb_objects` and assign the new value to the public instance attribute `id`

This class will be the “base” of all other classes in this project. The goal of it is to manage id attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)
```
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)

guillaume@ubuntu:~/$ ./0-main.py
1
2
3
12
4
guillaume@ubuntu:~/$ 
```

## 2.  First Rectangle: models/rectangle.py
The class `Rectangle` that inherits from `Base`:
* In the file `models/rectangle.py`
* Class `Rectangle` inherits from `Base`
* Private instance attributes, each with its own public getter and setter:
  * `__width` -> `width`
  * `__height` -> `height`
  * `__x` -> `x`
  * `__y` -> `y`
* Class constructor: `def __init__(self, width, height, x=0, y=0, id=None):`
  * Call the super class with `id` - this super call with use the logic of the `__init__` of the `Base` class
  * Assign each argument `width`, `height`, `x` and `y` to the right attribute

Why private attributes with getter/setter? Why not directly public attribute?

Because we want to protect attributes of our class. With a setter, you are able to validate what a developer is trying to assign to a variable. So after, in your class you can “trust” these attributes.
```
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)

guillaume@ubuntu:~/$ ./1-main.py
1
2
12
guillaume@ubuntu:~/$ 
```

## 3. Validate attributes: models/rectangle.py
Update the class `Rectangle` by adding validation of all setter methods and instantiation (`id` excluded):
* If the input is not an integer, raise the `TypeError` exception with the message: `<name of the attribute> must be an integer`. Example: `width must be an integer`
* If `width` or `height` is under or equals 0, raise the `ValueError` exception with the message: `<name of the attribute> must be > 0`. Example: `width must be > 0`
* If `x` or `y` is under 0, raise the `ValueError` exception with the message: `<name of the attribute> must be >= 0`. Example: `x must be >= 0`
```
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
""" 2-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    try:
        Rectangle(10, "2")
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.width = -10
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r = Rectangle(10, 2)
        r.x = {}
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        Rectangle(10, 2, 3, -1)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/$ ./2-main.py
[TypeError] height must be an integer
[ValueError] width must be > 0
[TypeError] x must be an integer
[ValueError] y must be >= 0
guillaume@ubuntu:~/$ 
```

## 4. Area first: models/rectangle.py
Update the class `Rectangle` by adding the public method `def area(self):` that returns the area value of the `Rectangle` instance.
```
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
""" 3-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(3, 2)
    print(r1.area())

    r2 = Rectangle(2, 10)
    print(r2.area())

    r3 = Rectangle(8, 7, 0, 0, 12)
    print(r3.area())

guillaume@ubuntu:~/$ ./3-main.py
6
20
56
guillaume@ubuntu:~/$ 
```
## 5. Display #0: models/rectangle.py
Update the class `Rectangle` by adding the public method `def display(self):` that prints in stdout the `Rectangle` instance with the character `#` - you don’t need to handle `x` and `y` here.
```
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
""" 4-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6)
    r1.display()

    print("---")

    r1 = Rectangle(2, 2)
    r1.display()

guillaume@ubuntu:~/$ ./4-main.py
####
####
####
####
####
####
---
##
##
guillaume@ubuntu:~/$ 
```
## 6.  __str__: models/rectangle.py
Update the class `Rectangle` by overriding the `__str__` method so that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height>`
```
guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
""" 5-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6, 2, 1, 12)
    print(r1)

    r2 = Rectangle(5, 5, 1)
    print(r2)

guillaume@ubuntu:~/$ ./5-main.py
[Rectangle] (12) 2/1 - 4/6
[Rectangle] (1) 1/0 - 5/5
guillaume@ubuntu:~/$ 
```
## 7. Display #1: models/rectangle.py
Update the class `Rectangle` by improving the public method `def display(self):` to print in stdout the `Rectangle` instance with the character `#` by taking care of `x` and `y`
```
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
""" 6-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(2, 3, 2, 2)
    r1.display()

    print("---")

    r2 = Rectangle(3, 2, 1, 0)
    r2.display()

guillaume@ubuntu:~/$ ./6-main.py | cat -e
$
$
  ##$
  ##$
  ##$
---$
 ###$
 ###$
guillaume@ubuntu:~/$ 
```
## 8. Update #0: models/rectangle.py
Update the class `Rectangle` by adding the public method `def update(self, *args):` that assigns an argument to each attribute:
* 1st argument should be the `id` attribute
* 2nd argument should be the `width` attribute
* 3rd argument should be the `height` attribute
* 4th argument should be the `x` attribute
* 5th argument should be the `y` attribute

This type of argument is called a “no-keyword argument” - Argument order is super important.
```
guillaume@ubuntu:~/$ cat 7-main.py
#!/usr/bin/python3
""" Doc """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(89)
    print(r1)

    r1.update(89, 2)
    print(r1)

    r1.update(89, 2, 3)
    print(r1)

    r1.update(89, 2, 3, 4)
    print(r1)

    r1.update(89, 2, 3, 4, 5)
    print(r1)

guillaume@ubuntu:~/$ ./7-main.py
[Rectangle] (1) 10/10 - 10/10
[Rectangle] (89) 10/10 - 10/10
[Rectangle] (89) 10/10 - 2/10
[Rectangle] (89) 10/10 - 2/3
[Rectangle] (89) 4/10 - 2/3
[Rectangle] (89) 4/5 - 2/3
guillaume@ubuntu:~/$ 
```
## 9. Update #1: models/rectangle.py
Update the class `Rectangle` by updating the public method `def update(self, *args):` by changing the prototype to `update(self, *args, **kwargs)` that assigns a key/value argument to attributes:
* `**kwargs` can be thought of as a double pointer to a dictionary: key/value
  * As Python doesn’t have pointers, `**kwargs` is not literally a double pointer – describing it as such is just a way of explaining its behavior in terms you’re already familiar with
* `**kwargs` must be skipped if `*args` exists and is not empty
* Each key in this dictionary represents an attribute to the instance

This type of argument is called a “key-worded argument”. Argument order is not important.
```
guillaume@ubuntu:~/$ cat 8-main.py
#!/usr/bin/python3
""" 8-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(height=1)
    print(r1)

    r1.update(width=1, x=2)
    print(r1)

    r1.update(y=1, width=2, x=3, id=89)
    print(r1)

    r1.update(x=1, height=2, y=3, width=4)
    print(r1)

guillaume@ubuntu:~/$ ./8-main.py
[Rectangle] (1) 10/10 - 10/10
[Rectangle] (1) 10/10 - 10/1
[Rectangle] (1) 2/10 - 1/1
[Rectangle] (89) 3/1 - 2/1
[Rectangle] (89) 1/3 - 4/2
guillaume@ubuntu:~/$ 
```



