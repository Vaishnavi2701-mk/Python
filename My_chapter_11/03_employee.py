class Employee:
    salary= 2000
    increment=1.5


    @property

    def salaryAfterIncreament(self):
        return self.salary*self.increment

    @salaryAfterIncreament.setter
    def salaryAfterIncreament(self,val):
        self.increament=val/self.salary


e=Employee()
print(e.salaryAfterIncreament)
print(e.increment)
e.salaryAfterIncreament=4500
print(e.increment)
