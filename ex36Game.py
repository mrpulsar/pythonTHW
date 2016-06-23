from sys import exit
import random

print "Welcome to the byte-sized adventure."
print "Please enter your name:"
name = raw_input(">> ")
new_line = "\n"
knife = False

def first_path():
  print "You have entered the Adventure World, %s." % name
  the_room()
  

def room_one():
  print "The safest decision for sure. As you begin to walk toward the tavern, a group of bandits jump out and murder you. You die, game over!"
  

def room_two_two():
    print "Nearby, a pack of wolves fights a bear over the rights to your body as dinner. You watch as the wolves jump on the bear and he rips them off. The fight goes on for hours, all the while you lose blood and feel snakes crawl along your body. Suddenly, the bear has seemed to gain the upper hand, but as he claws the last wolf, it charges and bites hard into the bears eyes, blinding it. The wolf dies and the bear stumbles around north of you, blind, trying to smell past the wolves blood for your scent. How the hell do we get out of this?"
  


def room_two(): # Falling off the cliff choice.
  print "You jump from the cliff like a schoolgirl on a pop star. The cliff proves to you\nthat gravity still dictates the laws of matter as your legs crush beneath you, \nabsorbing your fall and you hit your shoulder on a rock, displacing your arm."
  print "Pick your decision:"
  print "1. Scream for help."
  print "2. Scream harder for help."
  print "3. Pretend your legs are not broken."
  print "4. Cut your legs off, if you have a knife."
  
  decision = raw_input(">> ")
  
  if decision == "1":
    print "No one heard you, except for the pack of wolves nearby. They run to your aid and swiftly eat you. You die, game over!"
  elif decision == "2":
    room_two_two()
  elif decision == "3":
    print "You try to get up and the wolves laugh at you as if they are human, and then they eat you. You die, game over!"
  elif decision == "4":
    if knife == True:
      print "You cut your legs off and watch as wolves eat them. You manage to keep the wolves at bay with your knife but struggle to patch the wounds while doing so... But not quick enough as you lose all your blood. You die, game over!"
    else:
      print "You'd love to have a knife right now, wouldn't you? Well you don't, so you lay \nthere bruised and bleeding. You die, game over!"
  else:
    print "I don't think you made an actual choice.... let's try this again.\n\n"
    room_two()
  
def room_four():
  print "This is it, the path is clear, you have no broken legs, crushed organs or stab\nwounds. You notice that the sun has risen incredibly fast, already being about\none third of the way up further in the sky than before. It looks beautiful,\nand you have a smile on your face. In about ten minutes, you make it to the\nbuilding you saw and it becomes clear that it is indeed a Tavern. You take\nshelter, adventure some more, come back, drink, adventure some more, sell\nall sorts of odd loot the inn keeper never wants but yet buys anyways,\nmostly out of pity for you. It's clear you're an alcoholic, you die, game over!"

def room_three_one():
  print "For some reason, the abyss stares back at the bandits, leaving you looking at a puddle of blood left over from four to five corpses. You walk back to the original path and rummage among the bloody clothes for anything you can take."
  print "You've obtained a +1 knife!"
  knife = True
  print "Pick your decision:"
  print "1. To your north is a path leading to the Town's tavern"
  print "2. To your west is a cliff... it looks steep."
  print "3. To your east is a forest, so thick you can't see past the canopy."
  print "4. To your south is the abyss, it's where you came from."
  decision = raw_input()

  if decision == "1":  
    room_four()
  elif decision == "2":
    room_two()
  elif decision == "3":
    print "You get dizzy from going in circles too many times, good job man. You die, game over!"
  elif decision == "4":
    print "The abyss showed you mercy before, it decides not to this time. You die, game over!"
  else:
    print "I don't think you made an actual choice.... let's try this again.\n\n"
    room_three_one()

  

def room_three():
  print "This forest is very thick. You walk eastbown into the thickets and soon notice\nbandits behind you on the road, cursing about. They are clearly mad about\nsomething and then one yells, 'His name is %s'.\nThat is clearly creepy, as we have no awareness of where we are or even what time period we're in. To our north is... more forest, to our east is even more forest, to the south is the abyss, and we don't want to go back west." % name
  print "Pick your decision:"
  print "1. To your north you see the thickets become less dense and a small open area of grass is beautifully lit sunlight that has managed to penetrate the canopy of the forest. Go north to that area."
  print "2. To your east the forest gets thicker, and you start to see less places to plant your feet without having to climb the trees. Try and climb them and go east."
  print "3. To your south is the abyss... obviously still. We have not gone north yet."
  print "4. To your west is a buttload of angry bandits ready and willing to kill you and rip you apart piece by piece until every bit of value on your body is traded from one shady merchant to the next. Trust me, we do not want to go back west."
  
  decision = raw_input(">> ")
  
  if decision == "1":
    print "You go to the area and briefly take in the sunlight and beauty of the scenery, before the bandits catch a glimpse of you through the hollow thickets. They run into the thickets and murder you. You die, game over!"
  elif decision == "2":
    print "The forest gets thicker and thicker. So thick, oh so thick. You can't breathe yet you keep trying to merge through the trees. You die, game over!"
  elif decision == "3":
    room_three_one()
  elif decision == "4":
    print "What!? Why!? You die, game over! On the plus side, at least you got the Darwin Award."
  

def the_room():
  print "You walk along an unknown road as the sun rises in the east, in the distance \na building grows larger. It's clearly a tavern, what will you do?\n\n"
  print "Pick your decision:"
  print "1. To your north is a path leading to the Town's tavern"
  print "2. To your west is a cliff... it looks steep."
  print "3. To your east is a forest, so thick you can't see past the canopy."
  print "4. To your south is the abyss, it's where you came from."

  decision = raw_input(">> ")
  if decision == "1":
    print new_line
    room_one()
  elif decision == "2":
    print new_line
    
    room_two()
  elif decision == "3":
    print new_line
    room_three()
  elif decision == "4":
    print "The Abyss stares back at you. You die, game over!"
  else:
    print "Not sure I, the almighty god of knowing, understood that. Please try entering a single digit number instead."
    the_room()
  

first_path()

