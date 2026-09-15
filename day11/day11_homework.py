import math

def add_two_numbers(a,b):
    total = a + b
    return total
print(add_two_numbers(1,2))

def area_of_circle(r):
    pi = 3.14
    area = pi * r ** 2
    return area
print(area_of_circle(10))

def add_all_nums(*nums):
    total = 0
    for i in nums:
        if not isinstance(i,(int,float)):
            return "Error"
        total += i
    return total
print(add_all_nums(1,2,3,4,5,6))

def convert_celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
print(f"F = {convert_celsius_to_fahrenheit(100)}")

def check_seasons(month):
    if month in [9,10,11]:
        return "Winter"
    elif month in  [12,1,2]:
        return "Spring"
    elif month in [3,4,5]:
        return "Summer"
    elif month in [6,7,8]:
        return "Autumn"
print(check_seasons(1))

def calculate_slope(x1,x2,y1,y2):
    return (y2 - y1) / (x2 - x1)
print(calculate_slope(6,5,4,3))

def solve_quadratic_eqn(a,b,c):
    if a == 0:
        if b == 0:
            return "PT vo nghiem"
        return -c / b
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / 2 * a
        x2 = (-b - math.sqrt(delta)) / 2 *a
        return x1 , x2
    elif delta == 0:
        x = -b / 2 * a
        return x
    else:
        return "Pt vo nghiem"
print(solve_quadratic_eqn(1,-2,1))

def print_list(lst):
    for i in lst:
        print(i)
number = [1,2,3,4,5]
print_list(number)

def reverse_list(lst):
    reverse = []
    for i in range(len(lst)-1, -1, -1):
        reverse.append(lst[i])
    return reverse
print(reverse_list([1,2,3,4,5]))
print(reverse_list(["A","B","C"]))

def capitalize_list_items(lst):
    capitalize_list = []
    for i in lst:
        capitalize_list.append(i.capitalize())
    return capitalize_list
print(capitalize_list_items(["banana","orange"]))            

def add_item(lst,a):
    add_list = []
    for i in lst:
        add_list.append(i)
    add_list.append(a)
    return add_list
food = ["Potato","Orange"]
print(add_item(food,"Apple"))

def added_item(lst,a):
    return lst + a
food = ["Potato","Orange"]
print(add_item(food,"Apple"))

def remove_item(lst,a):
    if a in lst:
        lst.remove(a)
    return lst
food = ["Potato","Orange"]
print(remove_item(food,"Potato"))

def sum_of_number(num):
    total = 0
    for i in range(num+1):
        total += i
    return total
print(sum_of_number(5))
print(sum_of_number(10))

def sum_of_num(num):
    total_of_odds = 0
    total_of_even = 0
    for i in range(num+1):
        if i % 2 == 0:
            total_of_even += i
        else:
            total_of_odds += i
    return total_of_odds,total_of_even
print(sum_of_num(100))

def evens_and_odds(n):
    even = []
    odd = []
    for i in range(n+1):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return len(even),len(odd)
print(evens_and_odds(100))

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result
print(factorial(5))

def is_empty(n=""):
    if n == "":
        return "Empty"
    else: 
        return "Not empty"
print(is_empty())

def greet(name="Guest"):
    if name == "":
        return "Hello, Guest"
    else:
        return f"Hello,{name}"
print(greet("Tung"))

def show_args(**args):
    lst = [f"{key}: {value}" for key,value in args.items()]
    print("Received: " + ",".join(lst))
show_args(name="Alice",age=30,city="New York")

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
print(is_prime(2))

def check_unique(lst):
    return len(lst) == len(set(lst))
print(check_unique([1,2,3,4,5,1]))

def check_type(lst):
    if not lst:
        return True
    first_type = type(lst[0])
    return all(isinstance(i,first_type) for i in lst)
print(check_type([1,2,3,"a"]))

def is_valid(name):
    return name.isidentifier()
print(is_valid("hello"))