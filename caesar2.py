#!/usr/bin/python

import sys
import os.path

# Implementation notes.
# all routines and variables use snake_case.  To distinguish functions from 
# variables, all functions start with a verb or only contain a verb.

# caesar_cipher
# This is a rewrite of the caesar cipher code to use python3
# It also allows spaces and punctiuation in text.
# And uses files for input.

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

# This code is particulary efficient. It does not the modulo trick. Instead is looks up
# characters letter by letter.

## Globals ##########################################

thekey={}
crypt_text=list([])

ltr_to_numbr={
              'a':0,  'b':1,  'c':2,  'd':3,  'e':4,
              'f':5,  'g':6,  'h':7,  'i':8,  'j':9,
              'k':10, 'l':11, 'm':12, 'n':13, 'o':14,
              'p':15, 'q':16, 'r':17, 's':18, 't':19,
              'u':20, 'v':21, 'w':22, 'x':23, 'y':24,
              'z':25,
              'A':100, 'B':101, 'C':102, 'D':103, 'E':104,
              'F':105, 'G':106, 'H':107, 'I':108, 'J':109,
              'K':110, 'L':111, 'M':112, 'N':113, 'O':114,
              'P':115, 'Q':116, 'R':117, 'S':118, 'T':119,
              'U':120, 'V':121, 'W':122, 'X':123, 'Y':124,
              'Z':125}

### routines #######################################

def cvrt_numbr_to_ltr(n): # returns the letter corresponding to the number
	result = '.'	# retuns '.' if letter is not found.
	is_uppercase=False

	for ltr,nmbr in ltr_to_numbr.items():
		# print the ltter and the number
		# print ltr, nmbr

		if nmbr==n:
			result=ltr
			break

	return result

def encode(x,n):  # given a number(x) corresponding to a letter and
# a number(n) corresponding to the shift specification
# return the encoded letter specification.
	# if letter is uppercase, convert it lowercase to lookup
	# flag result by adding 100.

	if (x>=100):
		x= x - 100
		result = (x+n) % 26 
		result=result + 100
	else:
		result = (x+n) % 26 

	return result

def do_stuff():
	print("do stuff here")

def read_keyfile(thefile):
	for i in range(26):
		thekey[i]=thefile.read(1)

def read_cryptfile(thefile):
	for line in thefile:
		crypt_text.append(line)

def dump_keyfile():
	for i in range(26):
		print("thekey[{:d}] = {:s}".format(i,thekey[i]))

def dump_crypt_text():
	for i in range(len(crypt_text)):
		print("crypt_text[{:d}] = {:s}".format(i,crypt_text[i]))

def determine_shift(thekey):
	for i in range(26):
		if (thekey[i]=="a" ):
#			print("shift is {:d}".format(i))
			return i

def encrypt_line(thekey,clear_text):
	result =''
	shift_spec = determine_shift(thekey)
	for ltr in clear_text:
		if (ltr == '\n'):
			print()
			return
		#
		# TODO: This bit of if statements needs to be done smarter.
		#
		if (ltr == ' '):
			print(' ',end='')
			continue
		if (ltr == '.'):
			print('.',end='')
			continue
		if (ltr == '?'):
			print('?',end='')
			continue
		enc_ltr = encode(ltr_to_numbr[ltr],shift_spec)
		result = cvrt_numbr_to_ltr(enc_ltr)
		print('%s' % (result),end="")


#print "key: %s , value: %s" % (key, mydictionary[key])
#'%sResponse' % action: {'%sResult' % action: response}
# this print('%(language)s has %(number)03d quote types.' % {'language': "Python", "number": 2})
# results Python has 002 quote types.

#### Main #############################################

if len(sys.argv) != 3:
	print('Usage {:s}, <keyfile> <crypto_file>'.format(sys.argv[0]))
	sys.exit();

keyfile = str(sys.argv[1]);
crypt_file = str(sys.argv[2]);

# check to see if both files exist
if ( not os.path.isfile(keyfile) ):
	print('keyfile: {:s}, does not exist.'.format(keyfile))
	sys.exit();

if ( not os.path.isfile(crypt_file) ):
	print('encrypted file: {:s}, does not exist.'.format(crypt_file))
	sys.exit();


try:
    myfile = open(keyfile, "r") # or "a+", whatever you need
except ValueError:
	print('keyfile: {:s}, could not be opened for reading.'.format(keyfile))
	sys.exit()
except IOError:
	print('keyfile: {:s}, could not be opened for reading.'.format(keyfile))
	sys.exit()
else:
	read_keyfile(myfile)
	myfile.close()


try:
    myfile = open(crypt_file, "r") # or "a+", whatever you need
except ValueError:
	print('encrypted file: {:s}, could not be opened for reading.'.format(crypt_file))
	sys.exit()
except IOError:
	print('encrypted file: {:s}, could not be opened for reading.'.format(crypt_file))
	sys.exit()
else: 
	read_cryptfile(myfile)
	myfile.close()



for i in range(len(crypt_text)):
	encrypt_line(thekey,crypt_text[i])

#print('Normal exit')
sys.exit()


