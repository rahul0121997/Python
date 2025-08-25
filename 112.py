n = 123452654987
s = str(n)
l = []

for i in s:
    l.append(i)

for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] > l[j]:
            l[i],l[j] = l[j],l[i]

print(l)
l1 = "".join(l)
print(l1)


s1 = sorted(l)
print(s1)