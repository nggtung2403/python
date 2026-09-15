countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

from functools import reduce
mapped = list(map(lambda x : x * 2, numbers))
print(mapped)
filt = list(filter(lambda x : x % 2 == 0,numbers))
print(filt)
total = reduce(lambda x,y: x+y,numbers)
print(total)

for i in countries:
    print(i)

for i in names:
    print(i)

for i in numbers:
    print(i)

name = map(lambda x : x.upper(),countries)
print(list(name))
nums = map(lambda x : x**2,numbers)
print(list(nums))
name = map(lambda x: x.upper(),names)
print(list(name))
land_countries = filter(lambda x: "land" in x,countries)
print(list(land_countries))
country = filter(lambda x : len(x) == 6,countries)
print(list(country))
country = filter(lambda x: "E" in x,countries)
print(list(country))

result = reduce(lambda acc,x: acc +x,filter(lambda x : x > 5, map(int,numbers)))
print(result)

result = reduce(lambda a,b : a + b,numbers)
print(result)
result = reduce(lambda a,b: f"{a},{b}",countries[:-1])
sentence = f"{result},and {countries[-1]} are not of European countries"
print(sentence)