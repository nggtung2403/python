import sys
print("Xin chao,\nToi dang hoc\nPython!")
name = "Tung"
age = "19"
city = "Hanoi"
print(f"Toi ten la {name} {age} tuoi song o {city}")
print(type(10))
print(type(3.14))
print(type("Python"))
print(type(True))
print(type([1,2,3]))
name = input("nhap ten: ")
years = input("nhap nam sinh: ")
print(name)
print(years)
a = 5
b = 8
print(f"a + b = {a+b} | a - b = {a-b} | a * b = {a*b} | a / b = {a/b}")
lst = "I am enjoying 30 days of python challenge"
print(len(lst))
a = int(input("nhap chieu dai: "))
b = int(input("nhap chieu rong: "))
area = a * b
parameter = (a+b)*2
print(area)
print(parameter)

print(sys.version)

a = 1
b = 2.2
c = "hello world"
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))

company_name = "Google"
foundation_year = 1998
city = "Mountain View"
print(f"{company_name} duoc thanh lap nam {foundation_year} tai {city}")

print(round(3.14159))
lst = [23,45,12,67,34,89,10]
print(max(lst),min(lst),sum(lst))

num = "24.2"
print(type(num))
num = int(float(num))
print(type(num))
num = float(num)
print(type(num))

a = 10
b = 10
c = [1,2]
d = [1,2]
print(id(a))
print(id(b))
print(id(c))
print(id(d))
print(a is b)
print(b is c)
print(c is d)

lst = [1,2,3,4,5,6,7,8]
avg = sum(lst) / len(lst)
print(avg)
print(0.1 + 0.2 == 0.3)
print(round(0.1) + round(0.2) == round(0.3))

a = 15
b = 4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

print(10>5)
print(10 == 10.0)
print("abc" == "abc")
print(10 != 9)

x = True
y = False
print(x and y)
print(x or y)
print(not x)

num = int(input("Nhap so: "))
if num % 2 == 0:
    print("even")
else:
    print("odd")

year = int(input("nhap nam: "))
if year % 4 == 0 and year % 100 != 0:
    print("nam nhuan")
else:
    print("nam ko nhuan")

print("a" in "banana")
print(5 in [1,2,3,4])

n = 5
print(10 < n <100 and n % 2 == 0)

a = 5
b = 10
a , b = b , a
print(a,b)

s = "Thirty Days Of Python"
print(s.upper())
print(s.lower())
print(len(s))
print(s[0:6],s[-1:-7])
print("Python" in s)

sentence = "I am a teacher and I love teaching"
print(sentence.count("teach"))
print(sentence.replace(" ","_"))

a = "Python,JavaScript,C#,Java"
a = a.split(",")

a = "madam"
if s == s[::-1]:
    print("palindrome")
else:
    print("ko phai palindrome")

lst = "To be a great developer , you need to Practice, Practice and Practice"
print(len(lst))
print(lst.count("Practice"))
print(f"Cau co {len(lst)} tu va tu \'Practice\' xuat hien {lst.count("Practice")}")

fruits = ["banana","orange","mango","lemon"]
print(fruits)
print(len(fruits))
print(fruits[0],fruits[-1])
fruits.append("apple")
fruits.insert(0,"kiwi")
fruits.remove("lemon")
print(fruits)

numbers = [5,2,9,1,7,3]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
it_companies = ["Facebook","Google","Microsoft","Apple","IBM"]
does_exist = "Google" in it_companies
print(does_exist)
it_companies = list(it_companies)
for company in it_companies:
    company.upper()
print(it_companies)

lst = [1,2,3,4,4,4,5]
lt = []
ltt = []
lttt = []
for i in lst:
    if i not in lst:
        lt.append(i)
print(lt)
for i in lst:
    if i % 2 == 0:
        ltt.append(i)
    else:
        lttt.append(i)
print(ltt)
print(lttt)

siberian = ("Adam","Sadio","Ferdinand")
print(len(siberian))
print(siberian[1])

a = (1,2,3)
a = list(a)
a.append(4)
a = set(a)
print(a)
a,b,c = (10,20,30)
total = a+b+c
print(total)

nested = ((1,2),(3,4),(5,6))
for i in nested:
    print(sum(i))

def a(numbers):
    return (min(numbers),max(numbers),sum(numbers),sum(numbers)/len(numbers))
data = (10,20,30,40)
result = a(data)
print(result)

lst = [("An",20),("Binh",18),("Chi",25)]
sorte = sorted(lst,key=lambda item: item[1])
print(sorte)

it_companies = {"Facebook","Google","Microsoft","Apple","IBM"}
it_companies.add("Oracle")
it_companies.remove("Facebook")
print("Amazon" in it_companies)

A = {1,2,3,4,5}
B = {4,5,6,7,8}
print(A.union(B))
print(A.symmetric_difference(B))
print(A.issuperset({1,2,3}))
print({1,2,3}.issuperset(A))

lst = [1,2,3,3,4,4,5,5]
lst = set(lst)
lst = sorted(lst)
print(lst)
T = {"A","B","C"}
L = {"A","B","D"}
print(set(T.difference(L)))
print(set(L.difference(T)))

person = {
    "first_name" : "Asabeneh",
    "last_name": "Yetayeh",
    "age":250,
    "country":"Finland"
}
print(person.keys())
person["skills"] = ["Python","SQL"]
print(person)
print("age" in person)
person["age"] = 30
person.pop("country")
print(person.get("job"))
print(person.items())

students = [
    {"name":"An","score":8.5},
    {"name":"Binh","score":6.0},
    {"name":"Chi","score":9.2}
]
top = max(students,key=lambda s:s["score"])
print(top)

text = "apple orange apple banana"
words = text.split()
wordc = {}
for word in words:
    if word in wordc:
        wordc[word] += 1
    else:
        wordc[word] = 1
print(wordc)

a = int(input("nhap a: "))
if a > 0:
    print("so duong")
elif a == 0:
    print("bang 0")
else:
    print("so am")

age = int(input("nhap tuoi:"))
if age < 13:
    print("Tre em")
elif 13 < age <20:
    print("Thanh thieu nien")
else:
    print("nguoi lon")

a = int(input("nhap a: "))
if a % 3 == 0 and a % 5 == 0:
    print("FizzBuzz")
else:
    print("sai")

point = int(input("nhap diem: "))
if point >= 90:
    print("A")
elif point >= 80:
    print("B")
elif point >= 70:
    print("C")
elif point >= 60:
    print("D")
else:
    print("F")

years = int(input("Nhap nam: "))
if years % 4 ==0 and years % 100 != 0:
    print("Nam nhuan")
else:
    print("Nam thuong")

a = 1
b = 2
c = 3
if (a>b) and (a>c):
    print(a)
elif (b>a) and (b>c):
    print(b)
else:
    print(c)
    