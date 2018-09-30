#!/usr/bin/python

# if/else/elsif
age = 18

if age >= 18:
    print "is an adult"
elif age >= 12:
    print "young adult"
elif age >= 3:
    print "child"
else:
    print "is not an adult"


# ternary
if age >= 21:
    old_enough = True
else:
    old_enough = False

old_enough = True if age >= 21 else False

#while
while age < 50:
    print "Not old enough. Current age is " + str(age)
    age += 1 
