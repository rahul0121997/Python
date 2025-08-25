#nested dictonary
data = {'person': {'name': 'Alice', 'age': 30}}

for keys, values in data.items():
    for k,v in values.items():
        print(f"{v} {k} is {v}")