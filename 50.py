from collections import Counter,defaultdict
data = {
    'doc1': ['apple', 'banana', 'orange'],
    'doc2': ['banana', 'kiwi'],
    'doc3': ['apple', 'kiwi']
}
# {'apple': 2, 'banana': 2, 'orange': 1, 'kiwi': 2}

d = defaultdict(set)

d1 = {}

for k,i in data.items():
    for j in set(i):
        d1[j] = d1.get(j,0)+1
        d[j].add(k)
print(d)
print(d1)