# if __name__ == '__main__':
#     result = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         result.append([name,score])
#         print(result)
    
#     new_result = sorted(result,key=lambda x:x[0])
#     print(new_result)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    if query_name == student_marks[name]:
        result = scores / n
        print(result)