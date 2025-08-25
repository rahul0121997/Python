words = ['bat', 'tab', 'tap', 'pat', 'apt']

l = []
d = {}
for substring in words:
    s = substring[::-1]
    if s in words:
        d[substring] = s
        l.append(s)
        
print(l)
print(d)