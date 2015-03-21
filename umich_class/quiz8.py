#!/usr/bin/python

# this fails
#fruit = 'Banana'
#fruit[0]='b'
#print fruit

# create a list and get length
L = [1,2,3,4,5]
print L
print len(L)
fifth = L[4]
print fifth

# create another list
L = [i*2 for i in range(0,5)]
print L

# quiz question
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print len(c)

# Which of the following slicing operations will produce the list [12, 3]?
t = [9, 41, 12, 3, 74, 15]
print t[2:4]

# append to a list
L = [1,2,3,4,5]
print L
L.append(6)
print L

#What will the following Python code print out?
friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print friends[0]




