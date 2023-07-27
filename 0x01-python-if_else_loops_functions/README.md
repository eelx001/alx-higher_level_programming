# 0x01. Python - if/else, loops, functions
![code](https://github.com/elyse502/alx-higher_level_programming/assets/125453474/bc5ca824-88ef-4f89-bb85-b089d8a8315c)

# Resources🧵
**Read or watch:**
* [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) (Read until “4.6. Defining Functions” included)
* [IndentationError](https://www.youtube.com/watch?v=1QXOd2ZQs-Q)
* [How To Use String Formatters in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)
* [Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
* [Learn to Program 2 : Looping](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
* [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)
### man or help:
* **`python3`**

# More Info
_Note_: you do not need to understand lists yet.

# Tasks 📃
Exploration of control flow, loops and functions in python

## 0-positive_or_negative.py
This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print whether the number stored in the variable `number` is positive or negative.
* You can find the source code [here](https://github.com/alx-tools/0x01.py/blob/master/0-positive_or_negative_py)
* The variable `number` will store a different value every time you will run this program
* You don’t have to understand what `import`, `random. randint` do. Please do not touch this code
* The output of the program should be:
  * The number, followed by
    * if the number is greater than 0: `is positive`
    * if the number is 0: `is zero`
    * if the number is less than 0: `is negative`
  * followed by a new line
```
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-4 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
0 is zero
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-3 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-10 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
10 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
-5 is negative
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
6 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
7 is positive
guillaume@ubuntu:~/0x01$ ./0-positive_or_negative.py 
5 is positive
guillaume@ubuntu:~/0x01$ 
```

## 1-last_digit.py
This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable `number`.

* You can find the source code [here](https://github.com/alx-tools/0x01.py/blob/master/1-last_digit_py)
* The variable `number` will store a different value every time you will run this program
* You don’t have to understand what `import`, `random.randint` do. Please do not touch this code. This line should not change: `number = random.randint(-10000, 10000)`
* The output of the program should be:
  * The string `Last digit` of, followed by
  * the number, followed by
  * the string `is`, followed by the last digit of `number`, followed by
    * if the last digit is greater than 5: the string `and is greater than 5`
    * if the last digit is 0: the string `and is 0`
    * if the last digit is less than 6 and not 0: the string `and is less than 6 and not 0`
  * followed by a new line
```
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 4205 is 5 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -626 is -6 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 1144 is 4 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -9200 is 0 and is 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 5247 is 7 and is greater than 5
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -9318 is -8 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 3369 is 9 and is greater than 5
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -5224 is -4 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of -4485 is -5 and is less than 6 and not 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 3850 is 0 and is 0
guillaume@ubuntu:~/0x01$ ./1-last_digit.py
Last digit of 5169 is 9 and is greater than 5
guillaume@ubuntu:~/0x01$
```
 

## 2-print_alphabet.py
A  program that prints the ASCII alphabet, in lowercase, not followed by a new line.
* You can only use one `print` function with string format
* You can only use one loop in your code
* You are not allowed to store characters in a variable
* You are not allowed to import any module
```
guillaume@ubuntu:~/0x01$ ./2-print_alphabet.py
abcdefghijklmnopqrstuvwxyzguillaume@ubuntu:~/0x01$
```

## 3-print_alphabt.py
A program that prints the ASCII alphabet, in lowercase, not followed by a new line.
* Print all the letters except `q` and `e`
* You can only use one `print` function with string format
* You can only use one loop in your code
* You are not allowed to store characters in a variable
* You are not allowed to import any module
```
guillaume@ubuntu:~/0x01$ ./3-print_alphabt.py
abcdfghijklmnoprstuvwxyzguillaume@ubuntu:~/0x01$
```


## 4-print_hexa.py
A program that prints all numbers from `0` to `98` in decimal and in hexadecimal (as in the following example)
* You can only use one `print` function with string format
* You can only use one loop in your code
* You are not allowed to store numbers or strings in a variable
* You are not allowed to import any module
```
guillaume@ubuntu:~/0x01$ ./4-print_hexa.py
0 = 0x0
1 = 0x1
2 = 0x2
3 = 0x3
4 = 0x4
5 = 0x5
6 = 0x6
7 = 0x7
8 = 0x8
9 = 0x9
10 = 0xa
11 = 0xb
12 = 0xc
13 = 0xd
14 = 0xe
15 = 0xf
16 = 0x10
17 = 0x11
18 = 0x12
...
96 = 0x60
97 = 0x61
98 = 0x62
guillaume@ubuntu:~/0x01$
```

## 5-print_comb2.py
A program that prints numbers from `0` to `99`.
* Numbers must be separated by `,`, followed by a space
* Numbers should be printed in ascending order, with two digits
* The last number should be followed by a new line
* You can only use no more than 2 `print` functions with string format
* You can only use one loop in your code
* You are not allowed to store numbers or strings in a variable
* You are not allowed to import any module
```
guillaume@ubuntu:~/0x01$ ./5-print_comb2.py
00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99
guillaume@ubuntu:~/0x01$
```

## 6-print_comb3.py
A  program that prints all possible different combinations of two digits.
* Numbers must be separated by `,`, followed by a space
* The two digits must be different
* `01` and `10` are considered the same combination of the two digits `0` and `1`
* Print only the smallest combination of two digits
* Numbers should be printed in ascending order, with two digits
* The last number should be followed by a new line
* You can only use no more than 3 `print` functions with string format
* You can only use no more than 2 loops in your code
* You are not allowed to store numbers or strings in a variable
* You are not allowed to import any module
```
guillaume@ubuntu:~/0x01$ ./6-print_comb3.py
01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
guillaume@ubuntu:~/0x01$
```

## 7-islower.py
  * This is a function that checks for lowercase character.

## 8-uppercase.py
  * This is a function that prints a string in uppercase followed by a new line.

## 9-print_last_digit.py
  * This is a function that prints the last digit of a number.

## 10-add.py
  * This is a function that adds two integers and returns the result.

## 11-pow.py
  * This is a function that computes a to the power of b and return the value.

## 12-fizzbuzz.py
  * This is a function that prints the numbers from 1 to 100 separated by a space.

## 13-insert_number.c
  * Technical interview preparation:
    * A function in C that inserts a number into a sorted singly linked list.

## 100-print_tebahpla.py
  * A program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase) , not followed by a new line.

## 101-remove_char_at.py
  * A function that creates a copy of the string, removing the character at the position n (not the Python way, the “C array index”).

## 102-magic_calculation.py
  * The Python function def magic_calculation(a, b, c): that does exactly the same as the following Python bytecode:
    ![Screenshot from 2023-06-09 15-21-09](https://github.com/elyse502/alx-higher_level_programming/assets/125453474/9cc7b6a4-ddb9-4e63-ad18-b3531135047d)
    * tips - [ByteCode](https://docs.python.org/3.4/library/dis.html)


## lists.h
  * Header file containing prototypes for functons used in C programs in this repository.
