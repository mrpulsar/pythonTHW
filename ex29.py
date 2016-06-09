people = 20
cats = 30
dogs = 15

if people < cats:
  print "Too many cats! The world is doomed!"

if people > cats:
  print "Not many cats! The world is saved!"

if people < dogs:
  print "The world is drooled on!"

if people > dogs:
  print "The world is dry!"

dogs += 5

if people >= dogs:
  print "People are greater than or equal to dogs."

if people <= dogs:
  print "People are less than or equal to dogs."


if people == dogs:
  print "People are dogs."

# Study drill, using a function to test several statements from exercise 27.
statement = ("chunky" == "bacon" and (not (3 == 4 or 3 == 3))) # Statement num 19: false
statement2 = "test" != "testing" # Statement num 11: true

def logic_check(statements):
  if statements:
    print "It's true!"
  else:
    print "it's.... false!"

logic_check(statement)
logic_check(statement2)
# Exercise 29 What if
  # Using if conditionals