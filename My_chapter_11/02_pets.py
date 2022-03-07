class Animal:


    animaltype="domestic"
    
   
class Pets(Animal):

    colour="brown"


class Dog(Pets):
    
    @staticmethod
    def bark():
        print(f"Bow Bow!!")

p=Dog()
print(p.colour)
p.bark()