l = [1,23,3,4,5]
l1 = ['rahul','prithvi','ajay','sunil']

d = {v: k for k, v in zip(l,l1)}
print(d)

d1 = {}

for k,v in zip(l,l1):
    print(v,k)
    d1[v] = k
    
print(d1)