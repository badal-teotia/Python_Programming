#___________________ Make a rock, paper, scissors game.

import random

list = ["rock", "paper", "scissors"]

while True:
    a = random.choice(list)
    b = input("Enter your choice (rock, paper, scissors) :")
    
    if a==b:
        print("My choice was also " + a + ". It's a tie!")
        
    elif (a=="rock" and b=="scissors") or (a=="paper" and b=="rock") or (a=="scissors" and b=="paper"):
        print("My choice was " + a + ". I win!")
        
    elif (a=='scissors' and b=='rock') or (a=='rock' and b=='paper') or (a=='paper' and b=='scissors'):
        print("My choice was " + a + " You won!!")
        
    else:
        print ("You don't wanna play, ok , bye you dumb")
        break

