l = [9, 11, 2, 7]
target = 9
d = {}

for i, v in enumerate(l):
    num = target - v
    if num in d:
        print(f"Indices: {d[num]} and {i}")
        print(f"Values: {l[d[num]]} + {v} = {target}")
        break
    d[v] = i
