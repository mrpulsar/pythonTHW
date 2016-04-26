# Exercise 5: More Variables and Printing
# Embedding a variable into a string and printing them. It is called a 'format string'

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.00 # inches
weight = 180.00 # lbs (pounds)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# Part of study drill, conversion of inch to centimeter, and pounds to kilograms
metric_height = height * 2.54 		# 1 inch = 2.54 centimeters
mass_weight = weight / 2.20462 		# 1 kg = 2.20462 lbs

print "Let's talk about %s" % name
print "He's %r inches tall." % height
print "He's %r centimeters tall." % metric_height
print "He's %r pounds heavy." % weight
print "He's %r kilograms heavy." % mass_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right (Author's Notes)
print "If I add %r, %r, and %r I get %r." % (age, height, weight, age + height + weight)


#Here are all the format characters for adding variables, values, etc. into strings.
#Type code	C Type				Python Type			Minimum size in bytes
#'c'			char				character			1
#'b'			signed char			int					1
#'B'			unsigned char		int					1
#'u'			Py_UNICODE			Unicode character	2
#'h'			signed short		int					2
#'H'			unsigned short		int					2
#'i'			signed int			int					2
#'I'			unsigned int		long				2
#'l'			signed long			int					4
#'L'			unsigned long		long				4
#'f'			float				float				4
#'d'			double				float				8
