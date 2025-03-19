def mutate_string(string, position, character):
    new = list(s)
    new[int(i)] = c
    s_new = "".join(new)
    return s_new

# Actually, string = list(string) and string = [string] are not the same in Python. Let me explain the difference:
# string = list(string) converts the string into a list of individual characters:

# If string = "abcd", then list(string) produces ['a', 'b', 'c', 'd']

# string = [string] creates a list containing the entire string as a single element:

# If string = "abcd", then [string] produces ["abcd"]
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

