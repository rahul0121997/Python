from collections import defaultdict
n,m = list(map(int,input("enter the two number: ").split()))

b = []
a = []
for i in range(n):
    A = input("enter the value: ")
    a.append(A)
for i in range(m):
    B = input("enter the value: ")
    b.append(B)

d = defaultdict(list)

for index,value in enumerate(a):
    d[value].append(index)

print(d)

print(a)
print(b)