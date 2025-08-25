from collections import Counter,defaultdict
lst = [1, 2, 3, 1, 2, 1, 4, 5]

d = {}

# c1 = Counter(lst)

# print(c1.most_common(1))

for i in lst:
    first_num = lst[0]
    d.setdefault(i,[]).append(i)

print(d)

d2 = defaultdict(list)

for index, values in enumerate(lst):
    d2[values].append(values)
    
print(d2)