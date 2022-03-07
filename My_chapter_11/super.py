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
    
    def takeBreath(self):

        super().takeBreath()
        print("I am an Employee and I am Breathing!")

class Programmer(Employee):
    company="Uber"

    def takeBreath(self):

        super().takeBreath()      # this will execute the method of upper class with their own!

        print("I am breathing c++")

    def getSalary(self):
        super().getSalary()
        print(" No salary to the Programmer!") 


pr=Programmer()
pr.takeBreath()
pr.getSalary()