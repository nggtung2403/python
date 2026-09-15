lst = list()
empty_list = list()
print(len(empty_list))

lst= []
empty_list = []
print(len(empty_list))

fruits = ["banana","orange","mango","lemon"]
vegetables = ["tomato","potato","cabbage","onion","carrot"]
animal_products = ["milk","meat","butter","yoghurt"]
web_techs = ["Html","Css","React","Redux","Node","MongDB"]
countries = ["Finland","Estonia","Denmark","Sweden","Norway"]

print("Fruits:", fruits)
print(len(fruits))
print("Vegetables: ",vegetables)
print(len(vegetables))
print("Animal Products: ",animal_products)
print(len(animal_products))
print("Web technologies: ",web_techs)
print(len(web_techs))
print("Countries: ",countries)
print(len(countries))

lst = ["Asabeneh",250,True,{"country":"Finland","city":"Helsinki"}]
print(lst)

fruits = ["banana","orange","mango","lemon"]
first_fruit = fruits[0]
print(first_fruit)
second_fruit = fruits[1]
print(second_fruit)
last_fruits = fruits[len(fruits)-1]
print(last_fruits)

last_fruits = fruits[-1]
print(last_fruits)
first_fruit = fruits[-4]
print(first_fruit)
second_fruit = fruits[-2]
print(second_fruit)

lst = ["item1","item2","item3","item4","item5"]
first_item,second_item,third_item,*rest = lst
print(first_item)
print(second_item)
print(third_item)
print(rest)

fruits = ["banana","orange","mango","lemon"]
first_fruit,second_fruit,*last_fruits = fruits
print(first_fruit)
print(second_fruit)
print(last_fruits)

first,second,third,*number = [1,2,3,4,5,6,7,8,9,10]
print(first)
print(second)
print(third)
print(number)

countries = ["Germany","France","Vietnam","Sweden","Iceland","Estonia"]
gr,f,vn,*countries,ic,es = countries
print(gr)
print(f)
print(vn)
print(countries)
print(ic)
print(es)

fruits = ["banana","orange","mango","lemon"]
print(fruits[0:4])
print(fruits[0:])
print(fruits[1:3])
print(fruits[1::2])
print(fruits[-4:])
print(fruits[-3:-1])
print(fruits[::-1])

fruits = ["banana","orange","mango","lemon"]
does_exist = "banana" in fruits
print(does_exist)
does_exist = "lime" in fruits
print(does_exist)

fruits = ["banana","orange","mango","lemon"]
fruits.append("lime")
print(fruits)

fruits = ["banana","orange","mango","lemon"]
fruits.insert(2,"lime")
print(fruits)
fruits.insert(4,"grapes")
print(fruits)

fruits = ["banana","orange","mango","lemon"]
fruits.remove("banana")
print(fruits)

fruits = ["banana","orange","mango","lemon"]
fruits.pop()
print(fruits)

fruits = ["banana","orange","mango","lemon"]
fruits.pop(1)
print(fruits)

fruits = ["banana","orange","mango","lemon"]
del fruits[1]
print(fruits)
fruits.clear()
print(fruits)

fruits = ["banana","orange","mango","lemon"]
fruits_copy = fruits.copy()
del fruits_copy[0]
print(fruits_copy)
print(fruits)

positive_number = [1,2,3,4,5]
negative_number = [-5,-4,-3,-2,-1]
zero = [0]
integers = negative_number + zero + positive_number
print(integers)

list1 = [0,1,2,3]
list2= [4,5,6]
list1.extend(list2)
print(list1)

fruits = ["banana","orange","mango","lemon"]
print(fruits.count("banana"))
ages = [1,2,3,4,5,1,2,3,1,1,1,1,1]
print(ages.count(1))

fruits = ["banana","orange","mango","lemon"]
fruits.reverse()
print(fruits)

fruits = ["banana","orange","mango","lemon"]
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
fruits = sorted(fruits,reverse=True)
print(fruits)