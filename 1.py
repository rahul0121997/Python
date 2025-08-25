my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}

my_dict['profession'] = 'Doctor'
my_dict['age'] = 40
print(my_dict['city'])
print(my_dict)
my_dict.pop('profession')
print(my_dict.items())
print(my_dict)

print(my_dict.get('name'))

if 'data' in my_dict:
    print('yes')
else:
    print('nothing in dictonary')

