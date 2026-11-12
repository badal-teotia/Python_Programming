#_________________ Number guessing game.

a = 17

while True:
    b = int(input("Guess the number in my mind between 1 to 100 :"))
    
    if b>=30 and b<=100:
        print("Too high!")
        
    elif b>20 and b<30:
        print("High!")
        
    elif b>=1 and b<8:
        print("Too low!")
        
    elif b>=8 and b<12:
        print("Low!")
        
    elif b>=12 and b<17:
        print("Close!!!!")
        
    elif b>17 and b<=20:
        print("Close!!!!")
        
    elif b==a:
        print("Congratulations!! You guessed the number. You win!!!, The number is " + str(a))
        break
    
    else:
        print("Only guess numbers between 1 to 100.")
        continue