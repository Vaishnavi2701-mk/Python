class Employee:
    company = "Bharat Gas"
    salary = 5600
    salarybonus = 400
    # totalSalary = 6100

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus = val - self.salary  # it will set my property

e = Employee()
print(e.totalSalary)
e.totalSalary = 5800   # if totalsalary is changing that means salarybonus is changing
#print(e.salary)
print(e.salarybonus)