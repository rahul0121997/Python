from collections import Counter
s1 = "geeks" 
s2 = "kseeg"

s4 = Counter(s1)
s3 = Counter(s2)

if len(s1) == len(s2) and s3 == s4:
    print("yes")
else:
    print("no")
        
