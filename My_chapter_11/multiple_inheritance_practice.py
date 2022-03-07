class Freelancer():
    comapny="Microsoft"
    level=5

    def upgradeLevel(self):
        self.level=self.level+1
    
    
class Employee():
    company="Amazon"
    ecode="3462"


class Programmer(Employee,Freelancer):

    name='Vaishnavi'

p=Programmer()
p.upgradeLevel()
print(p.level)    # here level and ecode are not the attribute of programmer class but programmer class is the child of Employee and Freelancer class so it can use there attributes!
print(p.ecode)
print(p.company)  # it will print company(attribute of Employee because I write Employee first in the Programmer)
