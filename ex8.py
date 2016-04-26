# Exercise 8: Printing, Printing
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
		#The reason the next string outputs using "" instead of '' is 
		#because it has an apostrophe in the string itself, 
		# meaning if you use '' it'd end after "But it didn", 
		# and it will display an error if tried with single quotes.
	"But it didn't sing.",
	"So I said goodnight."
)

# Testing the formatter myself just to analyze behavior
##print formatter % (formatter, "Hello!", "Red", 2)
# Notice the next print (one not in original exercise) maintains brackets but excludes parenthesis.
##print formatter % (formatter, (formatter), formatter, [formatter])

