lst = ['a', 'b', 'a']

print(lst.count('a'))

l = {}

for i in lst:
    l[i] = l.get(i,0)+1
print(l)