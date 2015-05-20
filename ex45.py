# Practice from learnpythonthehardway.org/book/ex45.html
import Rooms

print "You see two doors"
print "1) Take left door"
print "2) Take right door"

action = raw_input("> ")
action = int(action)

if action == 1:
	choice = Rooms.LeftRoom()
	if choice.enter():
		print "There's nothing here"
		exit(0)
elif action == 2:
	choice = Rooms.RightRoom()
	if choice.enter():
		print "You find three VHS tapes of Speed 2"
		exit(0)
else:
	print "I guess you don't want to play"
	exit(0)
