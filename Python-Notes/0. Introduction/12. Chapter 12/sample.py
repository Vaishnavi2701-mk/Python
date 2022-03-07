from functools import reduce
sum=lambda a,b:a+b

f=[2,3,4,5]
val=reduce(sum,f)

print(val)