course1=int(input("Enter marks of course 1\n"))
course2=int(input("Enter marks of course 2\n"))
course3=int(input("Enter marks of course 3\n"))
course4=int(input("Enter marks of course 4\n"))
course5=int(input("Enter marks of course 5\n"))

score=((course1+course2+course3+course4+course5)/500)*100

print("\n*****STUDENT'S RESULT*****\n")

print(f"Your marks are:\ncourse 1= {course1}\ncourse 2= {course2}\ncourse 3= {course3}\ncourse 4= {course4}\ncourse 5= {course5}")
print("----------------")
print(f"Total = {score}")


if (course1>=40 and course2>=40 and course3>=40 and course4>=40 and course5>=40):


    if score>=75:
        print("\nResult: Congartulations ,you are Pass!\nYour grade is Distinction")

    elif score>=60 and score<75:
        print("\nResult: Congratulations, you are Pass!\nYour Grade is First Division")
    elif score>=50 and score<60:
        print("\nResult: Congratulations, you are Pass!\nYour Grade is Second Division")
    elif score>=40 and score<50:
        print("\nResult: Congratulations, you are Pass!\nYour Grade is Third Division")
    else:
        print("\nResult: You are Fail!")   
    


else:
    print("\nYou are Fail!")


