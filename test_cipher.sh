#!/bin/sh

# this is a method to test the caeser cipher
# since it does not have a command option to encode or decode
# you need to use a reversed key between operations.
# that is why the keyfile varies between encrupt and decrypt.
#
# Yes, I know I could have written a shift specifier instead of
# a keyfile like +1 or -1. I was just practicing code.
./caesar2.py keyfile.txt encrypted_file.txt > foo.txt
./caesar2.py keyfile2.txt foo.txt

