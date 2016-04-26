age = int(raw_input("How old are you? "))
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")
print "So, you're %i years old, %s tall and %s heavy." % (
	age, height, weight)

# study drills: look up pydoc, what is it?

# pydoc is a way to look at documentation for python as well as documentation for a specific python file.
	# You can also access it for particular built in functions/methods/etc.
		# Typing this into terminal:	pydoc raw_input
			# This produces documentation help on what that command, in this case, raw_input, does.
					# Remember to press Q to quit while using pydoc in the terminal.
	
# From common student questions:
# The input() function has security problems and should be avoided if possible. It also converts input as if it were python code rather than alphanumerical input.

# pydoc help on modules:
	# open
		#open(...)
    		# open(name[, mode[, buffering]]) -> file object
 	   		# 
    		# Open a file using the file() type, returns a file object.  This is the
    		# preferred way to open a file.  See file.__doc__ for further information.
    # file 
		# class file(object)
		# |  file(name[, mode[, buffering]]) -> file object
		# |  
		# |  Open a file.  The mode can be 'r', 'w' or 'a' for reading (default),
		# |  writing or appending.  The file will be created if it doesn't exist
		# |  when opened for writing or appending; it will be truncated when
		# |  opened for writing.  Add a 'b' to the mode for binary files.
		# |  Add a '+' to the mode to allow simultaneous reading and writing.
		# |  If the buffering argument is given, 0 means unbuffered, 1 means line
		# |  buffered, and larger numbers specify the buffer size.  The preferred way
		# |  to open a file is with the builtin open() function.
		# |  Add a 'U' to mode to open the file for input with universal newline
		# |  support.  Any line ending in the input file will be seen as a '\n'
		# |  in Python.  Also, a file so opened gains the attribute 'newlines';
		# |  the value for this attribute is one of None (no newline read yet),
		# |  '\r', '\n', '\r\n' or a tuple containing all the newline types seen.
		# |  
		# |  'U' cannot be combined with 'w' or '+' mode.
		# - This was all I bothered to grab, there is methods defined 
		# further using 'pydoc file'-
	# os
	#	NAME
    #os - OS routines for NT or Posix depending on what system we're on.

#FILE
#    /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/os.py

#MODULE DOCS
#    http://docs.python.org/library/os

#DESCRIPTION
#    This exports:
#      - all functions from posix, nt, os2, or ce, e.g. unlink, stat, etc.
#      - os.path is one of the modules posixpath, or ntpath
#      - os.name is 'posix', 'nt', 'os2', 'ce' or 'riscos'
#      - os.curdir is a string representing the current directory ('.' or ':')
#      - os.pardir is a string representing the parent directory ('..' or '::')
#      - os.sep is the (or a most common) pathname separator ('/' or ':' or '\\')
#      - os.extsep is the extension separator ('.' or '/')
#      - os.altsep is the alternate pathname separator (None or '/')
#      - os.pathsep is the component separator used in $PATH etc
#      - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
#
	