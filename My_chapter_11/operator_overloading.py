class Number():
    def __init__(self, num):
        self.num=num
    def __add__(self, num2):
        print("Lets add!!")

        return self.num+num2.num

    def __mul__(self,num2):
        print("Lets Multiply!!")    

        return self.num*num2.num

    def __str__(self):
        return (f"Decimal number {self.num}")

    def __len__(self):
        return 2
       

n1=Number(4)
n2=Number(45)
sum=n1+n2
print(sum)
multi=n1*n2
print(multi)
print(n2)
print(len(n1))
