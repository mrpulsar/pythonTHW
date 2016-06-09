i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i += 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
    
    
print "The numbers: "

for num in numbers:
    print num

# Study drills, remake using a function.
def countStep(i, x, yArr):
    while i < x:
        print "At the top i is %d" % i
        yArr.append(i)
        
        i = i + 1
        print "Numbers now: ", yArr
        print "At the bottom i is %d" % i
    
    print "The numbers: "
    for num in yArr:
        print num
    
print countStep(5, 12, [])


# Exercise 33 while loops
  # Tips for avoiding problems while using while-loops 
    # Avoid Infinite Loops:
      # NEVER make a while conditional that cannot be met or "finished"
    # From the book/site: 
      # 1. Make sure that you use while-loops sparingly. 
      #    Usually a for-loop is better.
      #
      # 2. Review your while statements and make sure that 
      #    the boolean test will become False at some point.
      #
      # 3. When in doubt, print out your test variable at the 
      #    top and bottom of the while-loop to see what 
      #    it's doing.