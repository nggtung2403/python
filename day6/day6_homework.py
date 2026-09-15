lst = ()
brother = ("hihi",)
sister = ("haha",)
father =("huhu",)
mother = ("hehe",)
sibling = sister +brother
print(sibling)
print(len(sibling))
family_members = sibling + father + mother
print(family_members)
sibling = family_members[:2]
parents = family_members[2:]
print(sibling)
print(parents)

fruits = ("apple","orange")
vegetables = ("tomato","potato","cabbage","onion","carrot")
animal_products = ("milk","meat","butter","yoghurt")
food_stuff_lt = fruits + vegetables + animal_products
print(food_stuff_lt)
food_stuff_lt = list(food_stuff_lt)
print(food_stuff_lt)
mid = len(food_stuff_lt) // 2
print(food_stuff_lt[mid])
food_stuff_lt = food_stuff_lt[3:-3]
print(food_stuff_lt)
del food_stuff_lt

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)