d = {'one': 60, 'three': 20, 'thirteen': 60}

max_value = max(d.values())

l=[]

for k,v in d.items():
    if v == max_value:
        l.append(k)     
        result = max(l,key=len)

print(result,max_value)


