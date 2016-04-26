# + plus
# - minus
# / slash
# * asterisk
# % percent
# < less-than
# > greater-than
# <= less-than-equal
# >= greater-than-equal

#Lets the end-user know we will be counting chickens.
print "I will now count my chickens."
# This prints the quantity of Hens and Roosters respectively, on separate lines each.
# The first equation looks more proper as "25 + (30 / 6)" which equals 30 as it's 25 + 5.
print "Hens", 25.0 + 30.0 / 6.0 
# the output of the whole equation will be 97 as it's essentially 100 - 3 once simplified
print "Roosters", 100.0 - 25.0 * 3.0 % 4.0 
# This output declares the preceding outputs purpose.
print "Now I will count the eggs:"
# As mentioned above, this is the equation the line above refers to
# This equation looks confusing, but in excel the equation is: 
#	  3 + 2 + 1 - 5 + MOD(4,2) - 1 / 4 + 6 = 7 where 7 is the output we see when run.
print 3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0
# This prints a string.
print "Is it true that 3 + 2 < 5 - 7?"
# This outputs a boolean value that is the equation used in the string above
print 3 + 2 < 5 - 7 # Evaluates false
# Next two lines print a string and an expression (addition, subtraction)
print "What is 3 + 2?", 3.0 + 2.0
print "What is 5 - 7?", 5.0 - 7.0
# After comparing the two sides of the first conditional, it's seen that 3+2 > 5-7, which is also 5 > -2 which is false, as this sentence declares as a string:
print "Oh, that's why it's False."
# Another string letting the user know the program is continuing.
print "How about some more."
# Printing strings and conditional expressions, "Is it greater? True" for example should be the output for the next line. The following lines after it are the same idea.
print "Is it greater?", 5.0 > -2.0
print "Is it greater or equal?", 5.0 >= -2.0
print "Is it less or equal?", 5.0 <= -2.0