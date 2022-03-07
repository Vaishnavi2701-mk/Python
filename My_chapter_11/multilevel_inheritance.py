class Person():
    country="India"
    city="Bhandara"

    def takeBreath(self):
        print("I am human being and thus I am breathing!")

class Employee(Person):
    company="Amazon"
    role="SDE"
    salary="200k"
    
    def getSalary(self):
        print(f"The salary is {self.salary}")
    
   # def takeBreath(self):
    #    print("I am an Employee and I am Breathing!")

class Programmer(Employee):
    company="Uber"

   # def takeBreath(self):
    #    print("I am breathing c++")

    def getSalary(self):
        print(" No salary to the Programmer!") 



#p=Person()
#p.takeBreath()
#e=Employee()
#e.takeBreath()
#e.getSalary()
pr=Programmer()
pr.takeBreath()
pr.getSalary()
           
