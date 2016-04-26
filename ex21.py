def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for extra credit, type it in anyway
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
#	add
#	1.
#		age = 35 
#	2.
#			74 - 4500 = -4426
#
#			weight * divide = 4500
#			weight = 180
#			divide=25
#
#	3. 35 + (-4426) = -4391
#
#
#
print "That becomes: ", what, "Can you do it by hand?"
						# -4391
						# I got it correct without checking, first time! :D - Austin @ 12:21PM Monday April 4 2016
#	Exercise 21:
	#	Functions Can Return Something
		# The purpose of this exercise is to demonstrate how functions in python return values with given arguments.