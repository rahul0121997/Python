students = [
    {'name': 'A', 'marks': {'math': 80, 'science': 70}},
    {'name': 'B', 'marks': {'math': 90, 'science': 60}},
    {'name': 'C', 'marks': {'math': 70, 'science': 80}},
]

l1 = []
l2 = []

for i in students:
    math_marks = i['marks']['math']
    science_marks = i['marks']['science']
    l2.append(science_marks)
    l1.append(math_marks)
    
res = sum(l1)/ len(l1)
res1 = sum(l2)/len(l2)

print(res1)
print(res)


