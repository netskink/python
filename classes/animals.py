#!/usr/bin/env python3


# demo usage of :
# @property
# @staticmethod def foo(somevar):
# @classmethod def foo(cls, somvar):

import random

class Animal(object):

    def __init__(self, aname, sound):
        self.aname = aname
        self.sound = sound
    
    def make_sound(self):
        print("a {} {}s".format(self.aname, self.sound))

    @staticmethod
    def eat(food):
        # no access to self variables
        print("animal eats {}".format(food))


class Dog(Animal):

    # class variable
    # all dogs do these
    aname = "dog"
    sound = "bark" 

#    def __init__(self):
#        self.aname = Dog.aname  # Animal parent class will use instance variables
#        self.sound = Dog.sound
#        self.tricks = []  # Each dog will have its own tricks

    # alternate method of above
    def __init__(self):
        Animal.__init__(self, Dog.aname, Dog.sound)
        self.tricks = []  # Each dog will have its own tricks

    def wag_tail(self):
        print("a {} wags tail".format(self.aname))

    def add_trick(self, trick):
        self.tricks.append(trick)

    def do_random_trick(self):
        trick_index = random.randrange(0, len(self.tricks))
        print("Do {}".format(self.tricks[trick_index]))

    @classmethod
    def eat(cls, food):
        # no access to self variables
        print("{} eats {}".format(cls.aname, food))

def main():
    print("Class demo")

    animal = Animal("dog","bark")
    animal.make_sound()


    dog1 = Dog()
    dog1.make_sound()
    dog1.wag_tail()
    dog1.add_trick("come")
    dog1.add_trick("jump")
    dog1.add_trick("sit")
    dog1.add_trick("down")
    dog1.do_random_trick()
    Animal.eat("food")
    Dog.eat("canned dog food")





if '__main__' == __name__:
    main()



