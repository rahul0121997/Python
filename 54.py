def is_prime(num):
    if num <= 1:
        return False
    for i in range(2,int(num **0.5)+1):
        if num % 2 ==0:
            return False
        else:
            return True
        
res= is_prime(29)
print(res)
    