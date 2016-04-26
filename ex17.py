from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# We could do these two on one line, how?
# in_file = open(from_file)
indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print" Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()

# We may comment this out (or remove it) as we have changed line 10 to optimize script per study drill.
# in_file.close()


# Exercise 17: More Files
# Found at: learnpythonthehardway.org/book/ex17.html

# Notes:
	#	len() is a function (len = length) that returns the length of a passed in string as a number (character count, essentially, which corrolates to bytes. one character = 1 byte
	#	Because I changed the indata variable to include "open(from_file)" and then call the run method, it's unnecessary to close the txt file at the end, because it was never assigned an actual memory space as the file itself.