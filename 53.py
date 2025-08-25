def decor(func):
    def wrapper(*args, **kwargs):
        print("function before the call")
        result = func(*args, **kwargs)
        print("function after call")
        return result
    return wrapper

@decor
def name(x,y):
    print("my name : Rahul")
    return x + y


print(name(2,4))
