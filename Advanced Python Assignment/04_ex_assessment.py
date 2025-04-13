from functools import reduce
class Grade:
    def __init__(self):
        self.get_user_subject()
        
        
    
    def get_user_subject(self):
        print("***************************")
        print("WELCOME TO GRADE CALCULATOR")
        print("***************************")
        user_sub = int(input("Enter Your Subjects: "))
        user_total = user_sub * 100
        marks = []
        
        
        while user_sub > 0:
            user_marks = int(input("Enter Subject marks out of 100 :"))
            marks.append(user_marks)
            user_sub -= 1
        total_marks = reduce(lambda x, y : x + y, marks)
        print("***************************************")
        print(f"you got {total_marks}/{user_total} ")
        
        avg = total_marks * 100/ user_total
        print("***************************")
        
        if avg >= 90 :
            print(f"Your grade Is : A+")
        elif avg < 90 and avg >= 80:
            print(f"Your grade Is :A")
        elif avg < 80 and  avg >= 70:
            print(f"Your grade Is : B+")
        elif avg < 70 and avg >=60 :
            print("Your Grade Is : B")
        elif avg < 60 and avg >= 50:
            print("Your Grade Is : C")
        elif avg < 50 and avg >= 35:
            print("Your grade Is : pass")
        else:
            print("You Fail Try Again !!")
        
        
s = Grade()