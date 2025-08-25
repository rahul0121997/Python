first = ['John', 'Jane']
last = ['Doe', 'Smith']

res = list(map(lambda fl:(fl[0] + " " + fl[1]), zip(first, last)))
print(res)