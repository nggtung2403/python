letter = "P"
print(letter)
print(len(letter))
greeting = "Hello, World!"
print(greeting)
print(len(greeting))
sentence = "I hope you are enjoying 30 days of Python Chanllenge"
print(sentence)
print(len(sentence))

multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

first_name = "Asabeneh"
last_name = "Yetayeh"
space = " "
full_name = first_name + space + last_name
print(full_name)

print(len(first_name))
print(len(last_name))
print(len(full_name))
print(len(full_name) > len(first_name))

print("I hope everyone is enjoying the Python Challenge. \nAre you?")
print("Days\tTopics\tExercises")
print("Day1\t5\t5")
print("Day2\t6\t20")
print("Day3\t5\t23")
print("Day4\t1\t35")
print("This is blackslash symbol (\\)")
print("In every programming language it starts with \"Hello, World!\"")

first_name = "Asabeneh"
last_name = "Yetayeh"
language = "Python"
formted_string = "I am %s %s. I teach %s" %(first_name,last_name,language)
print(formted_string)

radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = "The area of circle with a radius %d is %.2f." %(radius,area)
print(formated_string)

python_libraries = ["Django","Flask","Numpy","Matplotlib","Pandas"]
formated_string = "The following are python libraries:%s" %(python_libraries)
print(formated_string)

first_name = "Asabeneh"
last_name = "Yetayeh"
language = "Python"
formated_string = "I'm {} {}. I teach {}".format(first_name,last_name,language)
print(formated_string)

a = 4
b = 3
print("{} + {} = {}".format(a,b,a+b))
print("{} - {} = {}".format(a,b,a-b))
print("{} * {} = {}".format(a,b,a*b))
print("{} / {} = {}".format(a,b,a/b))
print("{} // {} = {}".format(a,b,a//b))
print("{} ** {} = {}".format(a,b,a**b))

radius = 10
pi = 3.14
area = radius ** 2 * pi 
formted_string = "The area of a circle with a radius {} is {:.2f}.".format(radius,area)
print(formted_string)

a = 4
b = 3
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b:.2f}")
print(f"{a} % {b} = {a%b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} ** {b} = {a**b}")

language = "Python"
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

language = "Python"
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
last_letter = language[len(language) - 1]
print(last_letter)

last_letter = language[-1]
print(last_letter)
second_last = language[-2]
print(second_last)

first_three = language[0:3]
last_three = language[3:6]
print(first_three)
print(last_three)
last_three = language[3:]
print(last_three)
last_three = language[-3:]
print(last_three)

greeting = "Hello, World!"
print(greeting[::-1])

pto = language[0:6:2]
print(pto)

challenge = "thirty days of python"
print(challenge.capitalize())

print(challenge.count("y"))
print(challenge.count("th"))
print(challenge.count("y",7,14))

print(challenge.endswith("on"))
print(challenge.endswith("tion"))

challenge = "thirty\tdays\tpython"
print(challenge.expandtabs())
print(challenge.expandtabs(10))

print(challenge.find("y"))
print(challenge.rfind("y"))

challenge = "thirty days of python"
sub_string ="da"
print(challenge.index(sub_string))

print(challenge.rindex(sub_string))
print(challenge.rindex("on",8))

print(challenge.isalnum())
challenge = "30dayspython"
print(challenge.isalnum())
challenge = "thirtydaysofpython"
print(challenge.isalnum())

print(challenge.isalpha())
challenge = "30daysofpython"
print(challenge.isalpha())

challenge = "30daysofpython"
print(challenge.isdecimal())
print(challenge.isdigit())
challenge = "30"
print(challenge.isdecimal())
print(challenge.isdigit())

num ="10"
print(num.isnumeric())
num="10.5"
print(num.isnumeric())

challenge = "30daysofpython"
print(challenge.isidentifier())
challenge = "hihi_hehe"
print(challenge.isidentifier())

challenge = "30Daysofpython"
print(challenge.islower())
print(challenge.isupper())

challenge = "30daysofpython"
print(challenge.islower())
print(challenge.isupper())

web_tech = ["HTML","CSS","Java","React"]
result = " ".join(web_tech)
print(result)

web_tech = ["HTML","CSS","Java","React"]
result = "#".join(web_tech)
print(result)

challenge = "30daysofpython"
print(challenge.strip("n"))

challenge = "thirty days of python"
print(challenge.split())
challenge = "thirty, days, of, python"
print(challenge.split(","))

challenge = "thirty, days, of, python"
print(challenge.title())
print(challenge.swapcase())
print(challenge.startswith("thirty"))
print(challenge.startswith("30"))