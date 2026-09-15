lst = []
print(lst)

lst =[1,2,3,4,5,6]
print(lst)
print(len(lst))
print(lst[0],lst[2],lst[-1])

mixed_data_types = ["Tung\n19\n1.78\nSingle\nHanoi"]
print(mixed_data_types[0])

it_companies = ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
print(it_companies)
print(len(it_companies))

first_company = it_companies[0]
middle_company = it_companies[len(it_companies) // 2]
last_company = it_companies[-1]

print(first_company)
print(middle_company)
print(last_company)

it_companies[2] = "Toyota"
print(it_companies)

it_companies.append("Microsoft")
print(it_companies)

it_companies.insert(3,"Xiaomi")
print(it_companies)

it_companies[1] = it_companies[1].upper()
print(it_companies)

it_companies = "#".join(it_companies)
print(it_companies)

does_exit = "Facebook" in it_companies
print(does_exit)

it_companies = ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
it_companies.sort()
print(it_companies)
it_companies = ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
it_companies.sort(reverse=True)
print(it_companies)

it_companies = ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
it_companies.remove("Facebook")
it_companies.remove("Google")
it_companies.remove("Microsoft")
print(it_companies)

it_companies = ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
del it_companies[-1]
del it_companies[-2]
del it_companies[-3]
print(it_companies)

it_companies = ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
middle_company = len(it_companies) // 2
del it_companies[middle_company]
print(it_companies)

del it_companies[0]
print(it_companies)

del it_companies[-1]
print(it_companies)

it_companies.clear()
print(it_companies)
del it_companies

front_end = ["HTML","CSS","JS","React","Redux"]
back_end = ["Node","Express","MongoDB"]

fullstack = front_end + back_end
fullstack.insert(5,"Python")
fullstack.insert(6,"SQL")
print(fullstack)

ages = [19,22,19,24,20,25,26,24,25,24]
ages.sort()
print(ages[0],ages[len(ages)-1])
middle_ages = len(ages) // 2
print(ages[middle_ages])
tong = sum(ages)
avg_ages = tong/len(ages)
print(avg_ages)
chenhlech = ages[-1] - ages[0]
print(chenhlech)
min_ages=min(ages)
max_ages=max(ages)
diff_min = abs(min_ages - avg_ages)
diff_max = abs(max_ages-avg_ages)
print(diff_min,diff_max)

