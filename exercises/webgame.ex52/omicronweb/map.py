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
The container cracks open and gas starts leaking from it. You burst towards the Bridge with the doomsday device.
""")

escape_pod("Escape Pod",
"""
You inch slowly towards the door, open it and place the doomsday device at your feet. You rush through the ship heading towards the chamber with the escape pods. You see five pods, all with slight damage to them, which do you choose?
""")

the_end_winner = Room("The End",
"""
You jump into pod #2 and hit the eject button. The pod slowly drifts away from the ship deeper and deeper into space. You look back just in time the see the ship explode behind you. 
""")

the_end_loser = Room("The End",
"""
You jump into a random pod and hit eject. However the pod doesn't move. A familar voice then repeats 'I'm afraid I cannot let you do that, Dave' before sealing the pod door. 
"""
)

escape_pod.add_paths({
	'2': the_end_winner,
	'*': the_end_loser
})

generic_death = Room("death", "He's dead Jim")

the_bridge.add_paths({





