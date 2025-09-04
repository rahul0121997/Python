a = [10, 20, 4, 45, 99]

# a.sort()
# print(a)

for i in range(len(a)):
    for j in range((len(a))):
        if a[i] < a[j]:
            a[i],a[j] = a[j],a[i]

print(a)