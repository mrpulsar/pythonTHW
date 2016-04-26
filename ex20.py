from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

print "First lets print the whole file:\n"

print_all(current_file)
# The only difference is I added an escape sequence '\n\' to the print line as the code is the same but does not match the output of learnpythonthehardway exercise 20
print "\nNow let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
# Remember the checklist for functions:
	# def python_function(arguments):
	# 	 python_script
	# 
	# ^^^ One line of delimited whitespace (not tabbed or spaced to close function)
current_file.close()