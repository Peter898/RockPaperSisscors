"""
Peter Mei
CIS 401

Task: Create a rock paper and scissors application using libraries from Python
"""

def welcome():
    print("Welcome to rock, paper and scissors")
    print("---------------------------------------------")
    print("Rules: \n 1 represents rock \n 2 represents paper \n 3 represents scissors. \n You can play again or exit the program after each game")
    print("-----------------------------------------------------------------------------------")
    player = input("Enter your name: ")
    print(f"Hello, {player}")
    print("You will be playing against a computer.")
    game(player)


def game(player):
    #import the libraries needed to do a loop
    import random
    result =""
    pick = eval(input("Pick a number: 1 (rock), 2(paper), 3(scissor).  "))

    #pick a random number from 1 to 3
    compPick = random.randint(1,3)
    print(f"Computer picked {compPick}.")

    #checks if the number picked by player is = to computer
    #uses boolean to test result to return the result
    #make sure valid input is entered
    if((pick <=0 ) or  (pick>3)):
        #enter incorrect number
        print("Invalid input, please try again")
        game(player)
    elif(pick == compPick):
        #draw
        print("Draw!")
    elif (pick < compPick):
        #computer won
        print("Computer Won!")
    else:
        #player won
        print(f"{player} won! ")
    #asks the player if he wants to play again
    again = input("Would you like to play again? Y/N")
    print("---------------------------------------------")
    if((again[0] == 'y') or (again[0] == 'Y')):
        welcome()
    else:
        exit()


welcome()