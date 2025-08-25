# Count Character Frequencies

string1 = 'Jessa'

d = {}

for char in string1:
    d[char] = d.get(char,0)+1

print(d)