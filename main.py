import random
from os import system as sys
from os import environ as env
import time
import replit


user_wins = 0
computer_wins = 0
username = env["REPL_OWNER"]
options = ["rock", "paper", "scissors"]

print("Welcome to Rock-paper-scissors, " + str(username))

def clear(): sys('clear')



while True:
    user_input = input("Chose rock/paper/scissors\n(q to quit)\n ").lower
    if user_input() == "q":
        break
    
    if user_input() not in options:
        print("troller")
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("The computer has chose " + computer_pick)

    if user_input() == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1
        time.sleep(1)
        replit.clear()

    elif user_input() == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1
        time.sleep(1)
        replit.clear()

    elif user_input() == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1
        time.sleep(1)
        replit.clear()
    elif user_input() == computer_pick:
        print("It's a tie")
        time.sleep(1)
        replit.clear()
    else:
        print("You lost!")
        computer_wins += 1
        time.sleep(1)
        replit.clear()

print("You have won " + str(user_wins) + " times.")
print("The computer has won " + str(computer_wins) + " times.")
        

    