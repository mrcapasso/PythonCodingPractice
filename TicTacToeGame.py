#Goal: Create a tic-tac-toe game using functions, data-structures, dictionaries, and lists.
#Helpful Libraries: pprint, random, sys, pprint, copy
#Note: First player to go is X and second player is O

                                                ####PsudeoCode####

#*#*#*#*#*#*#*#*#*#*#**#*#*#*#*#*#*#*#*#*#*#*( Functions PsudeoCode )*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
##First Move Mini Game Function || Input: Rand Number; Output: Human first bool (COMPLETED)
    #Coinflip? Rand. Number Guessing game?

##Print Gameboard Function || Input: Board Data Structure; Output: Pretty Board Data Structure (COMPLETED)
    #Note: Use pretty print library

##Game Continuation Checker Function || Input: Board Data-Structure; Output: Finished game bool (COMPLETED)
    #Three In Row? 
        #If yes: count most common element and declare winner.
        #If no:
            #Empty Spaces remaining? 
                #If No: Draw
                #If Yes: Return Unfinished

##Easy AI Function || Input:(X/O & Board Data-Structure); Output: Easy AI Board Data-Structure Revision (COMPLETED)

##Hard AI Function || Input:(X/O & Board Data-Structure); Output: Hard AI Board Data-Structure Revision
    #See 'win tictactoe every time algo'

#*#*#*#*#*#*#*#*#*#*#**#*#*#*#*#*#*#*#*#*##*#*( Main Program PsudeoCode )*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
#set default errors attempts to 0
#Welcome Screen, 
   #try:
        #Loop 'Play tic tac toe? (y/n)'
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
            #Winner Declaration
                #histogram = list(boardDataStructure.values())
                #winningCharacter = max(set(histogram))
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
import pprint #* needed?

#Demo Data Structure (Missing Key-Pairs)
#boardDataStructure = {'top-right': 'X', 'mid-left': 'O', 'mid-center': 'O', 'mid-right': 'X', 'bot-left': 'O', 'bot-center': 'X', 'bot-right': 'O'}

def firstMoveMiniGame(): #Prompts user to play 0 to 10 number guessing game to determine first move. Returns true or false value if the human won.
    randomNumber = random.randint(0,10)
    computerChoice = random.randint(0,10)
    for i in range(0,3): #Loop for three attempts, used to error check non-valid game inputs.
        try:
            print('Please pick a number between 0 and 10.')
            number = str(input())
            if abs(randomNumber - int(number)) == abs(randomNumber - computerChoice):
                os.system('cls')
                print('You tied!' + "\n" + 'The number was: ' + str(randomNumber) + '. You guessed ' + str(number) + ' and the computer guessed ' + str(computerChoice) +'.')
                print("\n"+ "Please try again!") #Human tied, loop.
                i += 1
            elif abs(randomNumber - int(number)) < abs(randomNumber - computerChoice):
                os.system('cls')
                print('Congrats, you can move first!' + "\n" + 'The number was: ' + str(randomNumber) + '. You guessed ' + str(number) + ' and the computer guessed ' + str(computerChoice) +'.')
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
            print('Critical error in first move mini game, exiting program.')
            sys.exit()

def printGameboard(boardDataStructure): #Inputs current tic-tac-toe data structure and returns it in easy to read format.
    #*os.system('cls')
    print(boardDataStructure.get('top-left', ' ') + ' | ' + boardDataStructure.get('top-center', ' ') + ' | ' + boardDataStructure.get('top-right',' '))
    print('---------')
    print(boardDataStructure.get('mid-left', ' ') + ' | ' + boardDataStructure.get('mid-center', ' ') + ' | ' + boardDataStructure.get('mid-right',' '))
    print('---------')
    print(boardDataStructure.get('bot-left', ' ') + ' | ' + boardDataStructure.get('bot-center', ' ') + ' | ' + boardDataStructure.get('bot-right',' '))
    return

def gameContinuation(grid): #Inputs board data structure to check game status. Outputs true or false bool representing if the game should continue.
    try: 
        if ( #This checks for all winning combinations in 3x3 game.
            ((grid.get('top-left') == grid.get('top-center') == grid.get('top-right')) and grid.get('top-left') != None) or  #Checking top row & non-empty 
            ((grid.get('mid-left') == grid.get('mid-center') == grid.get('mid-right')) and grid.get('mid-left') != None) or  #Checking mid row & non-empty
            ((grid.get('bot-left') == grid.get('bot-center') == grid.get('bot-right')) and grid.get('bot-left') != None) or  #Checking bot row & non-empty
            ((grid.get('top-left') == grid.get('mid-left') == grid.get('bot-left')) and grid.get('top-left') != None) or          #Checking left col & non-empty
            ((grid.get('top-center') == grid.get('mid-center') == grid.get('bot-center')) and grid.get('top-center') != None) or  #Checking mid col & non-empty
            ((grid.get('top-right') == grid.get('mid-right') == grid.get('bot-right')) and grid.get('top-right') != None) or      #Checking right col & non-empty
            ((grid.get('top-left') == grid.get('mid-center') == grid.get('bot-right')) and grid.get('top-left') != None) or   #Checking diag left to right & non-empty
            ((grid.get('top-right') == grid.get('mid-center') == grid.get('bot-left')) and grid.get('top-right') != None)     #Checking diag right to left & non-empty
            ):
            return False #Game is won/lost therefore over.
        else:
            if len(grid) < 9: #Checks if there are missing key pairs, this represents an unfinished game.
                return True
            else:
                return False #Game is drawn therefore over.
    except:
        os.system('cls')
        print('Critical error in game status checker, exiting program.')
        sys.exit()

def easyAI(boardDataStructure, humanFirst): #Inputs current tic-tac-toe data structure and modifys global datastucture of current game. 
    emptyBoard = {'top-left': '', 'top-center': '', 'top-right': '', 'mid-left': '', 'mid-center': '', 'mid-right': '', 'bot-left': '', 'bot-center': '', 'bot-right': ''}
    emptyBoardKeysList = list(emptyBoard.keys())
    boardDataStrucKeysList = list(boardDataStructure.keys())
    unfilledSquaresList = list(set(emptyBoardKeysList)^set(boardDataStrucKeysList)) #Checking for key differences between two sets.
    randomIndex = random.randint(0,int(len(unfilledSquaresList))-1) #Chooses random number (based off length of unfilledSquaresList) for use in indexing.
    computerMove = unfilledSquaresList[randomIndex]
    if humanFirst == True:
        boardDataStructure.setdefault(computerMove, 'O')
    else:
        boardDataStructure.setdefault(computerMove, 'X')

#Main Program
print("\n" + 'Hello, welcome to my tic-tac-toe game.')
exit == True
errorAttempts = 0

#*Include Loop
try:
    print("Would you like to play a round of tic-tac-toe? (Enter yes or no)")
    if input() == "y" or "yes": #* this input check is broken
        print("\n" +'Please type desired difficulty level: ''easy'' or ''hard''')
        difficulty = input()
        os.system('cls')
        boardDataStructure = {} #Setting the game board to empty.
        if firstMoveMiniGame() == True: #Note, firstMoveMiniGame includes print() in its function.
            humanFirst = True
            playerCharacter = 'X'
            print("\n" + 'You are X, and are playing at ' + difficulty +' difficulty.' + "\n")
            printGameboard(boardDataStructure)
            print("\n" + 'Please input an option from the following: (top-left, top-center, top-right, mid-left, mid-center, mid-right, bot-left, bot-center, bot-right)')
            boardDataStructure.setdefault(input(), 'X') #Player Move Input
        else:
            humanFirst = False
            playerCharacter = 'O'
            print("\n" + 'You are O, and are playing at "' + difficulty +'" difficulty.' + "\n")
        while gameContinuation(boardDataStructure) == True:     
            easyAI(boardDataStructure, humanFirst) #AI Move Input
            printGameboard(boardDataStructure) #Print gameboard
            if gameContinuation(boardDataStructure) == False:
                break
            print("\n" + 'Please input an option from the following: (top-left, top-center, top-right, mid-left, mid-center, mid-right, bot-left, bot-center, bot-right).')
            print('Recall your symbol is "' + playerCharacter +'".')
            boardDataStructure.setdefault(input(), playerCharacter) #Player Move Input
            print()
        #*Winner Declaration
                #histogram = list(boardDataStructure.values())
                #winningCharacter = max(set(histogram))
        #*Input error checking for duplicate enteries and bad values on main game
    else:
        #*exit == True
        sys.exit()
except:
    errorAttempts =+ 1
    if errorAttempts >= 3:
        print("\n" + 'Wrong data type entered, please read directions carefully. Restarting game.')
    else:
        print("\n" + 'Maxiumum number of error attempts reached.')
        #*exit == True
        sys.exit()
print("\n"*5 + 'Thank you for playing, have a nice day!')
