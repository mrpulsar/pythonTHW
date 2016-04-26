# Defining function "cheese_and_crackers" with arguments "cheese_count" and "boxes_of_crackers delimited by commas
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	# Following print's outputs to console the amount of cheeses and boxes of crackers, and additional information regarding them.
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
# The print explains another way of 'passing' arguments to a function, in this case, 20 and 30, which are ints.
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# This just explains that we can also use variables in our python script to call a function.
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
# Here we run the function passing in the two variables we just declared as the arguments.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Here, we run the function doing basic arithmetic inside it. In this case, the arguments are both the sums of two ints.
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# Last example showing we can combine arithmetic and variables when passing values to our functions arguments.
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# My own function, per the study drill.
	# Arguments require double data-type format. e.g. 2.00, 3.14, 6.02
def magic_deck(name, creatures, spells, lands):
	deck = creatures + spells + lands
	print "Deck: %s" % name
	print "You have %i creatures in your deck, which makes up %d percent of your deck."  % (creatures, (creatures/ deck)*100.00) 
	print "You have %i spells, making up  %d percent of your deck" % (spells, (spells / deck) * 100.00)
	print "Finally, %i lands making up the remaining %d percent of your deck.\nHave fun!\n\n" % (lands, (lands/ deck) * 100.00)


deck_name = "Thundering Valley"	
magic_deck(deck_name, 24.00,12.00,24.00)
magic_deck(deck_name, 24.00, 12.00, 24.00)
magic_deck(deck_name, 20.0, 20.0, 20.0)
magic_deck(deck_name, 28.0, 8.0, 24.0)
magic_deck(deck_name, 20.0, 16.0, 24.0)
magic_deck(deck_name, 16.0, 20.0, 24.0)
magic_deck(deck_name, 10.0, 20.0, 30.0)
magic_deck(deck_name, 14.0, 22.0, 24.0)
magic_deck(deck_name, 18.0, 18.0, 24.0)
magic_deck(deck_name, 15.0, 20.0, 25.0)