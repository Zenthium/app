#! /usr/bin/env python3

import random

#This is an attempt at a rock-paper-scissors game.

cpuchoices = ['Rock', 'Paper', 'Scissors']
cpuchoice = cpuchoices[random.randint(0,2)]

print("Hello! Welcome to Rock Paper Scissors!")
print("Before we get started, what is your name?")
username = input()
print("Alright " + username + ", lets get started.")
print("Here is what you need to know: \n1. Rock \n2. Scissors \n3. Paper")

player = False

while player == False:
    print("What would you like to play?")
    player = input()
    if player == cpuchoice:
        print("It was a tie!")
    elif player == 'Rock':
        if cpuchoice == 'Paper':
            print("You lost! The CPU covered you with Paper!")
        else:
            print("You won! You broke the CPU's scissors!")
    elif player == 'Scissors':
        if cpuchoice == 'Paper':
            print("You won! You cut up the CPU's paper!")
        else:
            print("You lost! The CPU crushed your scissors with its rock!")
    elif player == 'Paper':
        if cpuchoice == 'Rock':
            print("You win! You covered the CPU's rock with your paper!")
        else:
            print("You lose! The CPU cut up your paper with its scissors!")
    else:
        print("That is not a valid input. Please enter a number between 1 and three.")

    print("Would you like to play again?")
    again = input("Press 1 to play again, 2 to exit")
    if int(again) == 2:
        print("Thank you for playing!")
        break
    elif int(again) == 1:
        print("")
        print("Let's do this!")
        player = False
        cpuchoice = cpuchoices[random.randint(0,2)]
    while 1 > int(again) or int(again) > 2:
        print("That is not a valid option! Please try again")
        again = input("Press 1 to play again, 2 to exit")