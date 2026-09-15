def sum_numbers(nums):
    return sum(nums)

def higher_order_function(f,lst):
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers,[1,2,3,4,5])
print(result)

def square(nums):
    return nums * nums
def higher(f,a):
    sum = f(a)
    return sum
result = higher(square,6)
print(result)

def square(x):
    return x ** 2
def cube(x):
    return x ** 3
def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type):
    if type == "square":
        return square
    elif type == "cube":
        return cube
    elif type == "absolute":
        return absolute

result = higher_order_function("square")
print(result(3))
result = higher_order_function("cube")
print(result(3))
result = higher_order_function("absolute")
print(result(-3))

def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add
closure_result = add_ten()
print(closure_result(15))
print(closure_result(10))

def greeting():
    return "Welcome to Python"
def uppercase_decorate(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorate(greeting)
print(g())

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return "Welcome to Python"
print(greeting())

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper
@split_string_decorator
@uppercase_decorator
def greeting():
    return "Welcome to Python"
print(greeting())

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(p1,p2,p3):
        function(p1,p2,p3)
        print("I live in {}".format(p3))
    return wrapper_accepting_parameters
@decorator_with_parameters
def print_full_name(first_name,last_name,country):
    print("I am {} {}. I love to teach.".format(first_name,last_name))
print_full_name("Tung","Nguyen","Vietnam")

numbers = [1,2,3,4,5]
def square(x):
    return x ** 2
numbers_squared = map(square,numbers)
print(list(numbers_squared))

numbers_squared = map(lambda x : x ** 2,numbers)
print(list(numbers_squared))

numbers_str = ["1","2","3","4","5"]
numbers_int = map(int,numbers_str)
print(list(numbers_int))

names = ["Asabeneh","Lidiya","Ermias","Abraham"]
def change_to_upper(name):
    return name.upper()
names_upper_cased = map(change_to_upper,names)
print(list(names_upper_cased))
names_upper_cased = map(lambda name : name.upper(),names)
print(list(names_upper_cased))

numbers = [1,2,3,4,5]
def is_evenn(num):
    if num % 2 == 0:
        return True
    return False
even_numbers = filter(is_evenn,numbers)
print(list(even_numbers))

def is_odd(num):
    if num % 2 != 0:
        return True
    return False
odd_numbers = filter(is_odd,numbers)
print(list(odd_numbers))

names = ["Asabeneh","Lidiya","Ermias","Abraham"]
def is_name_long(name):
    if len(name) > 7:
        return True
    return False
long_names = filter(is_name_long,names)
print(list(long_names))
def is_name_long(name):
    if len(name) < 7:
        return True
    return False
long_names = filter(is_name_long,names)
print(list(long_names))

from functools import reduce
numbers_str = ["1","2","3","4","5"]
def add_two_nums(x,y):
    return int(x) + int(y)
total = reduce(add_two_nums,numbers_str)
print(total)