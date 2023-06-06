#!/usr/bin/python3
for char in range(97, 123, -1):
	if char % 2 == 0:
		print("{:c}".format(char - 32), end='')
	print("{:c}".format(char), end='')
