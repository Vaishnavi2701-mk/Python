s=set()
s.add(20)
s.add("20")
s.add(20.00)
print(s)     
print(len(s))   # It will consider 20 and 20.00 as same thus two