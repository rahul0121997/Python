# Write a Python program that filters out even numbers using the filter() function.
def is_even(num):
    res = filter(lambda x: x %2 == 0, num)
    print(list(res))

num = [1, 2, 3, 4 ,5, 24,25, 34, 67]
is_even(num)