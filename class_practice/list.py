l=[1,1,2,3,5,3,4,2,6,2,5,8,9,2]
d={}

for i in range(0,len(l)):
    d[i]=l.count(i)

print(d)