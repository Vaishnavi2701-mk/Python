class Employee:
    company="Google"

    def getDetails(self):
        print("This is an employee!")

class Programmer(Employee):
    language= "Python" 

    def getLanguage(self):
        print(f"This is a {self.language}")

#e=Employee()
#e.getDetails()    # this one is method so we should have to run it without print#
#e.getLanguage()  # this one is parent class so it doesnt have that attribute
#e=Programmer()
#e.getDetails()
#e.getLanguage()


e=Employee()
e.getDetails()
p=Programmer()
p.getLanguage()
p.getDetails()
