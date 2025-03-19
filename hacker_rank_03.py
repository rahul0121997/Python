# if __name__ == '__main__':
#     result = []
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         result .append([name,score])

#     # new_score = sorted(set([score for name, score in result]))#score for name, score in students 
#     #is valid and used when you have a list of lists (or tuples) where each inner list has two elements


#     for new_result in result:
#         for item in new_result:
#             # print(item, end = " ")

#     new_item = sorted(map(lambda x: x[0], result))
#        print(new_item)
#     # print(new_score)


if __name__ == '__main__':
    result = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        result.append([name, score])
    
    # Get all the unique scores and sort them
    unique_scores = sorted(set(map(lambda x : x[1],result)))
    
    # Find the second lowest score
    second_lowest_score = unique_scores[1]
    
    # Get names of students with the second lowest score
    second_lowest_students = [x[0] for x in result if x[1] == second_lowest_score]
    
    # Sort these names alphabetically
    second_lowest_students.sort()
    
    # Print each name on a new line
    for name in second_lowest_students:
        print(name, end = " ")