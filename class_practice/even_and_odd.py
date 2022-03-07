n=int(input("Enter the number\n"))

list=[]
even_list=[]
odd_list=[]


def list_of_numbers(num):
    for i in range (num):
        j=int(input("Enter the number\n"))

        list.append(j)
    
        if j%2==0:
            even_list.append(j)
    
        else:
            odd_list.append(j)

    print(f"\n1]The list of given numbers is {list}")
    print(f"\n2]The list of even numbers is {even_list}")
    print(f"\n3]The list of odd numbers is {odd_list}")


result=list_of_numbers(n)


