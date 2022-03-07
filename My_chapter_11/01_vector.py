class C2d:

     def __init__(self,i,j):
            self.icap=i
            self.jcap=j
     

     def __str__(self):
         return(f"{self.icap}i + {self.jcap}j")

class C3d(C2d):

    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.kcap=k

    def __str__(self):
        return (f"{self.icap}i + {self.jcap}j + {self.kcap}k")




v1=C2d(4,3)
v2=C3d(3,6,7)
print(v1)
print(v2)