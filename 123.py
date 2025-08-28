# fibonacci series

def fibo(num):
    if num == 0 or num == 1:
        return num
    return fibo(num - 1) + fibo(num - 2)


for i in range(10):
    print(fibo(i))