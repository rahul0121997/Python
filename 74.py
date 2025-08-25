def count_up_to(n):
    for i in range(1, n+1):
        yield i

print(list(count_up_to(17)))