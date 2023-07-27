# 0x00. Python - Hello, World
![48a9fdbd67c84a328a9df9ec8d93b9ac2458ac37721d7d53e51a27fb2bdc5263](https://github.com/elyse502/alx-higher_level_programming/assets/125453474/2b80fd80-0cca-41d8-95ea-932d38656223)

# Author’s disclaimer
```
Welcome to the Python world!

The first projects are more "C-oriented" - no tricks, no funky syntax - simple!
If you've already played with Python, don't worry, fun things will come.
You'll soon find that with Python (and the majority of higher level languages), there are ten different ways to do the same thing. Some tasks will expect only one implementation, while other tasks will have multiple possible implementations.
Like C, Python also has a linter / style guide like Betty, called PEP8, also now known as PyCode.

Enjoy!

- Guillaume
```
# Resources🧵
### Read or watch:
* [The Python tutorial](https://docs.python.org/3/tutorial/index.html) (only the first three chapters below)
* [Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html)
* [Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html)
* [An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html) (Read up until “3.1.2. Strings” included)
* [How To Use String Formatters in Python 3](https://realpython.com/python-f-strings/)
* [Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
* [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)

# Tasks 📃
## 0-run
A Shell script that runs a Python script.

The Python file name will be saved in the environment variable `$PYFILE`
```
guillaume@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Best School")

guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
guillaume@ubuntu:~/py/0x00$ ./0-run
Best School
guillaume@ubuntu:~/py/0x00$ 
```

## 1-run_inline
A Shell script that runs Python code.

The Python code will be saved in the environment variable `$PYCODE`
```
guillaume@ubuntu:~/py/0x00$ export PYCODE='print(f"Best School: {88+10}")'
guillaume@ubuntu:~/py/0x00$ ./1-run_inline 
Best School: 98
guillaume@ubuntu:~/py/0x00$
```

## 2-print.py
A Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.

Use the function `print`
```
guillaume@ubuntu:~/py/0x00$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$
```

## 3-print_number.py
Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.
* You can find the source code [here](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py)
* The output of the script should be:
  * the number, followed by Battery street,
  * followed by a new line
* You are not allowed to cast the variable number into a string
* Your code must be 3 lines long
* You have to use f-strings [tips](https://realpython.com/python-f-strings/)
```
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$ 
```

# Pycodestyle
`Pycodestyle` is now the [new standard of Python style code](https://github.com/PyCQA/pycodestyle/issues/466)

![Flyingcircus_2](https://github.com/elyse502/alx-higher_level_programming/assets/125453474/f0117a02-f354-4b5d-89ee-e88075d5e3dc)
