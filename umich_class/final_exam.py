#!/sw/bin/python2.7

x = 12
if x <= 10:
   if x > 4:
      print "One"
   else:
      print "Two"
else:
   if x >= 11:
      print "Three"
   else:
      print "Four"


str = "hello there bob"
print str[4]

foo='with three words'
print(foo.split())


x=9
if x < 2 :
	print('Below 2')
elif x < 20 :
	print('Below 20')
elif x < 10 : 
	print('Below 10')
else :
	print('Something else')


lst = []
lst.append(4)
lst.append(10)
lst.append(21)
lst.append(6)
print lst[2]


sta = "abc"
stb = "123"
stc = sta + stb
print stc


fline = "blah blah"

if len(fline) > 1 :
    print "More than one"
    if fline[0] == "h" : 
        print "Has an h"
print "All done"



stx = "hello there bob how are you"
wds = stx.split()
print wds[2]



x = -1
for value in [3, 41, 12, 9, 74, 15] :
    if value < x :
        x = value 
print x


