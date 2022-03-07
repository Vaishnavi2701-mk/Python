# Reading a day from user and check whether it is saturday or sunday#

day=input("Enter a day\n")

if "Saturday"==day or "saturday"==day or "SATURDAY"==day:
    print(f"The day entered is {day}")   

elif "Sunday"==day or "sunday"==day or "SUNDAY"==day:
    print(f"The day entered is {day}")

else:
    print(" The day entered is not saturday or sunday!")