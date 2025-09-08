from collections import Counter
text = "apple banana apple orange banana apple"
d = {}
res = Counter(text) 

print(res)

l = text.split()

for k,v in enumerate(l):
    d[v] = d.get(v , 0) + 1

print(d)