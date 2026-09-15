print(True)
print(False)

#Arithmetic Operation in Python
#Integers

print("Addition: ",1+2)
print("Subtraction: ",2-1)
print("Multiplication: ",2*3)
print("Division: ",4/2)
print("Division: ",6/2)
print("Division: ",7/2)
print("Division without the remainder: ",7//2)
print("Division without the remainder: ",7//3)
print("Modulus: ",3%2)
print("Exponentiation: ",2**3)

#Floating numbers
print("Floating Point Number, PI", 3.14)
print("Floating Point Number, gravity",9.81)

#Complex numbers
print("Complex number: ",1+1j)
print("Multiplying complex numbers: ",(1+2j) * (2-5j))

#Declearing the variable at the top first
a = 3
b = 2

#Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a/b
remainder = a % b
floor_remainder = a // b
exponential = a ** b

print(total)
print("a + b = ",total)
print("a - b = ",diff)
print("a * b = ",product)
print("a / b = ",division)
print("a % b = ",remainder)
print("a // b = ",floor_remainder)
print("a ** b = ",exponential)

print("== Addition,Subtraction,Multiplication,Division,Modulus ==")

#Declering values and organizing them together
num_one = 3
num_two = 4

#Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

#Printing values with label
print("total: ",total)
print("Difference: ",diff)
print("Product: ",product)
print("Division: ",div)
print("Remainder: ",remainder)

#Calculating area of a circle
radius = 10
area_of_circle = radius ** 2 * 3.14
print("Area of a circle: ",area_of_circle)

#Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print("Area of rectangle: ",area_of_rectangle)

#Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print("Weight: ",weight)

#Calculate the density of a liquid
mass = 75
volume = 0.075
density = mass / volume
print(density,"Kg/m^3")

print(3 > 2)
print(3 >= 2)
print(3 < 2)
print(2 < 3)
print(2 <= 3)
print(3 == 2)
print(3 != 2)
print(len("tung") == len("nguyen"))
print(len("tung") != len("nguyen"))
print(len("tung") < len("nguyen"))
print(len("tung") > len("nguyen"))

#Comparing something gives either a True or False
print("True == True: ",True == True)
print("True == False: ",True == False)
print("False == False: ",False == False)

print("1 is 1: ", 1 is 1)
print("1 is not 2: ", 1 is not 2)
print("T in Tung", "T" in "Tung")
print("t not in Tung", "t" not in "Tung")
print("coding" in "Tung is coding")
print("4 is 2**2: ", 4 is 2**2)

print(3 > 2 and 5 > 3)
print(3 > 2 and 4 < 3)
print(True and True)
print(3>2 or 4 > 3)
print(3>2 or 2<1)
print(False or True)
print(not 2 > 1)
print(not 1 > 2)
print(not True)