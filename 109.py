def solution(number):
    total = 0
    for i in range(number):
        if i % 3 == 0  or i % 5 == 0 or i % 3 == 0 and i % 5 == 0 :
            total = total + i
    return total

print(solution(10))
  