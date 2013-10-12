#!/usr/bin/python

# http://gmarkhardy.com/docs/CarolinaCon9Crypto.txt

# four types of letter frequencies based upon type of text.
# ETAONISRHLDCUPFMWYBGVKQXJZ 
# ETNRIOASDHLCFPUMYGWVBXKQJZ 
# ETAOINSRHLDCUMFWGYPBVKXJQZ 
# ETOANIRSHDLUCMPFYWGBVKJXZQ

# Vigenere cipher


a1=['R','B','T','Z','T','H','S','E','B','D','T','T','N','W','S','L','G','Z','Z','I'];
a2=['F','J','I','G','E','P','J','S','C','R','U','W','Y','Q','X','C','M','O','H','B'];
a3=['G','D','S','F','U','A','X','T','W','R','N','Z','B','I','W','Q','N','H','L','V'];
a4=['Z','D','C','Y','T','T','M','A','I','O','U','Q','W','D','D','E','P','K','W','D'];
a5=['V','U','P','Z','S','V','K','X','D','G','E','X','Z','X','F','R','Q','F','K','J'];
a6=['L','X','L','N','I','D','M','Q','K','V','B','F','N','K','J','V','R','U','D','V'];
a7=['M','B','L','C','F','C','N','W','T','W','O','K','F','Q','P','M','V','F','T','D'];
a8=['V','H','S','D','B','I','O','R','J','F','V','T','U','W','S','F','R','B','V','J'];
a9=['I','G','U','V','L','Q','L','Q','Y','Y','W','Y','I','M','X','K','I','O','Y','X'];
aa=['H','I','D','O','K','I','K','A','P','D','P','T','E','A','Q','D','A','W','R','L'];
ab=['X','H','R','G','M','X','C','R','K','W','F','U','W','X','P','F','Q','L','Y','G'];
ac=['G','L','K','H','O','E','Q','A','R','V','S','C','O','V','K','M','J','K','G','G'];
ad=['X','K','J','P','J','L','Y','U','I','L','S','B','T','Z','C','Y','Z','H','N','V'];
af=['B','P','X','X','F','U','B','O','R','R','P','T','T','Y','D','K','V','J','D','Z'];

cipher_len=len(a1)
print  ("the length of a1 is",len(a1));
print  ("a1[0] is",a1[0]);

ans1="gmark";
print ("1: Crypto Creator(5)      \t",ans1,len(ans1)); 
ans2="MDNA";
print ("2: Ancestral Tracing(4)   \t",ans2,len(ans2));
ans3="terrier";
print ("3: Eire Canines(7)        \t",ans3,len(ans3));
ans4="earnest";
print ("4: Importance of being(7) \t",ans4,len(ans4));
ans5="";
print ("5: Old and new(10)        \t",ans5,len(ans5));
ans6="";
print ("6: IRA Financiers(10)        \t",ans6,len(ans6));
ans7="Guinness";
print ("7: Since 1759(8)        \t",ans7,len(ans7));
ans8="Guardiola";
print ("8: Taught by nuns(9)        \t",ans8,len(ans8));
ans9="Liquid Fence";
print ("9: Snake repellant(12)        \t",ans9,len(ans9));
ansa="persecution";
ansa="opportunity";
ansa="Tolerance";
ansa="Reunification";
ansa="oppression";
ansa="employment";
print ("a: Emigration motivation(12)        \t",ansa,len(ansa));
ansb="cornedbeefandcabbage";
print ("b: Traditional repast(20)        \t",ansb,len(ansb));
ansc="";
print ("c: Best done from below(19)        \t",ansc,len(ansc));
ansd="";
print ("d: 18 episode creator(10)        \t",ansd,len(ansd));








ABC =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
key1=['G','M','A','R','K','B','C','D','E','F','H','I','J','L','N','O','P','Q','S','T','U','V','W','X','Y','Z'];
a1  =['R','B','T','Z','T','H','S','E','B','D','T','T','N','W','S','L','G','Z','Z','I'];
ans1=['D','F','T','Z','T','K','S','I','F','H','T','T','O','W','S','N','A','Z','Z','L'];


print ("length of key1",len(key1));
print ("length of ABC",len(ABC));


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


letters={'A':0, 'B':1, 'C':2, 'D':3, 'E':4,
         'F':5, 'G':6, 'H':7, 'I':8, 'J':9,
         'K':10, 'L':11, 'M':12, 'N':13, 'O':14,
         'P':15, 'Q':16, 'R':17, 'S':18, 'T':19,
         'U':20, 'V':21, 'W':22, 'X':23, 'Y':24,
         'Z':25}




