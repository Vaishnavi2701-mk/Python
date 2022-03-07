num=int(input("Enter the number\n"))

l1=[num*i for i in range(1,11)]

print(l1)


with open("table.txt","a") as f:
    f.write(str(l1))
    f.write("\n")