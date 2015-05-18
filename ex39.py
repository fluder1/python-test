# Practice example sampled from learnpythonthehardway.org/book/ex35.html
import hashmap 

states = hashmap.new() 
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Fran')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')

hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

print '-' * 10
print 'NY State Has: %s' % hashmap.get(cities,'NY')
print 'OR State Has: %s' % hashmap.get(cities,'OR')

print '-' * 10
print 'Michigan abbr: %s' % hashmap.get(states, 'Michigan')
print 'Florida\'s abbr: %s' % hashmap.get(states, 'Florida')

print '-' * 10
print 'Mich has: %s' % hashmap.get(cities, hashmap.get(states, 'Michigan'))
print 'Florida has: %s' % hashmap.get(cities, hashmap.get(states, 'Florida'))

print '-' * 10
hashmap.list(states)

print '-' * 10
hashmap.list(cities)

print '-' * 10
newState = 'Texas'
state = hashmap.get(states, newState)

if not state:
	print "Sorry, no %s." % newState

city = hashmap.get(cities, 'TX', 'Does Not Exist')
print "The city for the state 'TX' is %s" % city
