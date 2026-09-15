person = {
    "first_name" : "Tung",
    "last_name" : "Nguyen",
    "age" : 19,
    "country" : "Vietnam",
    "is_married" : False,
    "address" : {
        "street" :"Thong Nhat Street",
        "House number" : 4,
    },
}
print(person)
print(len(person))
print(person["first_name"])
print(person["address"]["street"])
print(person.get("first_name"))
print(person.get("last_name"))
print(person.get("address")["street"])

person["city"] = "Hanoi"
print(person)

person["first_name"] = "Meow"
print(person)

print("first_name" in person)
print("hehe" in person)

person.pop("city")
print(person)
person.popitem()
print(person)
del person["first_name"]
print(person)

print(person.items())
print(person.clear())
del person

person = {
    "first_name" : "Tung",
    "last_name" : "Nguyen",
    "age" : 19,
    "country" : "Vietnam",
    "is_married" : False,
    "address" : {
        "street" :"Thong Nhat Street",
        "House number" : 4,
    },
}

person_copy = person.copy()
print(person_copy)
keys = person_copy.keys()
print(keys)
values = person_copy.values()
print(values)