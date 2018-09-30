#!/usr/bin/python

# initialize
my_dict = {}

# add item
my_dict["name"] = "Mustafa"
my_dict["state"] = "Maryland"
my_dict["age"] = 23
my_dict["test"] = "testing"

print my_dict

# access item
print my_dict["name"]

# change item
my_dict["name"] = "Mustafa Sidiqi"
print my_dict

# remove item by index
del my_dict["test"]
print my_dict

# iterate
for k, v in my_dict.iteritems():
    print k, "=>", v
