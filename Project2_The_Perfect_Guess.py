#                                          THE PERFECT GUESS GAME

'''We are going to write a program that generates a random number and ask a user to guess it. If the player's
guess is higher than actual number, the prog displays "Lower number please". Similarly if the user's guess is
too low, the prog prints "higher number please". When the user guess the correct number, the program displys
the number of guesses the player used to arrive at the number.'''
import random

def playGame():

    print('''Lets play a game. We will choose a number between 1- 10. You will have to guess what number 
    we ahave selected. Rules-:
    1.If the number you have guessed is less than what we selected, you willrecieve message
     'Higher number please!!!'. 
    2.Otherwise if the number you guessed is high than what we selected, you wil recieve message
    'Lower number please!!!'. 
    3.If you have guessed perfectly we willshow the number and the message 'Yeah!!!Perfect Guess'.\n''')
    dec = 'C'
    while dec == 'C':
        
        rand = random.randint(1,10)
        num = int(input("Guess The number!!\n"))

        if (num < rand):
            print("Higher number please!!!\n")
            
        elif (num > rand):
            print("Lower number please!!!\n")
            
        elif(num == rand):
            print(f"Yeah!!!Perfect Guess.The we too chose {rand}.\n")

        dec = input("I you want to continue the game, enter 'C' . Otherwise if you want to exit the game, enter 'E'.")
    

playGame()
