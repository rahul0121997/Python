#Practical Example 7: Write a Python program to calculate grades based on percentage using
# if-else ladder.
marks = int(input("enter tour marks: "))
marks1 = int(input("enter tour marks: "))
marks2 = int(input("enter tour marks: "))
marks3 = int(input("enter tour marks: "))

sum = marks + marks1 + marks2 + marks3
print(f"you got {sum} out of {(4 * 100)}")
percentage = sum / 4

if percentage >= 90:
    print("GRADE A+")

elif  percentage < 90 and percentage >= 70:
    print("GRADE A")

elif percentage < 70 and percentage >= 60:
    print("GRADE B")

elif percentage < 60 and percentage >= 45:
    print("GREADE PASSS CLASS") 

else:
    print("SORRY YOU FAILED!! TRY NEXT YEAR")

