d={123:"vishal",456:"tirth",789:"nikunj",963:"yash"}

print(d)
print(d.get(123))
print(d.items())
print(d.keys())
print(d.values())
d.popitem()
print(d)

d1={110:"roy",220:"hiren"}
d.update(d1)
print(d)
for i in d:
    print(i," : ",d[i])
