# 0x0B. Python - Input/Output
# Resources🧵
### Read or watch:
* [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
* [8.7. Predefined Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)
* [Dive Into Python 3: Chapter 11. Files](https://histo.ucsf.edu/BMS270/diveintopython3-r802.pdf) (_until “11.4 Binary Files” (included)_)
* [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
* [Learn to Program 8 : Reading / Writing Files](https://www.youtube.com/watch?v=EukxMIsNeqU)
* [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) (_ch. 8 p 180-183 and ch. 14 p 326-333_)
* [All about py-file I/O](https://techvidvan.com/tutorials/python-file-read-write/)
# Tasks 📃
In this project, I practiced file handling in Python. I used the builtin `with`, `open`, and `read` functions with the `json` module to read and write files and serialize and deserialize objects with [**JSON**](https://en.wikipedia.org/wiki/JSON).
## 0-read_file.py
A function that reads a text file (**`UTF8`**) and prints it to stdout:
* Prototype: `def read_file(filename=""):`
* You must use the with statement
* You don’t need to manage `file permission` or `file doesn't exist` exceptions.
* You are not allowed to import any module

## 1-write_file.py
A function that writes a string to a text file (**`UTF8`**) and returns the number of characters written:
* Prototype: `def write_file(filename="", text=""):`
* You must use the `with` statement
* You don’t need to manage file permission exceptions.
* Your function should create the file if doesn’t exist.
* Your function should overwrite the content of the file if it already exists.
* You are not allowed to import any module

## 2-append_write.py
A function that appends a string at the end of a text file (**`UTF8`**) and returns the number of characters added:
* Prototype: `def append_write(filename="", text=""):`
* If the file doesn’t exist, it should be created
* You must use the `with` statement
* You don’t need to manage `file permission` or `file doesn't exist` exceptions.
* You are not allowed to import any module

## 3-to_json_string.p
A function that returns the JSON representation of an object (string):
* Prototype: `def to_json_string(my_obj):`
* You don’t need to manage exceptions if the object can’t be serialized.

## 4-from_json_string.py
A function that returns an object (Python data structure) represented by a JSON string:
* Prototype: `def from_json_string(my_str):`
* You don’t need to manage exceptions if the JSON string doesn’t represent an object.

## 5-save_to_json_file.py
A function that writes an Object to a text file, using a JSON representation:
* Prototype: `def save_to_json_file(my_obj, filename):`
* You must use the `with` statement
* You don’t need to manage exceptions if the object can’t be serialized.
* You don’t need to manage file permission exceptions.

## 6-load_from_json_file.py
A function that creates an Object from a “JSON file”:
* Prototype: `def load_from_json_file(filename):`
* You must use the `with` statement
* You don’t need to manage exceptions if the JSON string doesn’t represent an object.
* You don’t need to manage file permissions / exceptions.

## 7-add_item.py
A script that adds all arguments to a Python list, and then save them to a file:
* You must use your function `save_to_json_file` from `5-save_to_json_file.py`
* You must use your function `load_from_json_file` from `6-load_from_json_file.py`
* The list must be saved as a JSON representation in a file named `add_item.json`
* If the file doesn’t exist, it should be created
* You don’t need to manage file permissions / exceptions.

## 8-class_to_json.py
A function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:
* Prototype: `def class_to_json(obj):`
* `obj` is an instance of a Class
* All attributes of the `obj` Class are serializable: list, dictionary, string, integer and boolean
* You are not allowed to import any module

## 9-student.py
A class **`Student`** that defines a student by:
* Public instance attributes:
  * `first_name`
  * `last_name`
  * `age`
* Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
* Public method `def to_json(self):` that retrieves a dictionary representation of a **`Student`** instance (same as `8-class_to_json.py`)
* You are not allowed to import any module

## 10-student.py
A class **`Student`** that defines a student by: (based on `9-student.py`)
* Public instance attributes:
  * `first_name`
  * `last_name`
  * `age`
* Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
* Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a **`Student`** instance (same as `8-class_to_json.py)`:
  * If `attrs` is a list of strings, only attribute names contained in this list must be retrieved.
  * Otherwise, all attributes must be retrieved
* You are not allowed to import any module

## 11-student.py
A class **`Student`** that defines a student by: (based on `10-student.py`)
* Public instance attributes:
 * `first_name`
 * `last_name`
 * `age`
* Instantiation with `first_name`, `last_name` and `age`: `def __init__(self, first_name, last_name, age):`
* Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a **`Student`** instance (same as `8-class_to_json.py`):
 * If `attrs` is a list of strings, only attributes name contain in this list must be retrieved.
 * Otherwise, all attributes must be retrieved
* Public method `def reload_from_json(self, json):` that replaces all attributes of the **`Student`** instance:
 * You can assume `json` will always be a dictionary
 * A dictionary key will be the public attribute name
 * A dictionary value will be the value of the public attribute
* You are not allowed to import any module

**_Now, you have a simple implementation of a serialization and deserialization mechanism (concept of representation of an object to another format, without losing any information and allow us to rebuild an object based on this representation)_**

## 12-pascal_triangle.py
Technical interview preparation:
* You are not allowed to google anything
* Whiteboard first

A function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal’s triangle of n:
* Returns an empty list if `n <= 0`
* You can assume `n` will be always an integer
* You are not allowed to import any module

## 100-append_after.py
A function that inserts a line of text to a file, after each line containing a specific string (see example):
* Prototype: `def append_after(filename="", search_string="", new_string=""):`
* You must use the `with` statement
* You don’t need to manage `file permission` or `file doesn't exist` exceptions.
* You are not allowed to import any module

## 101-stats.py
A script that reads stdin line by line and computes metrics:
* Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`
* Each 10 lines and after a keyboard interruption (**`CTRL + C`**), prints those statistics since the beginning:
  * Total file size: `File size: <total size>`
  * where is the sum of all previous (see input format above)
  * Number of lines by status code:
    * possible status code: `200`, `301`, `400`, `401`, `403`, `404`, `405` and `500`
    * if a status code doesn’t appear, don’t print anything for this status code
    * format: `<status code>: <number>`
    * status codes should be printed in ascending order
