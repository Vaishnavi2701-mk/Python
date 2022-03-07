#def percentage(marks):
#    return(sum(marks)/400*100)
#
#marks1=[89,67,80,92,90]
#percentage1=percentage(marks1)
#print(percentage1)
#marks2=[88,98,96,94,89]
#percentage2=percentage(marks2)
#print(percentage2)

#def greeting(name):
    #print("Hello,"+name)
#greeting("Vaishnavi")


#def mysum(num1,num2):
#    s=num1+num2
#    return s
#sum1=mysum(34,54)    
#print(sum1)

#def myname(name):     erroe dega
#def myname(name="stranger"):     # default argument
#    print("Hello, "+ name)       
#greet=myname()    
#print(greet)



#******Recursion******

#if I am printing a factorial of number by using function then it will be like;

#def factorial(n):
#    fact=1
#    for i in range(1,n):
#        fact=fact*(i+1)
#    return fact

#f=factorial(5)
#print(f)
#  but if Wanted to continue this with recursion

def recursive(n):
    if n==1 or n==0:
        return 1
    else:
        return n*recursive(n-1)    
f=recursive(5)
print(f)
