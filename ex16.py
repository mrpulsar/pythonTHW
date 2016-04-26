#import argument variable from system module
from sys import argv
# assign python script and a filename to argument variable (argv)
script, filename = argv
#Next three prints outline options to user for erasing the passed in file or keeping it as is.
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
# At this point the user can hit RETURN or CTRL-C depending on whether they want to or not.
	# Good to do in case the input file was a typo/accidental and you want to back out.
raw_input("?")
# Let the user know we're opening the file in this python script
print "Opening the file..."
# Assign the filename variable and 'w' for how we are going to change it. w = write (meaning we're going to edit it)
target = open(filename, 'w')

# If the user continues at this point they will be basically deleting the file. Truncating is essentially reformatting the file size of the file. Since we pass in no size variable, I'm certain it defaults to 0.
print "Truncating the file. Goodbye!"
target.truncate()

# Let user know we're going to ask them for input.
print "Now I'm going to ask you for three lines."
# Let the user give three inputs separately.
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
# Let user know the input they gave will be written to the file.
print "I'm going to write these to the file."
# Now we write the input itself to the file, using the escape character '\n' for a new line.
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Then we (and also state that we are going to) close the text file, THIS IS IMPORTANT AND NECESSARY!
print "And finally, we close it."
target.close()

# Exercise 16: Reading and Writing Files
	# From the Exercise:
		# close	-	Closes the file. Like 'File->Save...' in your editor.
		# read  -	Reads the contents of the file. You can assign the result to a variable.
		# readline - Reads just one line of a text file
		# truncate - Empties the file. Watch out if you care about the file.
		# write('stuff') - Writes "stuff" to the file.