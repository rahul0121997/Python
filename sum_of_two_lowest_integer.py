def sum_two_smallest_numbers(numbers):
    res = sorted(numbers)
    return res[0] + res[1]

print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))