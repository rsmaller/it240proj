#!/usr/bin/python3
# Takes a user-inputted string value or file path and hashes it.

import random
import sys
import math

def divisible_in_list(number, list):
	for value in list:
		if number % value == 0:
			return True
	return False

def is_prime(test_number):
	if test_number % test_number != 0:
		raise ValueError("Number must be an integer")
	if test_number == 1:
		return False
	for value in range(2, int(math.sqrt(test_number))):
		if test_number % value == 0:
			return False
	return True

def generate_random_prime(min, max):
	number = 0
	while not is_prime(number):
		number = random.randint(min, max)
	return number

def string_to_num(string):
	result = 0
	for index in range(len(string)):
		result += ord(string[index]) * ord(string[index - 1])
	return result

def hash(string):
	hash_val = ""
	primer = string_to_num(string)
	primer **= 149
	primer = rectify_string_length(str(primer), 3)
	primer = split_in_increment(primer, 3)
	for index in range(len(primer)):
		if int(primer[index]) < 33:
			primer[index] = int(primer[index]) + 33
		elif int(primer[index]) > 122:
			primer[index] = int(primer[index])
			while primer[index] > 122:
				primer[index] //= 2
		else:
			primer[index] = int(primer[index])
	for index in range(len(primer)):
		primer[index] = chr(primer[index])
	for character in primer:
		hash_val += character
	return hash_val[:32]

def split_in_increment(string, increment):
	split_list = []
	accrue = 1
	split_string  = ""
	for character in string:
		split_string += character
		if accrue % increment == 0:
			split_list.append(split_string)
			split_string = ""
		accrue += 1
	return split_list

def rectify_string_length(string, increment):
	length = len(string)
	if length % increment == 0:
		return string
	else:
		while length % increment != 0:
			length -= 1
		return string[:length]

def readfile(file):
	file = open(file, 'rb')
	return str(file.read())

def main():
	usage_message = "Usage: " + sys.argv[0] + " -h[ash]|-n[umber] STRING or -c[hecksum] FILE"
	if len(sys.argv) < 3:
		print(usage_message)
		quit()
	elif sys.argv[1] == '-h':
		print(hash(sys.argv[2]))
	elif sys.argv[1] == '-n':
		print(string_to_num(sys.argv[2]))
	elif sys.argv[1] == '-c':
		print(hash(readfile(sys.argv[2])))
	else:
		print(usage_message) 

main()