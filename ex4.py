# Exercise 4: Variables and Names A variable is nothing more than a name
# for something.
	# That something can be a value and represented as an expression.
	# 
# Defined variables for this exercise that contain a simple value:
cars = 100 
space_in_a_car = 4
drivers = 30 
passengers = 90
# Defined variables that use an expression to output a value
#cars (100) - drivers (30) = 70
cars_not_driven = cars - drivers
#This is needed for the average_passengers_per_car var. It is equal to 70 
cars_driven = drivers	
# carpool_capacity will output a value of the expression cars_driven * space_in_a_car
carpool_capacity = cars_driven * space_in_a_car	
#Average is calculated by taking passengers and dividing by cars_driven
average_passengers_per_car = passengers / cars_driven	

#This will output the amount of cars available.
print "There are", cars, "cars available."
#This will output the amount of drivers available.
print "Thare are only", drivers, "drivers available."
#This will output the cars_not_driven variable, an expression of cars -
#drivers.
print "There will be", cars_not_driven, "empty cars today."
#This will output the carpool_capacity, which is an expression of
#cars_driven * space_in_a_car
print "We can transport", carpool_capacity, "people today"
#This will output the passengers variable for how many there are in the
#carpool.
print "We have", passengers, "to carpool today."
#This will output the average_passengers_per_car variable, an expression
#of passengers / cars_driven
print "We need to put about", average_passengers_per_car, "in each car."

# In this lessons study drill, an error is pointed out the author made
# while writing this exercise. The error is that he typed in the name of
# a variable wrong. The intended variable was carpool_capacity and the
# author had written car_pool_capacity adding a underscore between car
# and pool instead of one word carpool.

# Study Drills:
# 1. The same output is given essentially except for line 4 of the output will say "120" instead of "120.0".
	# The reason is because if a floating point value is used with integer values, it becomes parsed into a floating point.
# 2. < Nothing I need to do, only notes about floating point (3.0, 4.0) vs integers (3, 4) >
# 3. Comments added in this exercise
# 4. = is more of an assignment operator than an 'equals' sign, but |
# 	  	|remember it is also an equal sign aside from being used to |
# 	  	|assign variables to expressions/values.					|
# 5. Note to remember that "_" is called a Underscore (without quotes of course), used as spaces when needed.
# 6. I ran various examples using the following variables: x = 2, y = 3, z = 4.
	# Some examples included addition +, subtraction -, multiplication (product) *, and division (quotient) /.
	# Math Operators, listed in order of operation (order they are calculated), plus other operators after them:
	#	Parens:			()	
	#	Exponent:		x**n   where x is the base and n is the exponent	
	#	Multiply:		*	
	#	Divide:			/	
	#	Add: 			+	
	#	Subtract:		-	
	#
	#	less-than:	  			<		Strictly less than value cutoff (can not be true at value)
	#	greater-than: 			>		Strictly greater than value cutoff (can not be true at value)
	#	less-than-or-equal:		<=		Must be designated cutoff or less than it (can be true at value)
	#	greater-than-or-equal: 	>=		Must be designated cutoff or greater than it (can be true at value)
	#	
	#	modulus:	%	Modulus takes the remainder of a value given another value. 4 % 2 would be 0, since 2 goes into 4 twice. 3 % 2 would equal 1, since 2 goes into 3 one time and has a left over remainder of 1
	#	
	
	
	



