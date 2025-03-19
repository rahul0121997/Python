name = input("enter student name : ")
rno = int(input("enter the students Roll Number: "))
marks1 = float(input("enter student marks 1: "))
marks2 = float(input("enter student marks 2: "))
marks3 = float(input("enter student marks 3: "))


sum = marks1 + marks2 + marks3
per = sum / 3
print(per)
print(sum)

if per >= 70:
    print("distinction class")

elif per >= 60:
    print("first class")

elif per >= 50:
    print("second class")

else:
    print("pass class")