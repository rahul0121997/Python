import time
def decor(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"the function execuation time - start : {time.time():.4f}sec")
        return result
    return wrapper

@decor
def my_func():
    time.sleep(1)
    print('Done')
    
print(my_func())