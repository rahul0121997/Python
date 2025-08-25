l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]

res = 0
res1 = 0

for i in l1:
    res = res * 10 + i
    
    
for i in l2:
    res1 = res1 * 10 + i

l4 = str(res + res1)
print(list(l4[::-1]))
