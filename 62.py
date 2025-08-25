a = ['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms']
b = 'Geek' # Substring

for i in range(len(a)):
    if b in a[i]:
        print("yes", a[i])