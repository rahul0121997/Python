# list of strings
a = ['GeeksforGeeks', 'is', 'Best', 'For', 'Geeks', 'And', 'Computer Science']

# list of word replacements 
b = [['Geeks', 'Gks'], ['And', '&'], ['Computer', 'Comp']]

d = dict(b)

for k,v in d.items():
    for i in range(len(a)):
        if k in a[i]:
            a[i] = a[i].replace(k,v)

print(a)