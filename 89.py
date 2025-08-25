l = [2,5,9,11,15,7]

target = 9

d = []

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[j] == target - l[i]:
            d.append([l[i],i])
            d.append([l[j],j])

print(d)