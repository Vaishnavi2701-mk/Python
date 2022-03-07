def game():
    return 56

score=game()
with open('highscore.txt') as f:
    highscore=(f.read())

    if int(highscore)<score:
        with open('highscore.txt', 'w') as f:
           highscore=f.write(str(score))
    elif highscore==""       :
         with open('highscore.txt', 'w') as f:
           highscore=f.write(str(score))
        

        