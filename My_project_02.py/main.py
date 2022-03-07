from os import write
import random
randNumber=random.randint(1,100)


userGuesses=None   # define kar rahe hai bus hum!
guesses=0

while(userGuesses!=randNumber):
    userGuesses=int(input("Guess a Number!\n"))
    guesses+=1
    
    if (userGuesses==randNumber):
            print("Yeah you guess it right!!")

    elif (userGuesses>randNumber):
            print("You Guessed it wrong! Enter the smaller number")
            
    else:
                print("You Guessed it wrong! Enter the larger number")

print(f"You guessed it in {guesses}")



# If I wanted to update my previous highscore stored in one file then --->
with open("highscore2.txt", "r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("You have just broken the high score!")
    with open("highscore2.txt", "w") as f:
        f.write(str(guesses))

