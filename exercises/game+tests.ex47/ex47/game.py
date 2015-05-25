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

