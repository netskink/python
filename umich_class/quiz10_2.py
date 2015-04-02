__author__ = 'davis'

# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each
# of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a
# second time using a colon.


# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1
# Note that the autograder does not have support for the sorted() function.


# name = raw_input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# handle = open(name)


#fname = raw_input("Enter file name: ")
fname = "mbox-short.txt"
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
time_sent = dict()

# Build the hash map of messages by time
for line in fh:
    line = line.rstrip()
    words = line.split()
    if len(words) == 7:     # From, email address, day of week, month, day, time, year
        if words[0] == "From":
            # print words
            key = words[5]
            # key is something like this: 10:04:31 and 16:23:48
            # subset it again to get the hour like this: 10, 16
            key = key[:2]
            #print key
            time_sent[key] = time_sent.get(key,0) + 1

# The grader does not have the sorted() function for dictionaries.
# use this method to sort the keys and then print the key,value pairs
keylist = time_sent.keys();
keylist.sort()
for key in keylist:
    print key, time_sent[key]




