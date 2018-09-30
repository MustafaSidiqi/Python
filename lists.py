#!/usr/bin/python

# liitializ
my_list = [1, 2, 3, "?", True, 4.95]

# add item
my_list.append(69)
print my_list

# access item
print my_list[4]
print my_list[0:3]

# change item
my_list[3] = "$"
print my_list[3]

#remove item by index
del my_list[2]

# iterate
for item in my_list:
    print item
