# Practical Example 4: Print this pattern using nested for loop:
# markdown
# Copy code
# *
# **
# ***
# ****
# *****

n = 5

# for i in range(1):
#     for j in range(n):
#         print("*" * j)
        

for i in range(1, n + 1):
    print("*" * i)