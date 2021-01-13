#Author: Matteo Capasso
#Goal: Create a tic-tac-toe game using functions, data-structures, dictionaries, and lists. Purpose is to develop working familiarity with data structures, lists, and indexes.
#Documentation Note: Comments denoted #* require further review.

import sys #Used everywhere
import os #Used everywhere
import random #Used in firstMoveMiniGame() and easyAI()

def firstMoveMiniGame(): #Prompts user to play guessing game to determine first move. Returns true if human won, returns false if human lost.
    for i in range(0,3): #Creating limited amount of attempts, used to validate mini-game inputs and stop infinite loop in the event of multiple ties.
        try:
            randomNumber = random.randint(0,10)
            computerChoice = random.randint(0,10)
            number = str(input('Please pick a number between 0 and 10: '))
            if abs(randomNumber - int(number)) == abs(randomNumber - computerChoice): #Using distance function to compare who is closer to the random number. 
                os.system('cls')
                print('You tied!' + "\n" + 'The number was: ' + str(randomNumber) + '. You guessed ' + str(number) + ' and the computer guessed ' + str(computerChoice) +'.')
                print("\n"+ "Time for a rematch!") #Human tied, continues through loop.
                os.system('pause')
                os.system('cls')
                i += 1
            elif abs(randomNumber - int(number)) < abs(randomNumber - computerChoice): #Using distance function to compare who is closer to the random number. 
                os.system('cls')
                print('Congrats, you can move first!' + "\n" + 'The number was: ' + str(randomNumber) + '. You guessed ' + str(number) + ' and the computer guessed ' + str(computerChoice) +'.')
                return True #Human won, returns true.
            else:
                os.system('cls')
                print('You lost the guessing mini-game.' + "\n" + 'The number was: ' + str(randomNumber) + '. You guessed ' + str(number) + ' and the computer guessed ' + str(computerChoice) +'.')
                return False #Human lost, returns false.
        except ValueError: #Error checking path for non-integer values. 
            i += 1
            if i >= 3:
                os.system('cls')
                print('Max attempts reached reached for mini-game.')
                sys.exit()
            os.system('cls')
            print("\n" + '*Incorrect input type. Try again.*' + "\n")
        except:
            os.system('cls')
            print('Critical error in first move mini game, exiting program.')
            os.system('pause')
            sys.exit()

def printGameboard(boardDataStructure): #Inputs current tic-tac-toe data structure, and prints it in easy to read format.
    print(boardDataStructure.get('top-left', ' ') + ' | ' + boardDataStructure.get('top-center', ' ') + ' | ' + boardDataStructure.get('top-right',' '))
    print('---------')
    print(boardDataStructure.get('mid-left', ' ') + ' | ' + boardDataStructure.get('mid-center', ' ') + ' | ' + boardDataStructure.get('mid-right',' '))
    print('---------')
    print(boardDataStructure.get('bot-left', ' ') + ' | ' + boardDataStructure.get('bot-center', ' ') + ' | ' + boardDataStructure.get('bot-right',' '))
    return

def gameContinuation(grid): #Inputs current board to check game status. Returns game status as string: champion (this denotes a winner exists but not who), unfinished, or draw.
    try: 
        if ( #This checks for all winning combinations in a 3x3 game.
            ((grid.get('top-left') == grid.get('top-center') == grid.get('top-right')) and grid.get('top-left') != None) or  #Checking top row equality & non-empty 
            ((grid.get('mid-left') == grid.get('mid-center') == grid.get('mid-right')) and grid.get('mid-left') != None) or  #Checking mid row equality & non-empty
            ((grid.get('bot-left') == grid.get('bot-center') == grid.get('bot-right')) and grid.get('bot-left') != None) or  #Checking bot row equality & non-empty
            ((grid.get('top-left') == grid.get('mid-left') == grid.get('bot-left')) and grid.get('top-left') != None) or          #Checking left col equality & non-empty
            ((grid.get('top-center') == grid.get('mid-center') == grid.get('bot-center')) and grid.get('top-center') != None) or  #Checking mid col equality & non-empty
            ((grid.get('top-right') == grid.get('mid-right') == grid.get('bot-right')) and grid.get('top-right') != None) or      #Checking right col equality & non-empty
            ((grid.get('top-left') == grid.get('mid-center') == grid.get('bot-right')) and grid.get('top-left') != None) or   #Checking diag left to right equality & non-empty
            ((grid.get('top-right') == grid.get('mid-center') == grid.get('bot-left')) and grid.get('top-right') != None)     #Checking diag right to left equality & non-empty
            ):
            return 'champion' #Game is won/lost therefore over.
        else:
            if len(grid) < 9: #Checks if there are missing key pairs, this represents an unfinished game.
                return 'unfinished'
            else:
                return 'draw' #Game is drawn therefore over.
    except:
        os.system('cls')
        print('Critical error in game status checker, exiting program.')
        os.system('pause')
        sys.exit()

def easyAI(boardDataStructure, humanFirst, emptyBoard): #Inputs current game structure, randomly chooses computer's move, and then modifies board datastructure accordingly. 
    emptyBoardKeysList = emptyBoard 
    boardDataStrucKeysList = list(boardDataStructure.keys()) #Taking keys from current board.
    unfilledSquaresList = list(set(emptyBoardKeysList)^set(boardDataStrucKeysList)) #Checking for differences in the two sets of keys
    randomIndex = random.randint(0,int(len(unfilledSquaresList))-1) #Generates random number based off the length of the differenced set, unfilledSquaresList.
    computerMove = unfilledSquaresList[randomIndex] #Uses that randomly generated number to pick an element to index by.
    if humanFirst == True: #Insuring computer writes proper character to main game board.
        boardDataStructure.setdefault(computerMove, 'O')
    else:
        boardDataStructure.setdefault(computerMove, 'X')

def userEntryCollectAndCheck(boardDataStructure, playerCharacter, emptyBoard): #Input prompt that validate's users game move with empty board template and current game board.
    for i in range(1,5): #Creating limited amount of attempts.
        try:
            userGameInput = input()
            if userGameInput.lower() in emptyBoard: #Checking if user's input appears in the empty board list
                if userGameInput.lower() in boardDataStructure.keys(): #Checking if user's input appears as key in current game
                    print("\n" + 'That spot is already taken, please type a new spot:')
                    i += 1
                else:
                    boardDataStructure.setdefault(userGameInput, playerCharacter)
                    break
            else:
                print("\n" + 'Invalid entry, please read options and type new move:')
                i += 1
        except:
            os.system('cls')
            print('Critical error in user entry collector and checker, exiting program.')
            os.system('pause')
            sys.exit()

#Main Program
exitGame = False
errorAttempts = 0
emptyBoard = ['top-left', 'top-center', 'top-right', 'mid-left', 'mid-center', 'mid-right', 'bot-left', 'bot-center', 'bot-right']
os.system('cls') #Clear previous terminal gunk
while exitGame == False: 
    try:
        playGameQ = input('Would you like to play tic-tac-toe? (yes/no): ')
        if (playGameQ.lower() == 'y') or (playGameQ.lower() =='ye') or (playGameQ.lower() =='yes'):
            #os.system('cls') #Include if various AI difficulties
            #difficulty = input(r'Please type desired difficulty level. (easy/hard): ') #Difficulty prompt for various AI levels
            difficulty = 'easy' #Remove if various AI difficulties; however, for practice project purposes, easy mode suffices.
            os.system('cls')
            boardDataStructure = {} #Setting the game board to empty, important for repeated game functionality.
            if firstMoveMiniGame() == True: #Note, firstMoveMiniGame() includes print() in its function.
                humanFirst = True
                playerCharacter = 'X' #Note, first player to move in tic-tac-toe is always 'X'.
                print("\n" + 'You are "X", and are playing at ' + difficulty +' difficulty.' + "\n")
                printGameboard(boardDataStructure)
                print("\n" + 'Please input an option from the following:' +"\n" + str(emptyBoard))
                userEntryCollectAndCheck(boardDataStructure, playerCharacter, emptyBoard) #Player Move Input & Validation
                os.system('cls')
            else:
                humanFirst = False
                playerCharacter = 'O' #Note, second player to move in tic-tac-toe is always 'O'.
            while gameContinuation(boardDataStructure) == 'unfinished':
                easyAI(boardDataStructure, humanFirst, emptyBoard) #AI Move Input and board datastructure Change
                lastMove = 'computer' #LastMove variable is important for winner declaration later.
                printGameboard(boardDataStructure)
                if gameContinuation(boardDataStructure) != 'unfinished': #Checking if computer's recent move ended game. 
                    break
                print("\n" + 'You are playing as "' + playerCharacter +'" on ' + difficulty + ' difficulty.')
                print("\n" + 'Please input an option from the following:' + "\n" + str(emptyBoard))
                userEntryCollectAndCheck(boardDataStructure, playerCharacter, emptyBoard) #Player Move Input & validation
                #Note, the process that validates if the player ended the game at this step is performed in the loop's conditionality statement. 
                lastMove = 'player' 
                os.system('cls')
            os.system('cls')
            printGameboard(boardDataStructure)
            #Winner declaration is done by checking who made the final move that led to the game reaching a 'champion' or 'draw' status. 
            if gameContinuation(boardDataStructure) == 'champion' and lastMove == 'player':
                print('Congratulations, you won as ' + playerCharacter +'!' + "\n")
            elif gameContinuation(boardDataStructure) == 'champion' and lastMove == 'computer':
                print('Sorry, you lost as ' + playerCharacter +'!' + "\n")
            elif gameContinuation(boardDataStructure) == 'draw':
                print('You tied. Nice try!' + "\n")
            else:
                print('Critical error in winner announcment.')
            os.system('pause')
            os.system('cls')
        else:
            exitGame = True        
    except: #Error segment for bad user inputs. 
        errorAttempts =+ 1
        if errorAttempts <= 3:
            print("\n" + 'Please read directions carefully. Restarting game.')
        else:
            print("\n" + 'Maxiumum number of error attempts reached.')
            exitGame = True
print("\n"*5 + 'Thank you for playing, have a nice day!')
os.system('pause')
sys.exit()