def summation(num):
    total = 0
    
    for i in range(num+1):
        total += i
    return total
    
print(summation(6))