for i in range(11):
    print(i)

i = 0
while i < 11:
    print(i)
    i += 1

for i in range(10,-1,-1):
    print(i)

i = 10
while i <= 10:
    print(i)
    i -= 1
    if i == -1:
        break

for i in range(8):
    print("#" * i)

for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print()

for i in range(11):
    print(f"{i} x {i} = {i*i}")

lst = ["Python","Numpy","Pandas","Django","Flask"]
for i in lst:
    print(i)

for i in range(0,100,2):
    print(i)

for i in range(0,100):
    if i % 2 != 0:
        print(i)

total = 0
for i in range(0,101):
    total += i
print(total)

odd_total = 0
even_total = 0
for i in range(0,101):
    if i%2 == 0:
        even_total += i
    else:
        odd_total += i
print(odd_total)
print(even_total)

countries = ["Findland","Iceland","Ireland","Thailand","Vietnam","Japan","Germany","Canada"]
for i in countries:
    if "land" in i:
        print(i)

fruits = ["banana","orange","mango","lemon"]
fruits_reverse = []
for i in range(len(fruits)-1,-1,-1):
    fruits_reverse.append(fruits[i])
print(fruits_reverse)    

