class Calculator:

    def __init__(self,num):
        self.num=num

    #def square(self):
    #    print(f" The square of {self.num} is {self.num**2}")
#
    #def squareRoot(self):
    #    print(f" The squareroot of a {self.num} is {self.num**0.5}")
#
    #def cube(self):
    #    print(f" The cube of {self.num} is {self.num**3}")      


    def calculation(self):
        print(f"The square, squareroot and the cube of the {self.num} are {self.num**2}, {self.num**0.5} and {self.num**3} respectively.")

number=Calculator(4)
number.calculation()