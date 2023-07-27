# 0x03. Python - Data Structures: Lists, Tuples
# Resources🧵
### Read or watch:
* [3.1.3. Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
* [Data structures](https://docs.python.org/3/tutorial/datastructures.html) (until **_`5.3. Tuples and Sequences`_** included)
* [Learn to Program 6 : Lists](https://www.youtube.com/watch?v=A1HUzrvS-Pw)

# Tasks 📃
## 0-print_list_integer.py
A function that prints all integers of a list.
* Prototype: `def print_list_integer(my_list=[]):`
* Format: one integer per line. See example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
* You have to use `str.format()` to print integers
```
guillaume@ubuntu:~/0x03$ cat 0-main.py
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

guillaume@ubuntu:~/0x03$ ./0-main.py
1
2
3
4
5
guillaume@ubuntu:~/0x03$ 
```

## 1-element_at.py
A function that retrieves an element from a list like in C.
* Prototype: `def element_at(my_list, idx):`
* If `idx` is negative, the function should return `None`
* If `idx` is out of range (> of number of element in `my_list`), the function should return None`
* You are not allowed to import any module
* You are not allowed to use `try/except`
```
guillaume@ubuntu:~/0x03$ cat 1-main.py
#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

guillaume@ubuntu:~/0x03$ ./1-main.py
Element at index 3 is 4
guillaume@ubuntu:~/0x03$ 
```

## 2-replace_in_list.py
A  function that replaces an element of a list at a specific position (like in C).
* Prototype: `def replace_in_list(my_list, idx, element):`
* If `idx` is negative, the function should not modify anything, and returns the original list
* If `idx` is out of range (> of number of element in `my_list`), the function should not modify anything, and returns the original list
* You are not allowed to import any module
* You are not allowed to use `try/except`
```
guillaume@ubuntu:~/0x03$ cat 2-main.py
#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./2-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
guillaume@ubuntu:~/0x03$ 
```

## 3-print_reversed_list_integer.py
A function that prints all integers of a list, in reverse order.

Prototype: `def print_reversed_list_integer(my_list=[]):`
Format: one integer per line. See example
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to use `str.format()` to print integers
```
guillaume@ubuntu:~/0x03$ cat 3-main.py
#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

guillaume@ubuntu:~/0x03$ ./3-main.py
5
4
3
2
1
guillaume@ubuntu:~/0x03$ 
```

## 4-new_in_list.py
A function that replaces an element in a list at a specific position without modifying the original list (like in C).
* Prototype: `def new_in_list(my_list, idx, element):`
* If `idx` is negative, the function should return a copy of the original `list`
* If `idx` is out of range (> of number of element in `my_list`), the function should return a copy of the original `list`
* You are not allowed to import any module
* You are not allowed to use `try/except`
```
guillaume@ubuntu:~/0x03$ cat 4-main.py
#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./4-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
guillaume@ubuntu:~/0x03$ 
```

## 5-no_c.py
A  function that removes all characters `c` and `C` from a string.

Prototype: `def no_c(my_string):`
The function should return the new string
You are not allowed to import any module
You are not allowed to use `str.replace()`
```
guillaume@ubuntu:~/0x03$ cat 5-main.py
#!/usr/bin/env python3
no_c = __import__('5-no_c').no_c

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))

guillaume@ubuntu:~/0x03$ ./5-main.py
Best Shool
hiago
 is fun!
guillaume@ubuntu:~/0x03$
```

## 6-print_matrix_integer.py
A function that prints a matrix of integers.
* Prototype: `def print_matrix_integer(matrix=[[]]):`
* Format: see example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
* You have to use `str.format()` to print integers
```
guillaume@ubuntu:~/0x03$ cat 6-main.py
#!/usr/bin/python3
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

guillaume@ubuntu:~/0x03$ ./6-main.py | cat -e
1 2 3$
4 5 6$
7 8 9$
--$
$
guillaume@ubuntu:~/0x03$ 
```

## 7-add_tuple.py
A function that adds 2 tuples.
* Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
* Returns a tuple with 2 integers:
  * The first element should be the addition of the first element of each argument
  * The second element should be the addition of the second element of each argument
* You are not allowed to import any module
* You can assume that the two tuples will only contain integers
* If a tuple is smaller than 2, use the value `0` for each missing integer
* If a tuple is bigger than 2, use only the first 2 integers
```
guillaume@ubuntu:~/0x03$ cat 7-main.py
#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))

guillaume@ubuntu:~/0x03$ ./7-main.py
(89, 100)
(2, 89)
(1, 89)
guillaume@ubuntu:~/0x03$ 
```

## 8-multiple_returns.py
  * A function that returns a tuple with the length of a string and its first character.

## 9-max_integer.py
  * A function that finds the biggest integer of a list.

## 10-divisible_by_2.py
  * A function that finds all multiples of 2 in a list.

## 11-delete_at.py
  * A function that deletes the item at a specific position in a list.

## 12-switch.py
  * Altered the source code to switch the value of a and b .

## 13-is_palindrome.c
  * A function in C that checks if a singly linked list is a palindrome.

## 100-print_python_list_info.c
  * CPython is the reference implementation of the Python programming language. Written in C, CPython is the default and most widely used implementation of the language. Since we now know a bit of C, we can look at what is happening under the hood of Python. Let’s have fun with Python and C, and let’s look at what makes Python so easy to use.
    * All my files were interpreted/compiled on Ubuntu 14.04 LTS
     
![7e7834b535261d05532fb80a9304f7051c4ad7ac](https://github.com/elyse502/alx-higher_level_programming/assets/125453474/fc2fa043-e4da-4aa1-b449-38f1c11432b2)


## lists.h
  * Contains the prototypes of functions used for this task.
