# Variable "x" with a string formatted to include a double num, in this case an int displayed as one.
x = "There are %d types of people." % 10
# Variable declaration of binary and do_not as strings
binary = "binary"
do_not = "don't"
# Variable y is a string formatted to include two other strings, the two above.
y = "Those who know %s and those who %s." % (binary, do_not)

# Outputs out "There are 10 types of people. Those who know binary and those who don't."
print x
print y

# Outputs out a formatted string saying "I said: There are 10 types of people."
print "I said: %r." % x
# Outputs out a formatted string: "I also said: 'Those who know binary and those who don't'."
print "I also said: '%s'." % y

# Variable declaration: first one is boolean, second is formatted string with no declared variable.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# Outputs 'joke_evaluation' which needs and uses 'hilarious' for its formatted string character.
print joke_evaluation % hilarious

# Outputs "This is the left side of...a string with a right side." at line 30
w = "This is the left side of..."
e = "a string with a right side."
# A concatenation of two variable strings outputted.
print w + e

# The reason the string is made 'longer' when we print 'w + e' is because
	# it is a 'concatenation' of the two strings, meaning that the '+'
	# is actually 'adding' them together and procedurally. If we had typed
	# 'e + w' instead, it would be "a string with a right side. This is the left side of..."
	# which would look in this context inappropriate.
