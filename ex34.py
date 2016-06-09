# Exercise 34: Accessing Elements of Lists
# list elements and pointers.
  # animals = ['bear', 'tiger', 'penguin', 'zebra']
  # The values (when calling them) are:
  # animals[0] = bear, animals[2] = penguin, animals[3] = zebra

# Exercise: (Write down correct answer to given list
  # animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
  
  # The animal at 1?
    # The animal at 1 is the python, it is the second animal in the list.
  # The third animal?
    # The third animal is the peacock, at location 2
  # The first animal?
    # The first animal is at location 0 and is a bear
  # The animal at 3?
    # The animal at location 3 is the Kangaroo and fourth animal.
  # The fifth animal?
    # The fifth animal, at location 4, is the whale
  # The animal at 2?
    # The animal at 2 is the peacock, the third list item.
  # The sixth animal?
    # platypus is the sixth animal and it's array position in the list is 5.
  # The animal at 4?
    # The animal at 4 is the Whale, which is the fifth animal on the list.
    
animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
i = 0
place = i + 1
for name in animals:
  print name, ": %i, %i place" % (i, place)
  i += 1
  place += 1
  