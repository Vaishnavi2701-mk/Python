##class People():
 #   def __int__(self,name):
 #       self.name=name
#
 #   def namePrint(self):
 #       print("Name:"+self.name)
#
#
# #erson1=People("Sally")
#erson2=People("Louise")
#erson1.namePrint()


class A():
    def __init__(self,count=100):
        self.count=count

obj1=A()
obj2=A(102)
print(obj1.count)
print(obj2.count)