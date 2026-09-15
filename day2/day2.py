print("Hello, World!")

print(len("Hello, World!"))

print(str(10))
print(int(9.8))
print(float(10))

print(input("Enter your name:"))

help(str)
print(dir(str)) 

print(min(20,30,40,50))
print(max(20,30,40,50))
print(min([20,30,40,50]))
print(max([20,30,40,50]))
print(sum([20,30,40,50]))

#variables in Python
first_name = "TUng"
last_name = "Tung"
country = "Vietnam"
city = "Hanoi"
age = 19
is_married = False
skills = ["HTML","Python","C++"]
person_info = {
    "first_name" : "TUng",
    "last_name" : "Tung",
    "country" : "Vietnam",
    "city" : "Hanoi"
}

print(first_name,last_name,country,city,age,is_married,skills,person_info)
print("First Name:", first_name)
print("First name length:",len(first_name))
print("Last name:",last_name)
print("Last name length:", len(last_name))
print("Country:",country)
print("City:",city)
print("Age:",age)
print("Married:",skills)
print("Person information:",person_info)

print("Hello, World!")
print("Hello",",","World","!")
print(len("Hello, World!"))

first_name,last_name,country,age,is_married = "Nguyen","Tung","Vietnam",19,False

print(first_name,last_name,country,age,is_married)
print("First name:",first_name)
print("Last name:",last_name)
print("Country:",country)
print("Age:",age)
print("Married:",is_married) 

first_name = input("What is your name:")
age = input("How old are you?")
print(first_name)
print(age)


#different python data types
first_name = "Tung"
last_name = "Nguyen"
country = "Vietnam"
city = "Hanoi"
age = 200

#printing out types
print(type("Tung"))
print(type(first_name))
print(type(10))
print(type(3.14))
print(type(1+1j))
print(type(True))
print(type([1,2,3,4]))
print(type({"name" : "Tung"}))
print(type((1,2)))
print(type(zip([1,2],[3,4])))

# int to float
num_int = 10
print("num_int = ",num_int)
num_float = float(num_int)
print("num_float = ",num_float)

#float to int
gravity = 9.81
print(int(gravity))

#str to int or float
num_str = "10.6"
num_fl = float(num_str)
num_in = int(num_fl)
print("num_int = ",num_in)
print("num_float = ",num_fl)
num_in = int(num_fl)
print("num_int = ",num_in)

#str to list
first_name = "Tung"
print(first_name)
first_name_to_list = list(first_name)
print(first_name_to_list)