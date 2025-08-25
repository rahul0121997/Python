s = """i am great python backend developer having great knowldege in my sql database django and python"""

d = {}

for char in s :
    d[char] = d.get(char, 0)+1



print(d)