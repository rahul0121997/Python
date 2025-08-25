n = 10
char = 106  # ASCII for 'E'

# Upper half
for i in range(1, n + 1, 2):
    spaces = (n - i)
    print("-" * spaces, end="")

    for j in range(i):
        print(chr(char), end="")
        if j != i - 1:
            print("-", end="")
        char -= 1

    print("-" * spaces)
    char = 69  # reset

# Lower half
for i in range(n - 2, 0, -2):
    spaces = (n - i)
    print("-" * spaces, end="")

    for j in range(i):
        print(chr(char), end="")
        if j != i - 1:
            print("-", end="")
        char -= 1

    print("-" * spaces)
    char = 69  # reset
