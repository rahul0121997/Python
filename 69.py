data = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 17}]

res= list(filter(lambda person: person['age'] >= 18, data))
print(res)