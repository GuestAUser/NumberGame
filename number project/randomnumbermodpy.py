import random
from os import system #linux case
from termcolor import colored
from time import sleep
import debuganim
#maybe add multi threading

print("==========================================")
print("Welcome to the simple random number say!!!")
print("==========================================")
games = 0
points = 0

while games < 10:
    try:
        if games > 0:
            print("Points: " + str(points) + ". Game: " + str(games))
        games += 1
        print("Try a number (1-25): ") #original = 99;
        Choice = int(input())
        X = random.randrange(1,25,1) #(1, 99, 1)
        print("The number is " +  str(X))
        if X == Choice:
            system('clear')
            packed_content = "YOU DID IT!!!"
            debuganim.textanimation(packed_content) #animation func at debuganim.py
            points += 100
        elif abs(X-Choice)<5:
            print("So close!")
            points += 10
        else:
            print("You miss!")

    except ValueError:
        print("---> PLEASE DO NOT USE STRINGS FOR INPUT! <---")
        print("__could be caused by empty input too__")
        input('continue? [ enter ]')
        games -= 1 
        system('clear')
        print("Welcome to the simple random number say!!!")
        print("Enjoy!")
    except KeyboardInterrupt:
        system('clear')
        print("\n KeyBoardExit Triggered, end!")
        print("Code: Lk10 -> GuestAUser")
        exit();

print("Good Game!")
print("Games: "+ str(games) + ". Points: "+str(points))
print("Code: Lk10 -> GuestAUser")
exit()
