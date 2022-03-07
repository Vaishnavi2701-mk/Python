import random

def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=="S":
        if you=="R":
            return  True
        elif you=="P":
            return False
    elif comp=="P":
        if you=="S":
            return True
        elif you=="R":
            return False
    elif comp=="R":
        if you=="S":
            return False
        elif you=="P":
            return True

                                        
print("Computer turn: Scissor(S), Paper(P), Rock(R)?\n")

randomno=random.randint(1,3)
if randomno ==1 :
    comp="S"
elif randomno==2:
    comp="P"
elif randomno==3:
    comp="R"

you=input("Your turn: Scissor(S), Paper(P), Rock(R)?\n")      

a=gamewin(comp,you)


if a==None:
    print("The game is tie!!")
elif a:
    print("Congatulations you win!!")
else:
    print("You lose!!")  