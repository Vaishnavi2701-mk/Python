from typing import ForwardRef


class Train:

    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats

    def getStatus(self):
        print(f"The name of your train is {self.name} and with the available {self.seats} seats")


    def getInfo(self):
        print(f"The fare of {self.name} is {self.fare}")

    def bookSeats(self):
        if int(self.seats)>0:
            print(f"Your ticket has been booked!\n your seat number is{self.seats}")
            int(self.seats)=int(self.seats)-1
        else:
            print(f"Sorry this train is full,ticket is not available!")



intercity=Train("Doranto Express:143045","400","02")

intercity.getStatus()
intercity.getInfo()
intercity.bookSeats()



     