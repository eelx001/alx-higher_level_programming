# 0x07. Python - Test-driven development
# Background Context
### Important notice on intranet checks for Python projects
Starting from today:
* Based on the requirements of each task, **you should always write the documentation (module(s) + function(s)) and tests first**, before you actually code anything
* The intranet checks for Python projects won’t be released before their first deadline, in order for you to focus more on TDD and think about all possible cases
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case. **But not in the implementation of them!**
* **Don’t trust the user**, always think about all possible edge cases
# Resources🧵
### Read or watch:
* [doctest — Test interactive Python examples](https://docs.python.org/3.4/library/doctest.html) (_until “26.2.3.7. Warnings” included_)
* [doctest – Testing through documentation](https://pymotw.com/3/doctest/)
* [Unit Tests in Python](https://www.youtube.com/watch?v=1Lfv5tUGsn8)
* [Unittest module](https://www.youtube.com/watch?v=6tNS--WetLI)
* [Interactive and Non-interactive tests](https://mattermost.com/blog/testing-python-understanding-doctest-and-unittest/)
# Tasks 📃
## 0-add_integer.py, tests/0-add_integer.txt
A function that adds 2 integers.
* Prototype: `def add_integer(a, b=98):`
* a and b must be integers or floats, otherwise raise a `TypeError` exception with the message `a must be an integer` or `b must be an integer`
* `a` and `b` must be first casted to integers if they are float
* Returns an integer: the addition of `a` and `b`
* You are not allowed to import any module
```
guillaume@ubuntu:~/0x07$ cat 0-main.py
#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x07$ ./0-main.py
3
98
100
98
b must be an integer
a must be an integer
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/0-add_integer.txt | tail -2
9 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$ python3 -c 'print(__import__("0-add_integer").__doc__)' | wc -l
5
guillaume@ubuntu:~/0x07$ python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)' | wc -l
3
guillaume@ubuntu:~/0x07$ 
```

## 2-matrix_divided.py, tests/2-matrix_divided.txt
A function that divides all elements of a matrix.
* Prototype: `def matrix_divided(matrix, div):`
* matrix must be a list of lists of integers or floats, otherwise raise a `TypeError` exception with the message `matrix must be a matrix (list of lists) of integers/floats`
* Each row of the `matrix` must be of the same size, otherwise raise a `TypeError` exception with the message `Each row of the matrix must have the same size`
* `div` must be a number (integer or float), otherwise raise a `TypeError` exception with the message `div must be a number`
* `div` can’t be equal to `0`, otherwise raise a `ZeroDivisionError` exception with the message `division by zero`
* All elements of the matrix should be divided by `div`, rounded to 2 decimal places
* Returns a new matrix
* You are not allowed to import any module
```
guillaume@ubuntu:~/0x07$ cat 2-main.py
#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

guillaume@ubuntu:~/0x07$ ./2-main.py
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
[[1, 2, 3], [4, 5, 6]]
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/2-matrix_divided.txt | tail -2
5 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$ 
```
Note: you might have a different number of tests than in the above example. As usual, your tests should cover all possible cases.

## 3-say_my_name.py, tests/3-say_my_name.txt
A function that prints `My name is <first name> <last name>`
* Prototype: `def say_my_name(first_name, last_name=""):`
* `first_name` and `last_name` must be strings otherwise, raise a `TypeError` exception with the message `first_name must be a string` or `last_name must be a string`
* You are not allowed to import any module
```
guillaume@ubuntu:~/0x07$ cat 3-main.py
#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name

say_my_name("John", "Smith")
say_my_name("Walter", "White")
say_my_name("Bob")
try:
    say_my_name(12, "White")
except Exception as e:
    print(e)

guillaume@ubuntu:~/0x07$ ./3-main.py | cat -e
My name is John Smith$
My name is Walter White$
My name is Bob $
first_name must be a string$
guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/3-say_my_name.txt | tail -2
5 passed and 0 failed.
Test passed.
guillaume@ubuntu:~/0x07$
```
Note: you might have a different number of tests than in the above example. As usual, your tests should cover all possible cases.

## 4-print_square.py
A function that prints a square with the character `#`.

## 5-text_indentation.py
A function that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`

## tests/6-max_integer_test.py
Unittests for the function `def max_integer(list=[]):`.

## 100-matrix_mul.py
A  function that multiplies 2 matrices:
* Read: [Matrix multiplication - only Matrix product (two matrices)](https://en.wikipedia.org/wiki/Matrix_multiplication)

## 101-lazy_matrix_mul.py
A function that multiplies 2 matrices by using the module `NumPy`.
* To install it: `pip3 install numpy==1.15.0`

## 102-python.c
![2c4f2b92514745519f833afdf5bc5f3eaff8c6ca](https://github.com/elyse502/alx-higher_level_programming/assets/125453474/07704351-2398-4e96-a38c-aa90e79866d8)

A function that prints Python strings.
* Read: [Unicode HOWTO](https://docs.python.org/3.4/howto/unicode.html)
