class Programmer:
    company="Microsoft"

    def __init__(self,name,subunit):
        self.name=name
        self.subunit=subunit

    def getInfo(self):
        print(f"The name of an employee is {self.name} and his/her role is {self.subunit}")

a=Programmer("Vaishnavi","SDE")
b=Programmer("Anshika","Web Developer")

a.getInfo()
b.getInfo()