#_________________ Making dice rolling simulator.

from ast import Continue
import random

while True:
    a = input("Do you want to play? (y/n) :").upper()
    if (a=="Y"):
        b = random.randint(1, 6)
        c = random.randint(1, 6)
        print(f'({b},{c})')
    elif(a!="N" and a!="Y"):
        print("What did you said?")
        continue
    else:
        print("Thank you for playing.")
        break