#syntax
tpl = ("item1","item2","item3")
fruits = ("banana","orange","mango","lemon")
print(len(tpl))

tp1 = ("item1","item2","item3")
first_item = tp1[0]
second_item = tp1[1]
last_index = tp1[len(tpl)-1]
print(first_item)
print(second_item)
print(last_index)

tp1 = ("item1","item2","item3","item4")
first_item = tp1[-4]
second_item = tp1[-3]
last_index = tpl[-1]
print(first_item)
print(second_item)
print(last_index)

tp1 = ("item1","item2","item3","item4")
all_items = tp1[0:4]
print(all_items)
all_items = tp1[0:]
print(all_items)
it2_to_it3 = tp1[1:3]
print(it2_to_it3)
all_items = tp1[-4:]
print(all_items)

tp1 = ("item1","item2","item3","item4")
lst = list(tp1)
print(lst)

fruits =("banana","orange","mango","lemon")
fruits = list(fruits)
fruits[0] = "apple"
print(fruits)
fruits = tuple(fruits)
print(fruits)

fruits =("banana","orange","mango","lemon")
does_exits = "banana" in fruits
print(does_exits)

tpl1 = ("item1","item2","item3")
tpl2 = ("item4","item5","item6")
tpl3 = tpl1 + tpl2
print(tpl3)

tpl1 = ("item1","item2","item3")
del tpl1
