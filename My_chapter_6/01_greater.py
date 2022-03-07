a=int(input("Enter the first number \n"))
b=int(input("Enter the second number\n "))
c=int(input("Enter the third number \n  "))
d=int(input("Enter the fourth number\n "))

#if(a>d):
#    great=a
#else:
#    great=d    
#if(b>c):
#    great2=b
#else:
#    great2=c
#
#if(great>great2):
#    print(str(great) +" is the greatest number")
#else:
#    print(str(great2) +" is the greatest number")    

if(a>b and a>c and a>d):
    print(str(a) + " is the greatest number")
elif(b>c and b>a and b>d):
    print(str(b) + " is the greatest number")
elif(c>a and c>b and c>d):
    print(str(c) + " is the greatest number")
else:
    print(str(d) + " is the greatest number")        
