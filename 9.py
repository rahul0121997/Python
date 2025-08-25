sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

d = {}


for k,v in sample_dict.items():
    if k == 'salary':
        d[k] = sample_dict[k]
    else:
        pass
print(d)