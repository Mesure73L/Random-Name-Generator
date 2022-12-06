# WARNING: The program will stop running quickly if the list is too long!

from time import sleep
import words
import random
import os

usedNames = []

with open('usednames.txt', 'r') as filehandle:
    for line in filehandle:
        # Remove linebreak which is the last character of the string
        curr_place = line[:-1]
        # Add item to the list
        usedNames.append(curr_place)

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)

def makeRandom(adjective, noun):
  if f"{adjective}{noun}" in usedNames:
    makeRandom(random.choice(words.adjectives), random.choice(words.nouns))
  else:
    usedNames.append(f"{adjective}{noun}")
    with open('usednames.txt', 'w') as filehandle:
      for i in usedNames:
        filehandle.write(f"{i}\n")
    clearConsole()
    print(f"{usedNames[-1]}")

makeRandom(random.choice(words.adjectives), random.choice(words.nouns))

loop = True

while loop == True:
  cmd = input('> ')
  if cmd.startswith('/'):
    clearConsole()
    if cmd == "/reset":
      with open('usednames.txt', 'w') as filehandle:
        filehandle.write('')
      usedNames = []
      print("Reset the list.")
    elif cmd == "/help":
      print("Commands:\n/reset - Resets the list\n/help - Shows this list\n/quit - Closes the program")
    elif cmd == "/quit":
      print("Exiting the program.")
      loop = False
    else:
      print("Unknown command.")
  else:
    makeRandom(random.choice(words.adjectives), random.choice(words.nouns))