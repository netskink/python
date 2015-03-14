#!/usr/bin/python

print "hello"

xfile = open('foo.txt')
for line in xfile:
	print line


fhand = open('foo.txt')
x = 0
for line in fhand:
       x = x + 1
print x
