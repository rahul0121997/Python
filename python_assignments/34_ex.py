# Two lists
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]

# Merge using a loop
merged_dict = {}
for i in range(len(keys)):
    merged_dict[keys[i]] = values[i]

# Display result
print("Merged Dictionary:", merged_dict)
