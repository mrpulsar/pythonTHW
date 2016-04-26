# From system library import argument variable
from sys import argv
# Assigning the python script and the filename to be given as argv's
script, filename = argv
# Using previous lesson technique, making prompt for raw_input
prompt = '> '
# Declaring a "file object" using variable name txt. 
	# Easier to express the file's contents and name via methods or calling with short names.
txt = open(filename)

# Here we are calling the filename
print "Here's your file %r:" % filename
# Here we are calling the contents with the .read() method on txt, part of the open() module.
print txt.read()
# Per study drill, add a close argument to close the files.
txt.close()

# print "Type the filename again:"
# file_again = raw_input(prompt)
# 
# txt_again = open(file_again)
# 
# print txt_again.read()
# txt_again.close()

# Exercise 15: Reading Files
# Learn Python The Hard Way learnpythonthehardway.org/book/ex15.html

# Reminder of getting input from user using raw_input with argument variables (argv)

# Notes:
	# Remember to import
	# Make note to close all files that are opened.
	# Use variables to shorten file objects/functions to minimize duplication.

