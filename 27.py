l = [1, 2, 3, 2, 4]

rem = 2
for i in l:
    if rem == i:
        l.remove(i)

print(l)