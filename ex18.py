# this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
		
# ok, that *args is actually pointless, we can do just this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
		
# this takes just one argument
def print_one(arg1):
	print "arg1: %r" % arg1
		
# this one takes no arguments
def print_none():
	print "I got nothin'."


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

# Exercise 18: Names, Variables, Code, Functions
	# Introduction to functions in python
		# Function Syntax:
			# Function with one argument
				# 	def example_function(argument):
				#		print "Argument: %r" % argument
			# Function with no argument
				#	def example_function2(argument, argument2)
				#		print "Argument: %r, Argument 2: %r" % (argument, argument2)
			# Function that acts like argv (can take as many arguments as its given)
				#	def example_funtion3(*arguments)
				#		argument, argument2, argument 3 = args
				#		print "Argument: %r, Argument 2: %r, Argument 3: %r" % (argument, argument2, argument3)