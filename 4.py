dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

for k,v in dict2.items():
    dict1[k]= v

print(dict1)

res = dict1 | dict2 
print(res)