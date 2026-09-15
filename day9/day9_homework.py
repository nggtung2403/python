age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    age_need = 18 - age
    print(f"You need {age_need} more years to learn to drive.")

my_age = int(input("Enter my age: "))
your_age = int(input("Enter your age: "))
if your_age > my_age:
    if your_age - my_age == 1:
        print("You are 1 year older than me.")
    elif your_age - my_age >1:
        diff = your_age - my_age
        print(f"You are {diff} years older than me.")
elif your_age == my_age:
    print("We are the same age")
else:
    print("You are younger than me.")

a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a > b:
    print(f"{a} is greater than {b}")
elif a == b:
    print(f"{a} equal {b}")
else:
    print(f"{a} is smaller than {b}")

student_point = int(input("Enter point: "))
print("Xep hang")
if student_point >= 90 and student_point <= 100:
    print("A")
elif student_point >= 80 and student_point <= 89:
    print("B")
elif student_point >= 70 and student_point <= 79:
    print("C")
elif student_point >= 60 and student_point <= 69:
    print("D")
else:
    print("F")

month = int(input("Enter the month: "))
if month >8 and month < 11:
    print("Autumn")
elif month > 2 and month < 6:
    print("Spring")
elif month >5 and month < 9:
    print("Summer")
elif month == 12 or month == 1 or month == 2:
    print("Winter")

fruits = ["banana","orange","mango","lemon"]
enter_fruit = input("Enter fruits: ")
if enter_fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(enter_fruit)
    print(fruits)

person ={
    "first_name" : "Asabeneh",
    "last_name" : "Yetayeh",
    "age" : 250,
    "country" : "Finland",
    "is_married" : True,
    "skills" : ["JavaScript","React","Node","MongoDB","Python"],
    "adress": {
        "street": "Space street",
        "zipcode":"02210",
    },
}
keys = person.keys()
print(keys)
middle_skill = len(person["skills"]) // 2
print(person["skills"][middle_skill])
does_exist = "Python" in person["skills"]
print(does_exist)

if person["skills"] == ["JavaScript","React"]:
    print("He is a front end developer")
elif person["skills"] == ["Node","Python","MongoDB"]:
    print("He is backend developer")
elif person["skills"] == ["React","Node","MongoDB"]:
    print("He is a fullstack developer")
else:
    print("unknown title")

if person["is_married"] == True and person["country"] == "Finland":
    print(person["first_name"], person["last_name"],"lives in",person["country"],".","He is married")
