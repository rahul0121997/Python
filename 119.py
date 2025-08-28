s = '153'

total = 0
for i in s:
    total += pow(int(i), len(s))

if str(total) == s:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
