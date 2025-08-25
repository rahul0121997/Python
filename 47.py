nested = [[1, 2], [3, 4], [5, 6]]

l = []

for i in nested:
    for j in i:
        l.append(j)
        
print(l)