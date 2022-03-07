sub1=int(input("Enter the marks of subject 1\n"))
sub2=int(input("Enter the marks of subject 2\n"))
sub3=int(input("Enter the marks of subject 3\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail!")
if((sub1+sub2+sub3)/300*100)<40:
    print("you are fail !")
else:
     print("You are pass!")    


#sub1=int(input("Enter the marks of subject 1\n"))
#sub2=int(input("Enter the marks of subject 2\n"))
#sub3=int(input("Enter the marks of subject 3\n"))
#
#if(sub1>33 and sub2>33 and sub3>33):
#    if(((sub1+sub2+sub3)/300*100)>40):
#        print("You are pass!")
#    else:
#        print("You are fail!")
#else:
#    print("You are fail!")  