list=[]
N=int(input("Enter the number\n"))

for i in range(N):
    num=int(input("Enter the element\n"))
    list.append(num)

print(f"\n Your list is\n {list}")

avg=(sum(list))/N

print(f"\nThe maximum of list is: ",max(list))
print(f"\nThe minimum of list is: ",min(list))
print(f"\nThr sum of list is: ",sum(list))
print(f"\nThe average of the elements in list is: ",avg)