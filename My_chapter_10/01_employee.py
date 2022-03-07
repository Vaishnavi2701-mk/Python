class Programmer:
    company="Microsoft"
    role="SDE"

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def getInfo(self):
        print(f"The name fo an employee is {self.name} having a salry {self.salary} playing a role of {self.role} in the {self.company}")
    

employee1= Programmer("Vaishnavi", "200k")
employee2=Programmer("Mohit","100k")

employee1.getInfo()
employee2.getInfo()