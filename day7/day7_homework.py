it_companies = {"Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"}
A = {19,22,24,20,25,26}
B = {19,22,20,25,26,24,28,27}
age = [22,19,24,25,26,24,25,24]

print(len(it_companies))
it_companies.add("Twitter")
print(it_companies)
it_companies.update(["Linux","Window"])
print(it_companies)
it_companies.remove("Linux")
print(it_companies)
it_companies.discard("Linux") # ko bao loi
print(it_companies)
#it_companies.remove("Linux") # bao loi
#print(it_companies)

C = A.union(B)
print(C)
C = A.intersection(B)
print(C)
C = A.issubset(B)
print(C)
C = A.isdisjoint(B)
print(C)
C = A.symmetric_difference(B)
print(C)
del C

ages = set(age)
print(len(age) > len(ages))

sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.replace("."," ").split()
print(words)
print(len(words))