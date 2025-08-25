l = [['1', '4'], ['5', '6'], ['7', '10'],['2','1']]

s = []
for val in l:
    total = 0
    for digit in val:
        total = total + int(digit)
    s.append(total)
    
print(sorted(s))