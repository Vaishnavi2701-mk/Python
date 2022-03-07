class Employee:
    company="microsoft"
    name="harry"
    salary="100k"
    role="SDE"
    allowence="Food"

    def getDetais(self):  #self class and object attribute leta hai
        print(f"The name of an employee is {self.name} having a salary {self.salary} playing a role of {self.role} working in the company {self.company} having an allowence of  {self.allowence}")
    
    @staticmethod   # When I dont want to pass an object,just like here I only wanted to print greeting but self ke bina leta nahi,then we use @staticmethod
    def greet():
        print("Hello mam, a very Good Morning to you!")    

    def __init__(self,name,salary,role,company) :
        self.name=name
        self.salary=salary
        self.role=role
        self.company=company
          


vaishnavi=Employee("Vaishnavi","100k","SDE","Microsoft")
#vaishnavi=Employee()
#
#vaishnavi.company="Amazon"   # *** in this case vaishnavi is taken as self and all the attributes corresponding to this object vaishnavi will be printed by using self
#vaishnavi.name="vaishu"
#vaishnavi.salary="200k"

#print(vaishnavi.name)
#print(vaishnavi.company)
#print(vaishnavi.salary)

vaishnavi.getDetais()
vaishnavi.greet()