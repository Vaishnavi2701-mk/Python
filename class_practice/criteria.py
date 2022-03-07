percentage=float(input("Enter the percentage\n"))
percentage10th=float(input("Enter the 12th percentage\n"))
percentage12th=float(input("Enter the 10th percentage\n"))
age=int(input("Enter your age\n"))

if percentage>=80:
    if percentage10th>=80:
        if percentage12th>=80:
            if age>=20:
                print("You are selected!")
            else:
                print("Sorry you are not eligible due to your age!")
        else:
            print("Sorry you are not eligible! your 12th marks doesn't fit for criteria!")     
    else:
        print("Sorry you are not eligible! your 10th marks doesn't fit for criteria!") 
else:
    print("Sorry you are not eligible! your percentage doesn't fit for criteria!")                      

