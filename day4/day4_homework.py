result = " ".join(["Thirty","Days","Of","Python"])
print(result)

result =" ".join(["Coding","For","All"])
print(result)

company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
company = "Coding For All"
result =" ".join(company[7:].split())
print(result)
print(company.find("Coding"))
print(company.replace("Coding","Python"))

result = "Python For Everyone"
print(result.replace("Python For Everyone","Python for All"))

company = "Coding For All"
print(company.split())

result = "Facebook,Google,Microsoft,Apple,IBM,Oracle,Amazon"
print(" ".join(result.split(",")))

company = "Coding For All"
print(company[0])
print(len(company)-1)
print(company[10])

result = "Python For Everyone"
print(result[0] +result[7]+result[11])

company = "Coding For All"
print(company[0] + company[7] + company[11])
print(company.find("C"))
print(company.find("F"))

company = "Coding For All People"
print(company.rfind("l"))

result = "You cannot end a sentence with because because because is a conjunction"
print(result.index("because"))
print(result.find("because"))
print(result.rindex("because"))
print(result.split("because"))

company = "Coding For All"
print(company.startswith("Coding"))
print(company.endswith("Coding"))
print(company.strip())

result ="30DaysOfPython"
print(result.isidentifier())
result = "thirdty_days_of_python"
print(result.isidentifier())

result = ["Django","Flask","Bottle","Pyramid","Falcon"]
print(" ".join(result))

result = "I am enjoying this challenge.\nI just wonder what is next."
print(result)

result = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(result)

radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {:.0f} meters square.".format(radius,area))

a = 8
b = 6
print("{} + {} = {}".format(a,b,a+b))
print("{} - {} = {}".format(a,b,a-b))
print("{} * {} = {}".format(a,b,a*b))
print("{} / {} = {:.2f}".format(a,b,a/b))
print("{} % {} = {}".format(a,b,a%b))
print("{} // {} = {}".format(a,b,a//b))
print("{} ** {} = {}".format(a,b,a**b))