a=int(input("Enter the number\n"))
b=int(input("Enter the number\n"))


try:
    print(a/b)

except ZeroDivisionError:
    print("Infinite")

finally:
    print("ok done!")