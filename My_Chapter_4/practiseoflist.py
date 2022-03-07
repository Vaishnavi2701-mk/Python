'''l=["vaishnavi",34,78.45,"mango"]
l[2]=45.78
print(l)'''
l1=[3,9,65,83,8,23,94]
l1.sort()
print(l1)
l1.reverse()
print(l1)
l1.append(100)
print(l1)
l1.insert(4,67)
print(l1)
l1.pop(5)
print(l1)
l1.remove(83)
print(l1)

#eg
#print(l1.sort())       **It will give error, thus we have to sort first and then print the list** but some methods can be done in this way in the string.
#l1_sortit=l1.sort()    ** It will also give an error , because we are sorting l1,so how could we print l1_sortit,such types of printing may be valid in string"
#print(l1_sortit)