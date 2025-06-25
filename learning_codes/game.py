import random
from sys import exit

def main():
    
   
    while True:
        
        x = False
        try:
            level = inp("Level: ")
        except (ValueError):
            x = True
        
        
        if not x:
            break
        
   
    numero = random.randint(0, level)
    
    
    while True:
        x = True
        try:
            guess = inp("Guess: ")
        except ValueError:
            x = False
        if x:
            if guess < numero:
                print("Too low.")
            elif guess > numero:
                print("Too high.")
            else:
                    print("Just right.")
                    exit()
    
def inp(xd):
    return int(input(xd))
    


    


main()