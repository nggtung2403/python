def generate_full_name():
    first_name = "Asabeneh"
    last_name = "Yetayeh"
    space = " "
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name()

def add_two_numbers():
    num_one = 1
    num_two = 2
    total = num_one + num_two
    return total
print(add_two_numbers())

def greetings(name):
    message = name + ",welcome to Python for Everyone!"
    return message
print(greetings("Asabeneh"))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(5))

def square_number(x):
    return x * x
print(square_number(5))

def area_of_circle(r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(5))

def sum_of_numbers(n):
    total = 0
    for i in range (n+1):
        total += i
    return total
print(sum_of_numbers(5))

def generate_full_name(first_name,last_name):
    space = " "
    fullname = first_name + space + last_name
    return fullname
print("Full name: ",generate_full_name("Asabeneh","Yetayeh"))

def sum_two_numbers (num_one,num_two):
    sum = num_two + num_one
    return sum
print("Sum of two number",sum_two_numbers(1,2))

def calculate_age(current_year,birth_year):
    age = current_year - birth_year
    return age
print(calculate_age(2026,2007))

def weight_of_object (mass,gravity):
    weight = str(mass * gravity) + " N"
    return weight
print("Weight of an object in Newtons: ",weight_of_object(100,9.81))

def print_fullname(firstname,lastname):
    space = " "
    fullname = firstname + space + lastname
    return fullname
print(print_fullname(firstname="Asabeneh",lastname="Yetayeh"))

def is_even(n):
    if n % 2 == 0:
        return True
    return False
print(is_even(7))
print(is_even(2))

def find_even_numbers(n):
    evens = []
    for i in range(n+1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))

def greetings(name = "Peter"):
    message = name + ",welcome to Python for Everyone"
    return message
print(greetings())
print(greetings("Asabeneh"))

def calculate_age(birth_year,current_year = 2026):
    age = current_year - birth_year
    return age
print(calculate_age(2007))
print(calculate_age(2007,2030))

def sum_all_numbers(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(sum_all_numbers(2,3,4,5,6,7))

def generate_groups(team,*args):
    print(team)
    for i in args:
        print(i)
generate_groups("Team 1","hehe","hihi","haha")

def greet(name,location):
    print("Hi there",name,"how is the weather in",location)
greet("Asabeneh","NewYork")
my_dict = {"name":"Alice","location":"New York"}
greet(**my_dict)

def arbitrary_named_args(**args):
    print("I received an arbitrary of arguments,totaling",len(args))
    print("They are provided as a dictionary in my function",type(args))
    print("Let's print them:")
    for k,v in args.items():
        print("* key:",k,"value:",v)
arbitrary_named_args()

def square_number(n):
    return n * n
def do_something(f,x):
    return f(x)
print(do_something(square_number,3))