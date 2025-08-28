# print all prime number in given interval
def prime_number(num):
    l1 = []
    if num == 0 or num == 1:
        return False
    if num == 2 or num == 3:
        return True
    
    for i in range(2,int(num**0.5) + 1):
        if num % i == 0:
            return False
        else:
            l1.append(i)
            return True
    return l1        

x = 2
y = 7

l = []

for i in range(x,y):
    res = prime_number(i)
    l.append(res)
    
print(l)
    