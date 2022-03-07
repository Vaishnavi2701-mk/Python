names=["vaishnavi", "rupal", "sanika", "nikita", "rinku"]
 
print("your options are",names[0:])

name=input("Enter the name\n")

if(name in names):
    print(str(name)+" is present in the list")
else:
    print(str(name)+ " is not present in the list")    
