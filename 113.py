# def persistance(num):
#     s = str(num)
#     total = 1
    
#     for i in s:
#         total *= int(i)
#     if len(str(total)) > 1:
#         total = persistance(str(total))
#         if total % 10 == 0:
#                 total = sum(total)
#     return total
    

# print(persistance(1234))
def persistence(num):
    if num < 10:
        return 0
    
    steps = 0
    while num >= 10:
        product = 1
        for digit in str(num):
            product *= int(digit)
        num = product
        steps += 1
    
    return steps

print(persistence(1234))  # Output: 3