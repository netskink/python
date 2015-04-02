__author__ = 'davis'

# quiz 10 selected problems


# Question 2
# Which of the following methods work both in Python lists and Python tuples?
# append()
# index()
# reverse()
# pop()
# sort()

a_tuple = tuple(range(1000))
a_list = list(range(1000))

print a_tuple.__sizeof__() # 8024
print a_list.__sizeof__() # 9088

# a_list has all the above methods
# a_count only has count and index methods.


# Question 3
# What will end up in the variable y after this code is executed?
x , y = 3, 4

print(y) # 4


# Question 4
# In the following Python code, what will end up in the variable y?
x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()

print(y) # list of tuples [('jan', 100), ('chuck', 1), ('fred', 42)]

# Question 5
# Which of the following tuples is greater than x in the following Python sequence?

# y = (0, 1000, 2000) # not this one
# y = (4, 100, 200) # not this one
# y = (5, 0, 300) # not this one
y = (6, 0, 0) # this one

x = (5, 1, 3)
if y > x :
    print "this one"
else:
    print "not this one"


# Question 5
# What does the following Python code accomplish, assuming the c is a non-empty dictionary?
# c is a dictionary
c = {'sape': 4139, 'guido': 4127, 'jack': 4098}
tmp = list()
for k, v in c.items() :
    tmp.append( (v, k) )

# Question 6
# If the variable data is a Python list, how do we sort it in reverse order?
a_list = [66.25, 333, 333, 1, 1234.5]
print a_list
# not this one a_list = sortrev(a_list)
# not this one a_list = a_list.sort(-1)
# this one. it reverse sorts it.
a_list.sort(reverse=True)
# not this one. It simply reverses it
a_list.reverse()
print a_list

# Question 7
# Using the following tuple, how would you print 'Wed'?
days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
#print days{2}
#print days.get(1,-1)
#print days[1]
#print days(2)
print days[2]

# Question 8
# In the following Python loop, why are there two iteration variables (k and v)?
c = {'a':10, 'b':1, 'c':22}
for k, v in c.items() :
    print k,y







