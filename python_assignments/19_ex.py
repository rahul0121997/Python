# Practical Example 1: Skip 'banana' in a list using continue statement
# Practical Example 2: Stop the loop once 'banana' is found using break statement
l = ["apple", "banana", "orange"]

# for fruit in l:
#     if fruit == "banana":
#         continue
#     print(fruit)


for fruit in l:
    if fruit == "banana":
        break

    print(fruit)
    