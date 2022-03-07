try:
    a=int(input("Enter the number\n "))

    b=25/a

    print(b)

except Exception as e:
    print(f"The error is generated as {e}")


else:
    print("We are succesfull!")