
import random

max_range=int(input("enter the range for your guess :(you will have 3 try )"))
ai_guess=random.randrange(0,max_range)
guesses=0
while True:
    user_guess=int(input("start guessing"))
    guesses +=1
    if ai_guess==user_guess:
        print('u win gg')
        break
    elif guesses==3:
        print("you run out of guesses try again ")
        break
    

    
