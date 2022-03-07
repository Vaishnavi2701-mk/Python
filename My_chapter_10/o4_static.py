class Calculator:

    def __init__(self,num):
        self.num=num

    @staticmethod
    def greet():
        print("Hello !")
     


    def calculation(self):
        print(f"The square, squareroot and the cube of the {self.num} are {self.num**2}, {self.num**0.5} and {self.num**3} respectively.")

number=Calculator(4)
number.greet()
number.calculation()