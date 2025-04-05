# Practical Example 3: Write a Python program to find a specific string in the list using a simple
# for loop and if condition

l = ["prithvi", "ajay", "sunil", "america"]

name = "prithvi"
for value in l:
    if name in l:
        print(f"yes and the string is: {name}")
        print(type(name))
        # l.remove(value)
        break
    else:
        print(f"no i do not have {name} string ")
        break