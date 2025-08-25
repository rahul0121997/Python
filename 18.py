a = [123, 456, 789]

# res = list(map(lambda val: sum(int(digit) for digit in str(val)), a))
# print(res)

l = []

for val in a:
    total = 0
    for digit in str(val):
        total = total + int(digit)
    l.append(total)
    
print(l)