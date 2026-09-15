nums = [-4,-3,-2,-1,0,2,4,6]
negative_number = [i for i in nums if i <= 0]
print(negative_number)

list_of_lists = [[1,2,3],[4,5,6],[7,8,9]]
flatten_list = [i for row in list_of_lists for i in row]
print(flatten_list)

new_list = [(i,1,i**1,i**2,i**3,i**4,i**5) for i in range(11)]
print(new_list)

new_list = [(i,1,i**1,i**2,i**3,i**4) for i in range(5)]
print(new_list)

countries = [[("Finland","Helsinki")],[("Sweden","Stockholm")],[("Norway","Oslo")]]
flatten_list = [[country[0][0].upper(),country[0][0][:3],country[0][1].upper()] for country in countries]
print(flatten_list)

countries = [[("Finland","Helsinki")],[("Sweden","Stockholm")],[("Norway","Oslo")]]
result = [{"country":country[0][0].upper(), "city": country[0][1].upper()} for country in countries]
print(result)

names = [[("Asabeneh","Yetayeh")],[("David","Smith")],[("Donald","Trump")],[("Bill","Gates")]]
result = [f"{name[0][0]} {name[0][1]}" for name in names]
print(result)

slope = lambda x1,y1,x2,y2: (y2 - y1) / (x2 -x1)
y_intercept = lambda x,y,m : y -m * x
print("He so goc m:",slope(1,2,3,6))
print("Tung do goc b:",y_intercept(1,2,2))