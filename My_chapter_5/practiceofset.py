#s={}
#print(type(s))   **It will give a type as dictionary
#empty set
#s=set()
#print(type(s))     ** Now this is called as empty set

#s.add(4)      #** we can add the values such that but repeated values dont print
#s.add(6)
#s.add(5)
#s.add(5)
#s.add(4)
#print(s)
#s.add([2,4,8])                      ** we can't add list in sets because it changable(unhashable) and our set cannot be changed
#s.add({"vaishnavi":"Daughter"})     ** we cannot add dictionary beacuse it is also changable
#s.add((3,6,8))                      #** we  can add tuple because it is also unchangable               
#Methods
 
#print(len(s))                        ** it will give the no. of elements in the set, considering complete tuple as 1
#s.remove(6)                          ** remove the number inside the parenthisis
#s.pop()                              ** it will remove random element because it is unindexed
#s.clear()                            ** it will clear whole set
#s.union({9,7})                      
s={(5,9,3),7,3,4,5}
#print(s.union({4,5,8}))
print(s.intersection({4,8,23,3}))
