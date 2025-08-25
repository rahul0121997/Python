nums = [1, 2, 3, 4, 5]

res= list(map(lambda x: x**2,filter(lambda x : x % 2 ==0,nums)))
print(res)