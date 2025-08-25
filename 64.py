keys = ['name', 'age']
values = ['Alice', 25]

    
res = {k:v for k,v in zip(keys,values)}
print(res)
    
data = dict(map(lambda kv:(kv[0],kv[1]), zip(keys, values)))
print(data)