data = [('A', 1), ('B', 2), ('A', 3), ('B', 4)]

d = {}

for keys, value in data:
    d.setdefault(keys, []).append(value)
    
print(d)