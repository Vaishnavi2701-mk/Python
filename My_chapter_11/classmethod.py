#class Employee:
#    company = "Camel"
#    salary = 100
#    location = "Delhi"
#
#    # def changeSalary(self, sal):
#    #     self.__class__.salary = sal
#
#    @classmethod
#    def changeSalary(cls, sal):
#        cls.salary = sal
#
#e = Employee()
#print(e.salary)
#e.changeSalary(200)
#print(e.salary)
#print(Employee.salary)
#
##Employee.salary="500k"
##print(Employee.salary)


class Employee():
    salary="200k"

    @classmethod


    def changeSalary(cls,val):
        cls.salary=val




e=Employee()
#Employee.salary='100k'
print(e.salary)
e.changeSalary(490)
print(e.salary)
print(Employee.salary)