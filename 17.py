a = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3, None]


for i in a:
    print(i,a.count(i))
    
if None in a:
    print(a.count(None))