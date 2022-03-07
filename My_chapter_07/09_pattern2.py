n=int(input("Enter the number\n"))
for i in range(n+1):
    print(" "*((n+1)-i), end=" ")
    print("*"*(2*i-1), end=" ")
    print(" "*((n+1)-i))

