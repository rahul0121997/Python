s = "aabbcdeff"

d = {}

for i in s:
    d[i] = d.get(i, 0) + 1

print(d)

for k,v in d.items():
    if v == 1:
        print(k,v)
        break