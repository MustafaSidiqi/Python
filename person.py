#!/usr/bin/python

# definition / self / properties / method

class Person:

    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print "My name is %s" % self.name

    def print_age(self):
        print "My name is %d" % self.age

    def have_birthday():
        age += 1
