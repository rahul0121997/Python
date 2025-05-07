
def is_prime(n):
    if  n<=1:
        return False
    if n ==2 or n==3:
        return True
    if n%2 == 0:
        return False
    
    for i in range(3,int(n**0.5)+1, 2):
        if n%i==0:
            return False
    return True

# res = is_prime(15)
# print(res)
count = []

for j in range(100):
    if is_prime(j) == True:
        count.append(j)
print(count)
print(len(count))
        
