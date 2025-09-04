def square(num):
    total = ""
    for i in str(num):
        res = pow(int(i),2)
        total += str(res)
    return int(total)

print(square('0'))