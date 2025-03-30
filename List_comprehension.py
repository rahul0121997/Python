# [expression for item in iterable if condition] syntax of creating  a list in concise way
# [expression for item in list if condition == True]
# if __name__ == "__main__":
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())

#     result = [
#         [i, j, k]
#         for i in range(x + 1)
#         for j in range(y + 1)
#         for k in range(z + 1)
#         if i + j + k != n
#     ]
#     print(result)


# squares = [[1,1],[2,4],[3,9],[4,16],[5,25]]
# squares = [x.append("10") or x for x in squares]
# [square.append(10) for square in squares]
# [square.extend([10]) for square in squares]

# print(squares)

#basics list comprehension

numbers = [1, 2, 3, 4, 5]
squares = [x - 1 for x in numbers]
print(squares)
# Result: [1, 4, 9, 16, 25]
#[0, 1, 2, 3, 4] (x -1)

#Conditional List Comprehension
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(even_squares)
# Result: [4, 16]

#multiple condition
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered = [x for x in numbers if x % 2 == 0 if x > 5]
print(filtered)
# Result: [6, 8, 10]

#if-else condition in list comprehension
numbers = [1, 2, 3, 4, 5]
parity = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(parity)
# Result: ['odd', 'even', 'odd', 'even', 'odd']


#nested list comprehension

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)
# Result: [1, 2, 3, 4, 5, 6, 7, 8, 9]

#creating a matrix using list comprehension

# Create a 3x3 matrix
matrix = [[i * 3 + j + 1 for j in range(3)] for i in range(3)]
print(matrix)
# Result: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#transforming a string using list comprehension

words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(upper_words)
# Result: ['HELLO', 'WORLD', 'PYTHON']

#working with dictonaries

prices = {"apple": 0.5, "banana": 0.25, "orange": 0.75}
fruit_prices = [f"{fruit}: ${price}" for fruit, price in prices.items()]
print(fruit_prices)
# Result: ['apple: $0.5', 'banana: $0.25', 'orange: $0.75']

#dictonaries comprehension

fruits = ["apple", "banana", "cherry"]
fruit_lengths = {fruit: len(fruit) for fruit in fruits}
print(fruit_lengths)
# Result: {'apple': 5, 'banana': 6, 'cherry': 6}

#set comprehension

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_squares = {x**2 for x in numbers} #{x for x in [1, 2, 2, 3, 4, 4, 5] if x % 2 == 0}
print(unique_squares)
# Result: {1, 4, 9, 16, 25}

#tuple unpacking copmrehension

coordinates = [(1, 2), (3, 4), (5, 6)]
sums = [x + y for x, y in coordinates]
print(sums)
# Result: [3, 7, 11]

#conditional value manipulation

numbers = [1, -2, 3, -4, 5]
absolute_values = [abs(x) for x in numbers]
print(absolute_values)
# Result: [1, 2, 3, 4, 5]

#filtering none values

values = [1, None, 3, None, 5]
filtered = [x for x in values if x is not None]
print(filtered)
# Result: [1, 3, 5]

#calling function in comprehension

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [x for x in range(2, 30) if is_prime(x)]
print(primes)
# Result: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

#combining with zip()

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
people = [f"{name} is {age} years old" for name, age in zip(names, ages)]
print(people)
# Result: ['Alice is 25 years old', 'Bob is 30 years old', 'Charlie is 35 years old']

#nested condition

numbers = [1, 2, 3, 4, 5]
categorized = ["small" if x < 3 else "medium" if x < 5 else "large" for x in numbers]
print(categorized)
# Result: ['small', 'small', 'medium', 'medium', 'large']

#generator comprehension
sum_of_squares = sum(x**2 for x in numbers)
print(sum_of_squares)

#list comprehension with multiple iterables
combinations = [(x, y) for x in [1, 2, 3] for y in ['a', 'b']]
print(combinations)