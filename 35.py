from collections import defaultdict

l = ['a', 'b', 'a', 'c', 'b']

d = {}

d1 = defaultdict(list)

for index ,values in enumerate(l):
    d1[values].append(index)
    
print(d1)

for index , values in enumerate(l):
    d.setdefault(values, []).append(index)

print(d)

