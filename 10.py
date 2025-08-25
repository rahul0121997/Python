l  = [66,77,88,99,95]

for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i] > l[j]:
            l[i],l[j] = l[j],l[i]
        
print(l[0])
print(l[-1])