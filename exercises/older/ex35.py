# Practice example sampled from learnpythonthehardway.org/book/ex35.html
from sys import exit

def gold_room():
	print "This room is full of gold, how much did you take?"
	
	choice = raw_input("> ")
	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("Man, learn to type a number")

	if how_much < 50:
		print "Nice, you're not greedy"
		exit(0)
	else: 
		dead("You greedy bastard!")


def bear_room():
	print "There is a bear in here"
	print "The bear has a bunch of honey"
	print "The bear is in front of the door"
	print "How are you going to move the bear?"
	bear_moved = False

	while True:
		choice = raw_input("> ")
	
		if choice == "take honey":
			dead("The bears slaps your face off")
		elif choice == "taunt bear" and not bear_moved:
			print "Bear moves."
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("Bear chews your leg off")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print "I have not idea what that means"


def cthulhu_room():
	print "Here you see if the great evil Cthulhu."
	print "He, it, whatever stares at you and you go insane"
	print "Do you flee or eat your head?"
	
	choice = raw_input("> ")

	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("well that was tasty")
	else:
		cthulhu_room()


def dead(why):
	print why, "Good job!"
	exit(0)

def start():
	print "You are in a dark room"
	print "There is a door to your right and left"
	print "Which do you take?"

	choice = raw_input("> ")

	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead("You stumble arounf the room until you starve")


start()
