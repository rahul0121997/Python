from functools import reduce

l = [2, 5, 6, 7]

result = reduce(lambda x, y: x * y , l)
print(result)