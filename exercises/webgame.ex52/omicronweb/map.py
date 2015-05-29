# Practice based from example 47 from learnpythonthehardway.org/book/ex47.html
class Room(object):
	
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.paths = {}

	def go(self, direction):
		return self.paths.get(direction, None)

	def add_paths(self, paths):
		self.paths.update(paths)


central_corridor = Room("Central Corridor",
"""
The Omicronians of Omicron Persei 8 have invaded your ship. You are the last remaining member and you need to retrieve the doomsday device from the Weapons Armory, attached it to the bridge and blow up the ship after getting on an escape pod.
""")

laser_weapon_armory = Room("Laser Weapon Armory",
"""
You dive roll into the armory and scan the room. You see and walk over to the doomsday vault and pick up a locked box. There's a keypad lock on the box and you need the code. If you mistype the code 10 times the lock closes forever. The code is 3 digits.
""")

the_bridge = Room("The Bridge", 
"""

