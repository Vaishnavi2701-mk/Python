num=int(input("Enter the number\n"))

def prime(n):
    prime=True
    for d in range(2,n):
        if(n%d==0):
            prime=False
    if (prime):
        return (f"c) The number {n} is a prime number\n ")
    else:
        return (f"c) The number {n} is not a prime number\n")
        
def greater(n):
    if n>3:
        return 1
    else:
        return 0

print("*********************")
print(f"Your number is {num}")
print("*********************\n")

print(f"a) Square root of {num} is : ",num**0.5, "\n")

print(f"b) Cube of {num} is :", num**3, "\n")

print(prime(num))

great_num=greater(num)

print("d)", great_num,"\n")

print(f"e) The type of number is: ",type(num))

num=float(num)
print(f"\nf) Conversion of number into float is: ",num)

