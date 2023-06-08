#!/usr/bin/python3
from sys import argv

i, result = 1, 0

if __name__ == "__main__":
    while i < len(argv):
        result += int(argv[i])
        i += 1
    print(result)
