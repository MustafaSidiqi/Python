#!/usr/bin/python

# definition
def my_func():
    # your code
    print "hello world"


# arguments/return
def add(num1, num2):
    return num1 + num2

# multiple return
def square(n1, n2):
    return n1**2, n2**2

# calling
my_func()

res = add(num2=2, num1=6)
print res

res1, res2 = square(2, 4)
print res1, res2
