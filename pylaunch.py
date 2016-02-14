import launchpad
from pygame import time
import random

print("Pylaunch v0.1b, made by sesshomariu")
lp = launchpad.Launchpad()
lp.Open()

red = 0
green = 0

def colcho(arg):
	if arg is "r":
		red = 3
		green = 0
	elif arg is "y":
		red = 3
		green = 3
	elif arg is "g":
		red = 0
		green = 3
	else:
		print("ERROR: Couldn't choose color.")

while 1:
	command = raw_input("pylaunch>")
	if command is "exit":
		break

	elif command[:3] is "raw":
		if len(command) == 9:
			arg1 = command[4]
			arg2 = command[6:9]
			colcho(arg1)
			
		else:
	else:
		print("Command not found. Type 'help' for a list of valid commands.\n")
