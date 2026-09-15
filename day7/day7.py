st ={"item1","item2","item3","item4","item5"}
len(st)
print(st)
print("item1" in st)
st.add("item6")
print(st)
st.update(["item7","item8","item9"])
print(st)
st.remove("item7")
st.pop()
print(st)
st.clear()
print(st)

st ={"item1","item2","item3","item4","item5"}
del st

lst =["item1","item2","item3","item4","item5"]
st = set(lst)
print(st)

st1 = {"item1","item2","item3"}
st2 = {"item4","item5","item6"}
st3 = st1.union(st2)
print(st3)
st1 = {"item1","item2","item3"}
st2 = {"item2","item5","item6"}
st3 = st1.intersection(st2)
print(st3)
st1 = {"item1","item2","item3"}
st2 = {"item2","item5","item6"}
print(st2.issubset(st1))
print(st1.issubset(st2))
print(st2.symmetric_difference(st1))
print(st1.symmetric_difference(st2))
print(st2.isdisjoint(st1))