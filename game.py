import time
import sys
import os

#variables

inventory = []
weapon = False
key = False


#Colors
class colors:
   COLLOR = '\033[91m'
   WHITE = '\033[37m'

#aesthetic functions
def rbot(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.10)

def lore(text):
   for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.03)

def cs():
    os.system('cls')


#story/scens/locations
   
def room1():
    rbot(colors.COLLOR+"11:23\nGoodmorning sir\n"
        "life support: operational\n"
        "Oxygen: operational\n"
        "Power: operational\n"
        "Status: on course\n"
        "days left: 13\n\n"+colors.WHITE)

    x = input("Wake up? Y/N\n\n")
    if x == "y":
        lore("you wake up and look around.\n"
            "you realize that you're in a small room, with nothing personal.\n"
            "when looking out the window, you start to remember where you are.\n\n")
    else: 
        lore("You stay asleep\n\n")
        day13()
    
def day13():
   rbot("11:23\nGoodmorning sir\n"
        "life support: operational\n"
        "Oxygen: operational\n"
        "Power: operational\n"
        "Status: on course\n" 
        "Hours left: 3\n\n")
   
   lore('you wake up for the final 3 hours of your journey\n'
        'your fellow crewmates are praying to gods you dont believe in\n'
        'you are just focussing on the final things that need to be done before your arrival\n\n')
   
room1()
