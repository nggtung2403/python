try:
    print(10 + 5)
except:
    print("something went wrong")

try:
    name = input("Enter your name:")
    year_born = input("Year you were born:")
    age = 2026 - year_born
    print(f"you are {name}. And your age is {age}")
except:
    print("somthing went wrong!")

try:
    name = input("Enter your name:")
    year_born = int(input("year you were born:"))
    age = 2026 - year_born
    print(f"You are {name} and your age is {age}")
except TypeError:
    print("Type error occured")
except ValueError:
    print("value error occured")
except ZeroDivisionError:
    print("zero division error occured")
else:
    print("i usually run with the try block")
finally:
    print("i always run")

try:
    name = input("Enter your name: ")
    year_born = input("Year you born: ")
    age = 2026 - int(year_born)
    print(f"you are {name} and your age is {age}")
except Exception as e:
    print(e)

def sum_of_list(a,b,c,d,e):
    return a + b + c + d + e
lst = [1,2,3,4,5]
print(sum_of_list(*lst))

numbers = range(2,7)
print(list(numbers))
args = [2,7]
numbers = range(*args)
print(list(numbers))

countries = ["Finland","Sweden","Norway","Denmark","Iceland"]
fin,sw,nor,*rest = countries
print(fin,sw,nor,rest)
numbers = [1,2,3,4,5,6,7]
one,*middle,last = numbers
print(one,middle,last)

def unpacking_person_info(name,country,city,age):
    return f"{name} lives in {country},{city} he is {age} year old."
dct = {"name": "tung","country":"Vietnam","city":"Hanoi","age":19}
print(unpacking_person_info(**dct))

def sum_all(*args):
    s = 0
    for i in args:
        s+=i
    return s
print(sum_all(1,2,3,4,5,6))

def packing_person_info(**kwargs):
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs
print(packing_person_info(name="Asabeneh",country="Finland", city="Helsinki", age=250))

lst_one = [1,2,3]
lst_two = [4,5,6,7]
lst = [0,*lst_one,*lst_two]
print(lst)

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
for index,i in enumerate(countries):
    if i == "Finland":
        print(f"the country{i} has been found at index {index}")

fruits = ["banana","orange","mango","lemon","lime"]
vegetables = ["Tomato","Potato","Cabbge","Onion","Carrot"]
fruits_and_vegetables = []
for f,v in zip(fruits,vegetables):
    fruits_and_vegetables.append({"fruit":f,"veg":v})
print(fruits_and_vegetables)