# Output the followi to console window
print "Mary had a little lamb."
# Output a formatted string using a %s string format with the string 'snow'.
print "Its fleece was white as %s." % 'snow'
# Output next line to console.
print "And everywhere that Mary went."
# Output 10 periods "." to the console.
print "." * 10 # what'd that do?

# The following variable declarations are technically characters rather than strings. Last one is at line 22.
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
	# The comma acts as a way to negate line breaks.
	# The prints are a concatenated group of char's (characters) that make up "Cheese Burger"
	# When the comma is removed it will say "Cheese", do a line break, then "Burger"
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12
	# Those prints above should output "Cheese Burger" in one line.