a = [10, 20, 30, 40, 50]

# def add(n):
#     return n + 2
# n + 2  == lambda x + 2 we directly use this using lambda so we don't need to create  function .

# result = list(map(add, a))
result = list(map(lambda x : x + 2, a))  # here we are using lambda function
print(result)
print(type(result))
for i in (result):
    print(i)