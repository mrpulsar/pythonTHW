# Exercise 10

# Stuff to remember: new line character "\n", Remember use of single/double quotes.
# Examples of how to escape (avoid) errors when mixing single/double quotes.
# \' is for single quotes inside of a single quoted string.
# \" is for double quotes inside of a double quoted string.
# print "I am 6'2\" tall."
# print 'I am 6\'2" tall.'

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat



print "Months of the Year:\n" 
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
for month in months: 
  print "\t* %s" % month 


#month_list = '''
#Months of the year:
#\t* %s
#\t* %s
#\t* %s
#\t* %s
#\t* %s
#\t* %s
#\t* %s
#\t* %s
#\t* %s
#\t* %s
#\t* %s
#\t* %s
#''' % month_sort


# Infinite loop, do not use unless you really need to see it:
#while True:
#	for i in ["/","-","|","\\","|"]:
#		print "%s\r" % i



# Escape Sequences list put into my syntax notes. Here is a list the sake of it.
#	Escape				What It Does
#	\\					Backslash
#	\'					Single-Quote
#	\"					Double-Quote
#	\a					ASCII bell (BEL)
#	\b					ASCII backspace (BS)
#	\f					ASCII formfeed (FF)
#	\n					ASCII linefeed (LF)
#	\N{name}			Character named name in the Unicode Database (Unicode Only)
#	\r					Carriage Return (CR)
#	\t					Horizontal Tab (TAB)
#	\uxxxx				Character with 16-bit hex value xxxx (Unicode Only)
#	\Uxxxxxxxx			Character with 32-bit hex value xxxxxxxx (Unicode Only)
#	\v					ASCII vertical tab (VT)
#	\ooo				Character with octal value ooo
#	\xhh 				Character with hex value hh