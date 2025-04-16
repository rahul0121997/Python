d = {'id': 1, 'name': 'John', 'age': 30, 'city': 'New York'}
for key, value in d.items():
    print(key, value)
print(d['age'])  # Accessing a non-existent key
# print(d['country'])  # This will raise a KeyError
d['country'] = 'USA'  # Adding a new key-value pair
print(d)
print(d.keys())  # Getting all keys
print(d.values())  # Getting all values
print(d.items())  # Getting all key-value pairs
print('name' in d)  # Checking if a key exists
print('country' in d)  # Checking if a key exists
d.update({'city': 'Los Angeles', 'gender':'male'})  # Updating a value
print(d)
# print(d[0:2])  # Slicing the dictionary (not valid, will raise an error)
print(d['name'])  # Accessing a value using a key

del d['city']  # Removing a key-value pair
print(d)
print(d.pop('name'))  # Removing a key-value pair and returning its value
print(d)
print(d.pop('age'))  # Removing a key-value pair
print(d)
print(d.popitem())  # Removing the last inserted key-value pair
print(d)
print(d.clear())  # Clearing the dictionary
print(d)
print(type(d))  # Checking the type of the dictionary
print(d is None)  # Checking if the dictionary is None
print(d is not None)  # Checking if the dictionary is not None

# Nested dictionary
