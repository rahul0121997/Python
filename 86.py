# alphabet triangle


n = 5
char = 65

# for i in range(1,n+1):
#     print(chr(char) * i)
#     char += 1

for i in range(1, n + 1):
    print(" " * (n - i) + chr(char) * (2 * i -1))
    char += 1