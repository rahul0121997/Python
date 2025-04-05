from functools import reduce
# Write a Python program to apply the map() function to square a list of numbers.
l = [1, 2, 3, 4, 5, 6]
x = list(map(lambda x: x * x, l))
print(x)


# Write a Python program that uses reduce() to find the product of a list of numbers

l = [1, 2, 3, 4, 5, 6]
# L1 = "PYTHON"
x = reduce(lambda x , y : x * y , (l))
print(x)


# l2 = [1,1,2,32,32]
# l3 = [45, 65,34,232,]
# res = map(lambda x, y: x + y, l2,l3)
# print(list(res))

letters = ['a', 'b', 'c', 'e', 'i']
vowel = filter(lambda x:x in "aeiou", letters)
print(list(vowel))