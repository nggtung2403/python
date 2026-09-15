import mymodule
from mymodule import generate_full_name as fullname,sum_two_nums as total,gravity as g ,person as p
print(fullname("Tung","Nguyen"))
print(total(1,9))

mass = 100
weight = mass * g
print(weight)

print(p["firstname"])

""" import sys
print("Welcome {}.Enjoy {} challenge!".format(sys.argv[1],sys.argv[2])) """

from statistics import *
ages = [20,20,4,2,5,43,5,42]
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))

import math
print(math.pi)
print(math.sqrt(2))
print(pow(2,3))
print(math.floor(9.81))
print(math.ceil(9.81))
print(math.log10(100))

from math import pi
print(pi)

import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

from random import random,randint
print(random())
print(randint(5,20))