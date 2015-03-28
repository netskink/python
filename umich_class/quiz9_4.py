#!/usr/bin/python



# 9.4 Write a program to read through the mbox-short.txt and figure out who has
# the sent the greatest number of mail messages. The program looks for 'From '
# lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to
# a count of the number of times they appear in the file. After the dictionary is
# produced, the program reads through the dictionary using a maximum loop to find
# the most prolific committer.


#fname = raw_input("Enter file name: ")
fname = "mbox-short.txt"
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
senders = dict()

# Build the hash map
for line in fh:
	line = line.rstrip()
	words = line.split()
	if len(words) > 1:
		if words[0] == "From:":
			key = words[1]
			senders[key] = senders.get(key,0) + 1

# Find the max in the hash map
max_sender = ""
max_sent = 0
# Is senders a dictionary/hash map?
#print type(senders)
# This works in my python
#for sender,count in senders.iteritems():
# This works in the autograder python
for sender in senders.keys():
# This is required for autograder python
	count = senders[sender]
	if count > max_sent:
		max_sent = count
		max_sender = sender
	 

print max_sender, " ", max_sent




