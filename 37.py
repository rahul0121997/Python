from collections import defaultdict, Counter

d1 = {'a': 3, 'b': 2}
d2 = {'a': 1, 'c': 4}

merged = defaultdict(int)

for k,v in d1.items():
     for k1 , v1 in d2.items():
         if k == k1:
            d1[k] = v + v1      
             
d2.update(d1)
print(d2)

for k, v in d1.items():
    merged[k] += v

for k, v in d2.items():
    merged[k] += v

print(dict(merged))


c1 = Counter(d1)
c2 = Counter(d2)


print(c1 + c2)