d = {'a': 1, 'b': 2}
# Output: {1: 'a', 2: 'b'}

d1 = {}

for k, v in d.items():
    d1[v] = k

print(d1)