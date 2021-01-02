#Goal: Create a tic-tac-toe game using functions, data-structures, dictionaries, and lists.
#Helpful Libraries: pprint, random, sys, pprint, copy
#Note: First player to go is X and second player is O

                                                ####PsudeoCode####

#*#*#*#*#*#*#*#*#*#*#**#*#*#*#*#*#*#*#*#*#*#*( Functions PsudeoCode )*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
##First Move Mini Game Function || Input: Rand Number; Output: Human first bool (COMPLETED)
    #Coinflip? Rand. Number Guessing game?

##Print Gameboard Function || Input: Board Data Structure; Output: Pretty Board Data Structure (COMPLETED)
    #Note: Use pretty print library

##Game Status Checker Function || Input: Board Data-Structure; Output: Winner, Draw, Unfinished
    #Three In Row? 
        #If yes: count most common element and declare winner.
        #If no:
            #Empty Spaces remaining? 
                #If No: Draw
                #If Yes: Return Unfinished

##Easy AI Function || Input:(X/O & Board Data-Structure); Output: Easy AI Board Data-Structure Revision
    #Random Fill Data Structure

##Hard AI Function || Input:(X/O & Board Data-Structure); Output: Hard AI Board Data-Structure Revision
    #See 'win tictactoe every time algo'

#*#*#*#*#*#*#*#*#*#*#**#*#*#*#*#*#*#*#*#*##*#*( Main Program PsudeoCode )*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#set default errors attempts to 0
#Welcome Screen, 
#Loop 'Play tic tac toe? (y/n)'
   #try:
        #if yes:
            #Game Difficult Pick (Easy/Hard variable return)
            #First Move Mini Game (firstMove variable return)
                #if human first: 
                    #Declare human X
                    #Print Gameboard Function (Empty)
                    #User gameboard input
                    #Print Gameboard Function
                #else: 
                    #Declare computer X
            #Loop (depends on Game Status Checker Function)
                #Computer AI Function (Use Easy/Hard argument)
                #Print Gameboard Function
                #User input
                #Print Gameboard Function    
        #if no:
            #exit program
    #except:
        #error attempts + 1
        #if error attempts less than or equal max attempts
            #print('Wrong data type entered, please read directions carefully. Restarting game.')
        #else
            #Exit program. 
#*#*#*#*#*#*#*#*#*#*#**#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#

import sys
import os
import random

#Demo Data Structure
boardDataStructure = {'top-left': 'O', 'top-center': 'O', 'top-right': 'X', 'mid-left': 'O', 'mid-center': 'X', 'mid-right': 'O', 'bottom-left': 'X', 'bottom-center': 'O', 'bottom-right': 'X'}

def firstMoveMiniGame(): #Prompts user to play guessing game to determine first move. Returns true or false value if the human won.
    randomNumber = random.randint(0,10)
    computerChoice = random.randint(0,10)
    for i in range(0,3): #Loop for three attempts, used to error check non-valid game inputs.
        try:
            print('Please pick a number between 0 and 10.')
            number = str(input())
            if abs(randomNumber - int(number)) == abs(randomNumber - computerChoice):
                os.system('cls')
                print('You tied!' + "\n" + 'The number was: ' + str(randomNumber) + '. You guessed ' + str(number) + ' and the computer guessed ' + str(computerChoice) +'.')
                print("*Please try again!*") #Human tied, loop.
                i += 1
            elif abs(randomNumber - int(number)) < abs(randomNumber - computerChoice):
                os.system('cls')
                print('Congrats, you won the guessing game!' + "\n" + 'The number was: ' + str(randomNumber) + '. You guessed ' + str(number) + ' and the computer guessed ' + str(computerChoice) +'.')
                return True #Human won, returns true.
            else:
                os.system('cls')
                print('You lost the guessing game.' + "\n" + 'The number was: ' + str(randomNumber) + '. You guessed ' + str(number) + ' and the computer guessed ' + str(computerChoice) +'.')
                return False #Human lost, returns false.
        except ValueError: #Error checking for non-integer value.
            i += 1
            if i >= 3:
                os.system('cls')
                print('Max attempts reached, exiting program.')
                sys.exit()
            os.system('cls')
            print("\n" + '*Incorrect input type. Please try again.*' + "\n")
        except:
            os.system('cls')
            print('Critical error, exiting program.')
            sys.exit()

def printGameboard(boardDataStructure): #Inputs current tic-tac-toe data structure and returns it in easy to read format.
    os.system('cls')
    print(boardDataStructure.get('top-left', ' ') + ' | ' + boardDataStructure.get('top-center', ' ') + ' | ' + boardDataStructure.get('top-right',' '))
    print('----------')
    print(boardDataStructure.get('mid-left', ' ') + ' | ' + boardDataStructure.get('mid-center', ' ') + ' | ' + boardDataStructure.get('mid-right',' '))
    print('----------')
    print(boardDataStructure.get('bottom-left', ' ') + ' | ' + boardDataStructure.get('bottom-center', ' ') + ' | ' + boardDataStructure.get('bottom-right',' '))
    return

