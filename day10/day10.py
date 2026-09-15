count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        break

count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count += 1

numbers = [0,1,2,3,4,5]
for number in numbers:
    print(number)

language = "Python"
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)

person = {
    "first_name" : "Asabeneh",
    "last_name" : "Yetayeh",
    "age" : 250,
    "country" : "Finland",
    "is_married" : True,
    "skills" : ["JavaScript","React","Node","MongoDB","Python"],
    "address" : {
        "street" : "Space street",
        "zipcode" : "02210"
    }
}
for key in person:
    print(key)
for value in person.values():
    print(value)
for key , value in person.items():
    print(key,value)

it_companies = {"Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"}
for company in it_companies:
    print(company)

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print("Next number should be",number + 1) if number != 5 else print("loop's end")
print("outside the loop")

lst = list(range(11))
print(lst)
st = set(range(1,11))
print(st)

lst = list(range(0,11,2))
print(lst)
st = set(range(0,11,2))
print(st)

lst = list(range(11,0,-2))
print(lst)

for i in range(11):
    print(i)

person = {
    "first_name" : "Asabeneh",
    "last_name" : "Yetayeh",
    "age" : 250,
    "country" : "Finland",
    "is_married" : True,
    "skills" : ["JavaScript","React","Node","MongoDB","Python"],
    "address" : {
        "street" : "Space street",
        "zipcode" : "02210"
    }
}
for key in person:
    if key == "skills":
        for skill in person["skills"]:
            print(skill)

for number in range(11):
    print(number)
else:
    print("The loop end at",number)

for number in range(11):
    pass