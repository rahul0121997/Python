l = ['apple', 'banana', 'cherry',23, 45, 67,'true', False, None, [1,2,3], {'a':1, 'b':2}]
for i in l:
    print(i, type(i))
l1 = list(filter(lambda x: isinstance(x, (int, float)), l))
print(l1)
l2 = list(filter(lambda x: isinstance(x, str), l)) 
print(l2)
l3 = sorted(l1, reverse=True)
print(l3)
l4 = sorted(l2, reverse=True)
print(l4)
l6 = [34,65,66,23,45,67,89,12,34,56,78]
l6.sort()
print(l6)
l7 =[]
for i in l6:l7.insert(0, i)
print(l7)
for i in l6:
    l7.append(i)
print(l7)
s = set(l7)
print(s)