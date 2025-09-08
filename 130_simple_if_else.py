def love(n,m):
    if n % 2 == 0 and m % 2 != 0 or n % 2 != 0 and m % 2 == 0:
        return True
    else:
        return False
        
n = int(input("enter the number greate than 0: "))
m = int(input("enter the number greate than 0: "))

print(love(n,m))