#!/usr/bin/python


# 8.4 Open the file romeo.txt and read it line by line. For each line, split the
# line into a list of words using the split() function. The program should build
# a list of words. For each word on each line check to see if the word is already
# in the list and if not append it to the list. When the program completes, sort
# and print the resulting words in alphabetical order.  You can download the
# sample data at http://www.pythonlearn.com/code/romeo.txt


fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
	line = line.rstrip()
	for word in line.split():
		try:
			# if its not found, it will 
			# throw an exception. The rc
			# is the index in the list for
			# the item it found, but we don't
			# need it.
			i = lst.index(word)
		except ValueError:
			lst.append(word)

print sorted(lst)

