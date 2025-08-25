l = [1, 2, 2, 3, 4, 4, 5]
# remove duplicates
l1 = []
for i in l:
    if i not in l1:
        l1.append(i)
        
print(l1)
