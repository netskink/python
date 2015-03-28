#!/usr/bin/python

# quiz 9


# What would the following Python code print out?
#stuff = dict()
#print stuff['candy']


# What would the following Python code print out?
stuff = dict()
# If the get can't find the key,
# it returns the second parameter as the default.
print stuff.get('candy',-1)


