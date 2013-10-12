#!/usr/bin/python
import sys


# keyword cipher
#
# A keyword cipher is a form of monoalphabetic substitution. 
# A keyword is used as the key, and it determines the letter matchings of the cipher 
# alphabet to the plain alphabet. Repeats of letters in the word are removed, then 
# the cipher alphabet is generated with the keyword matching to A,B,C etc. until the 
# keyword is used up, whereupon the rest of the ciphertext letters are used in 
# alphabetical order, excluding those already used in the key Worked Example.
#
# Plaintext:   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# Encrypted:   K R Y P T O S A B C D E F G H I J L M N Q U V W X Z
#
# With KRYPTOS as the keyword, all As become Ks, all Bs become Rs and so on. 
# Encrypting the message "knowledge is power" using the keyword "kryptos":
#
# Plaintext:   K N O W L E D G E I S P O W E R
# Encoded:     D G H V E T P S T B M I H V T L
#
# Only one alphabet is used here, so the cipher is monoalphabetic.
#
# The best ways to attack a keyword cipher without knowing the keyword are 
# through known-plaintext attack, frequency analysis and discovery of the 
# keyword (often a cryptanalist will combine all three techniques). 
# Keyword discovery allows immediate decryption since the table can be made immediately.


print "keyword.py a keyword cipher program"


####################
# TABLES
##################
ltr_to_numbr={'A':0,  'B':1,  'C':2,  'D':3,  'E':4,
              'F':5,  'G':6,  'H':7,  'I':8,  'J':9,
              'K':10, 'L':11, 'M':12, 'N':13, 'O':14,
              'P':15, 'Q':16, 'R':17, 'S':18, 'T':19,
              'U':20, 'V':21, 'W':22, 'X':23, 'Y':24,
              'Z':25}


###################
# Routine to lookup a letter based upon a number
###################
def numbr_to_ltr(n): # returns the letter corresponding to the number
	result = '.'	# retuns '.' if letter is not found.

	for ltr,nmbr in ltr_to_numbr.iteritems():
		# print the ltter and the number
		# print ltr, nmbr

		if nmbr==n:
			result=ltr
			break

	return result


###################
# Routine to lookup a letter based upon a number (Using the encoded table)
###################
def numbr_to_ltr_enc(n): # returns the letter corresponding to the number
	result = '.'	# retuns '.' if letter is not found.

	for ltr,nmbr in ltr_to_numbr_enc.iteritems():
		# print the ltter and the number
		# print ltr, nmbr

		if nmbr==n:
			result=ltr
			break

	return result





# four types of letter frequencies based upon type of text.
# ETAONISRHLDCUPFMWYBGVKQXJZ 
# ETNRIOASDHLCFPUMYGWVBXKQJZ 
# ETAOINSRHLDCUMFWGYPBVKXJQZ 
# ETOANIRSHDLUCMPFYWGBVKJXZQ

# vowels
#  EAOI
# constonants
#  TNSRH/TNRSH
# mixed
#  ETAOIN
#
# The most rare 
#  ZQX
#
# The most common digraphs
#
# TH ER ON AN
#
# The most common repeats
# 
# SS EE TT FF
#
# The most common Trigraph
# THE
#
# here is a link to an online frequency analysis program
# http://www.asecuritysite.com/security/Coding/freq

###################
# Routine to Build a letter frequency table.
###################
def letter_freq_table(msg):
	freq={}
	# for each letter in the message, print the letter and the number.
	for ltr in msg:
		freq[ltr]=0

	for ltr in msg:
		freq[ltr]=freq[ltr]+1
	return freq


###################
# Build an encrypted dictionary
# this routine takes a normal dictionary and a keyword as input.
# Using the input, it creates an encoded dictionary.
###################
ltr_to_numbr_enc={}
def build_letter_to_number_encoded_table(keyword):

	# First we add the letters of the keyword to the encoded dictionary
	i=0
	for ltr in keyword:
		ltr_to_numbr_enc[ltr]=i
		i=i+1

	# Second we go through the entire alphabet in order and put them in the dictionary
	# with the exception of letters already added from the keyword.
	for ltr,numbr in iter(sorted(ltr_to_numbr.items())):
#		print ltr
		if keyword.find((ltr))==-1:
			ltr_to_numbr_enc[ltr]=i
			i=i+1


keyword="KRYPTOS"
build_letter_to_number_encoded_table(keyword)

#print ltr_to_numbr_enc
print "dump the encrypted letter to number dictionary"
for ltr,numbr in iter(sorted(ltr_to_numbr_enc.items())):
	# print the letter and the count
	print ltr, numbr

print "**********************************"


# count        0 1 2 3 4 5 6 7 8 9 a b c d e f 0 1 2 3 4 5 6 7 8 9
# Plaintext:   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# Encrypted:   K R Y P T O S A B C D E F G H I J L M N Q U V W X Z
#
# Plaintext:   K N O W L E D G E I S P O W E R
# Encoded:     D G H V E T P S T B M I H V T L
#

# encrypt this message and check result
#"knowledge is power
msg="KNOWLEDGEISPOWER"
# for each letter in the message, print the letter and the number.
print "the encrypted message"
for ltr in msg:
	x = "{0:3}  {1:2d} {2:3}".format(ltr, ltr_to_numbr[ltr], numbr_to_ltr_enc(ltr_to_numbr[ltr]))
	print x

print "**********************************"

msg="THISISATESTZ"
print "freq analysis of ",msg
freq = letter_freq_table(msg)
#for ltr,nmbr in freq.iteritems():
for ltr,nmbr in iter(sorted(freq.items())):
	# print the letter and the count
	print ltr, nmbr


print "**********************************"


sys.exit()

