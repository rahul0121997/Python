d = {'a': 10, 'b': 25, 'c': 5, 'd': 40}


res = {k:v for k ,v in d.items() if v > 20}
print(res)