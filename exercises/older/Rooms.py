# Practice from learnpythonthehardway.org/book/ex45.html
class Room(object):
	def enter(self):
		print "The room is dark"
		print "1) Stumble around"
		print "2) Feel wall"
		
		action = raw_input("> ")
		action = int(action)
		
		if action == 1:
			print "You fall down"
			return False
		elif action == 2:
			print "You find a light switch"
			return True
		else:
			print "I doubt that would work"
			self.enter()

class RightRoom(Room):
	pass

class LeftRoom(Room):
	pass
