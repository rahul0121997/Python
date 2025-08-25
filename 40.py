from collections import defaultdict
data = {
    'doc1': ['apple', 'banana', 'orange'],
    'doc2': ['banana', 'kiwi'],
    'doc3': ['apple', 'kiwi']
}

d = defaultdict(list)

for k,v in data.items():
    for i in v:
        d[i].append(k)

print(d)
        