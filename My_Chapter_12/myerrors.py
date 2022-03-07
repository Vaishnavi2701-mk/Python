try:
    a=int(input("Enter the number\n"))
    c=1/a
    print(c)

except ValueError:
    print("Please enter a valid value!")

except ZeroDivisionError:
    print("Make sure you are not dividing it by 0!")


print("Thnanks for using this code!")