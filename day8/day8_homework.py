dog = {
    "name" : "ducky",
    "color" : "brown",
    "type" : "husky",
    "feet" : "30cm",
    "age" : 4,
}
print(dog)

students = {
    "first_name" : "Tung",
    "last_name" : "Nguyen",
    "gender" : "Male",
    "age" : 19,
    "marital status" : "Single",
    "skills" : ["Python","C++"],
    "country" : "Vietnam",
    "city" : "Hanoi",
    "adress" : {
        "street" : "Thong Nhat Street",
        "house number" : 4,
    },
}
print(students)
print(len(students))
skills = students["skills"]
print(skills)
print(type(skills))
students["skills"].append("HTML")
print(students)
keys = students.keys()
print(keys)
values = students.values()
stu = students.items()
print(stu)
students.pop("city")
print(students)
del students
