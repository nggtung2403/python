import math
age = 19
height = 177.9
complexx = 1+1j
base = int(input("Enter base: "))
height = int(input("Enter height: "))
area_of_triangle = 1/2 * base * height
print(f"The area of the triangle is {int(area_of_triangle)}") 

a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
perimeter_of_triangle = a + b + c
print(f"The perimeter of the triangle is {int(perimeter_of_triangle)}")

height = int(input("Enter height: "))
width = int(input("Enter width: "))
area = height * width
perimeter = 2* (height + width)
print(f"Area = {area} , Perimeter = {perimeter}")

radius = int(input("Enter radius: "))
area = 2 * 3.14 * radius ** 2
perimeter = 2 * 3.14 * radius

m = 2
x1 = 0
y = 2 * x1 - 2

y2 = 0
x = (y2+2)/2

print(f"diem cat truc y: (0,{y})")
print(f"diem cat truc x: (0,{x})")

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))
m2 = (y2 - y1) / (x2 - x1)
euclid = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(f"Do doc = {m2}")
print(f"Euclid = {euclid}")

print(m > m2) 

x = int(input("Enter X: "))
y = (x + 3)**2
print(f" x = {x} then y = ",y)

print(len("python") > len("dragon"))
print("on" in ("dragon" and "python"))
print("jargon" in "i hope this course is not full of jargon")
print("on" not in ("python" and "dragon"))

a = len("Python")
b = float(a)
c = str(b)
print(a,b,c)

a = int(input("nhap a: "))
print(a%2==0)

a = 7 //3
b = int(2.7)
print(a == b) 

print("10" == 10)

a = int(float("9.8"))
print(a == 10)

a = int(input("Enter hours: "))
b = int(input("Enter rate per hour: "))
salary = a * b
print(f"Your weekly salary is {salary}")

years = int(input("Enter number of year you have lived: "))
sec = years * 31536000
print(f"You have lived for {sec} seconds.")

for n in range(1,6):
    print(f"{n} 1 {n} {n**2} {n**3}")