l = []
n= 10

for i in range(n):
    l.insert(i, i**2)

l.append(23)
l.pop()
l.remove(4)

print(l)