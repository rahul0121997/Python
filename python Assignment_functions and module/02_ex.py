l = ['apple', 'banana', 'cherry',23, 45, 67,'true', False, None, [1,2,3], {'a':1, 'b':2}]

l.append('orange')
l.append(100)
print(l)
l.insert(3, 'kiwi')
print(l)
l.pop(10)
del l[3:6]
l.remove('banana')
print(l)