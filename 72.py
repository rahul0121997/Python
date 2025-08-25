def gen():
    yield 1
    yield 2
    yield 3

print(tuple(gen()))

def rangee():
    for i in range(10):
        yield i
print(rangee)