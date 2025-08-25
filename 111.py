n = 5
char = 65
for i in range(n):
    print(" " * (n - i))
    for j in range(i+1):
        print(chr(char), end= " ")
        char += 1
    
    
