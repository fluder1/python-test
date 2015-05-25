# Practice based from example 48 from learnpythonthehardway.org/book/ex48.html
def scan(userString):
	userStringFormatted = []
	direction = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 					 'right', 'back')
	verb = ('go', 'stop', 'kill', 'eat')
	stop = ('the', 'in', 'of', 'from', 'at', 'it')
	noun = ('door', 'bear', 'princess', 'cabinet')
	userWordList = userString.lower().split()

	for eachWord in userWordList:	
		if eachWord in direction:
			userStringElement = 'direction', eachWord
		elif eachWord in verb:
			userStringElement = 'verb', eachWord
		elif eachWord in stop:
			userStringElement = 'stop', eachWord
		elif eachWord in noun:
			userStringElement = 'noun', eachWord
		else:
			if check_if_int(eachWord):
				userStringElement = 'number', int(eachWord)
			else:
				userStringElement = 'error', eachWord

		userStringFormatted.append(userStringElement)

	return userStringFormatted

def check_if_int(possibleInt):
	try:
		int(possibleInt)
		return True
	except ValueError:
		return False
