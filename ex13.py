#This is saying: Import the system module, where argv is the "argument variable"
	#argv or argument variables, a standard in programming. This variable holds arguments passed through python script when ran. It's demonstrated in this exercise and explained on line 13.
from sys import argv

script, first, second, third = argv

# You have to supply all variables needed in the terminal for this to work correctly.
	# Attempt using only two argument variables ended up with an error saying at least 3 are required.
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# Script is another name for py (python) files. 
# When running this program, you must include the command line arguments needed (at least one, but three in this case)
# so instead of typing just: 	python ex13.py
			#Type Instead:		python ex13.py first 2nd 3rd
			
			
