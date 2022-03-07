import random

def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=="S":
        if you=="W":
            return  True
        elif you=="G":
            return False
    elif comp=="W":
        if you=="S":
            return True
        elif you=="G":
            return False
    elif comp=="G":
        if you=="S":
            return False
        elif you=="W":
            return True

                                        
print("Computer turn: Snake(S), Water(W), Gun(G)?\n")

randomno=random.randint(1,3)
if randomno ==1 :
    comp="S"
elif randomno==2:
    comp="W"
elif randomno==3:
    comp="G"

you=input("Your turn:Snake(S), Water(W), Gun(G)?\n")      

a=gamewin(comp,you)


if a==None:
    print("The game is tie!!")
elif a:
    print("Congatulations you win!!")
else:
    print("You lose!!")        
