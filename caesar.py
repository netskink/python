#!/usr/bin/python


# caesar_cipher
#
# The transformation can be represented by aligning two alphabets; the cipher alphabet is the plain alphabet 
# rotated left or right by some number of positions. For instance, here is a Caesar cipher using a left 
# rotation of three places, equivalent to a right shift of 23 (the shift parameter is used as the key):

# Plain:    ABCDEFGHIJKLMNOPQRSTUVWXYZ
# Cipher:   XYZABCDEFGHIJKLMNOPQRSTUVW

# When encrypting, a person looks up each letter of the message in the "plain" line and writes down the 
# corresponding letter in the "cipher" line. Deciphering is done in reverse, with a right shift of 3.

# Ciphertext: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD
# Plaintext:  the quick brown fox jumps over the lazy dog

# The encryption can also be represented using modular arithmetic by first transforming the letters into 
# numbers, according to the scheme, A = 0, B = 1,..., Z = 25.[1] Encryption of a letter  by a shift n 
# can be described mathematically as,[2]

# En(x)=(x+n) mod 26

# Decryption is performed similarly,
# Dn(x)=(x-n) mod 26

# (There are different definitions for the modulo operation. In the above, the result is in the 
# range 0...25. I.e., if x+n or x-n are not in the range 0...25, we have to subtract or add 26.)
# The replacement remains the same throughout the message, so the cipher is classed as a type of 
# monoalphabetic substitution, as opposed to polyalphabetic substitution.


print "Caesar.py a caesar cipher program"

ltr_to_numbr={'A':0,  'B':1,  'C':2,  'D':3,  'E':4,
              'F':5,  'G':6,  'H':7,  'I':8,  'J':9,
              'K':10, 'L':11, 'M':12, 'N':13, 'O':14,
              'P':15, 'Q':16, 'R':17, 'S':18, 'T':19,
              'U':20, 'V':21, 'W':22, 'X':23, 'Y':24,
              'Z':25}


print ltr_to_numbr['A']
print ltr_to_numbr['Z']

def numbr_to_ltr(n): # returns the letter corresponding to the number
	result = '.'	# retuns '.' if letter is not found.

	for ltr,nmbr in ltr_to_numbr.iteritems():
		# print the ltter and the number
		# print ltr, nmbr

		if nmbr==n:
			result=ltr
			break

	return result

def encode(x,n):  # given a number(x) corresponding to a letter and
# a number(n) corresponding to the shift specification
# return the encoded letter specification.
	result = (x+n) % 26 
	return result

msg="THISISATESTZ"
SHIFT_SPEC=1
# for each letter in the message, print the letter and the number.
for ltr in msg:
	print ltr , ltr_to_numbr[ltr], numbr_to_ltr(encode(ltr_to_numbr[ltr],SHIFT_SPEC))

print "**********************************"

# Ciphertext: QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD
# Plaintext:  the quick brown fox jumps over the lazy dog

msg="THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
SHIFT_SPEC=-3
# for each letter in the message, print the letter and the number.
for ltr in msg:
	print ltr , ltr_to_numbr[ltr], numbr_to_ltr(encode(ltr_to_numbr[ltr],SHIFT_SPEC))


print "**********************************"
msg="QEBNRFZHYOLTKCLUGRJMPLSBOQEBIXWVALD"
SHIFT_SPEC=+3
# for each letter in the message, print the letter and the number.
for ltr in msg:
	print ltr , ltr_to_numbr[ltr], numbr_to_ltr(encode(ltr_to_numbr[ltr],SHIFT_SPEC))


# Building a letter frequency table.


print "**********************************"
msg="THISISATESTZ"
freq={}
# for each letter in the message, print the letter and the number.
for ltr in msg:
	freq[ltr]=0

for ltr in msg:
	freq[ltr]=freq[ltr]+1

for ltr,nmbr in freq.iteritems():
	# print the letter and the count
	print ltr, nmbr


print "**********************************"


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
#  ETAON

