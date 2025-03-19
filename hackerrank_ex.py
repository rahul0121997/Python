# def is_leap(year):
#     leap = False
#     if(year % 400 == 0):
#         return True
#     elif(year % 100 == 0):
#         return False
#     elif(year % 4 == 0):
#         return True
#     return leap

# year = int(input())
# print(is_leap(year))


# if __name__ == '__main__':
#     n = int(input())
#     for i in range(1,n+1):

# list1 = [89,90,78,93,80]
# list2 = [90,91,85,88,86]
# list3 = [91,92,83,89,90.5]


# a = zip(list1, list2 , list3)

# for x,y,z in (a):
#     average = (x + y + z) / 3
#     print(average)

# Read the number of students and subjects
# No need to import anything for this task
# Read the number of students and subjects
n,m = map(int, input().split())

# Initialize a list to store marks for each subject
marks = []

# Read marks for each subject
for _ in range(m):
    subject_marks = list(map(float, input().split()))
    marks.append(subject_marks)

# Transpose the marks so that we group by student using zip
transposed_marks = zip(*marks)

# For each student's marks, calculate the average
for student_marks in transposed_marks:
    average = sum(student_marks) / m
    print(f"{average:.1f}")
