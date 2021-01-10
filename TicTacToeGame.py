#Goal: Create a tic-tac-toe game using functions, data-structures, dictionaries, and lists. Purpose is to develop familiarity with data structures, lists, and indexes.
#Game Rule Note: First player to go is "X" and second player to move is "O"
#Documentation Note: Comments denoted #* require further review.

                                                ####PsudeoCode####
#*#*#*#*#*#*#*#*#*#*#**#*#*#*#*#*#*#*#*#*#*#*( Functions PsudeoCode )*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
    ##First Move Mini Game Function || Input: Rand Number; Output: Human first bool (COMPLETED for nxn board)
        #Coinflip? Rand. Number Guessing game?

    ##Print Gameboard Function || Input: Board Data Structure; Output: Pretty Board Data Structure (COMPLETED for 3x3 board)
        #Note: Use pretty print library

    ##Game Continuation Checker Function || Input: Board Data-Structure; Output: Finished Game Boolean (COMPLETED for 3x3 board)
        #Three In Row? Note, this logic can be applied to nxn board with a modification in the yes pathway's conditional statement.
            #If yes: count most common element and declare winner.
            #If no:
                #Empty Spaces remaining? 
                    #If No: Draw. Note, it may be possible to draw in 3x3 or nxn board before all the spaces are filled in - needs further review, but functional as is for 3x3 case.
                    #If Yes: Return Unfinished

    ##Error Checking & Duplicate Entry Checking Function (Pending)
    
    ##Easy AI Function || Input:(X/O & Board Data-Structure); Output: Easy AI Board Data-Structure Revision (COMPLETED for nxn board)
        #Note, the easy AI fills in entries by randomly indexing set differences.

    #Hard AI Function || Input:(X/O & Board Data-Structure); Output: Hard AI Board Data-Structure Revision (Pending)
        #See 'win tictactoe every time algo' for 3x3 Grid, I believe there is a hardcode for this -- needs further review.

#*#*#*#*#*#*#*#*#*#*#**#*#*#*#*#*#*#*#*#*##*#*( Main Program PsudeoCode )*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
    #Note, this logic works for nxn board; however, the user would need to be prompted for more info (e.g. how big of a grid they want, how many matching characters in row to win)
    #Main Program (Pending) 
        #set default errors attempts to 0
        #try:
            #Loop 'Play tic tac toe? (y/n)'
            #if yes:
                #Game Difficult Pick (Easy/Hard variable return)
                #First Move Mini Game (firstMove variable return)
                    #if human first. from mini game above: 
                        #Declare Human X
                        #Print Gameboard Function (Empty)
                        #User gameboard input
                    #else: 
                        #Declare Computer X
                #Loop (depends on Game Status Checker Function)
                    #Computer AI Function (Use Easy/Hard argument)
                    #Print Gameboard Function
                    #if AI won game here
                        #break from loop
                    #User input
                    #Print Gameboard Function    
                #Winner Declaration, check who has the most enteries total b/c winner is last person to move; therefore, most enteries in turn-by-turn game.
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

import sys
import os
import random

def firstMoveMiniGame(): #Prompts user to play 0 to 10 number guessing game to determine first move. Returns true or false value if the human won.
    for i in range(0,3): #Loop for three attempts, used to error check non-valid game inputs.
        try:
            randomNumber = random.randint(0,10)
            computerChoice = random.randint(0,10)
            number = str(input('Please pick a number between 0 and 10: '))
            if abs(randomNumber - int(number)) == abs(randomNumber - computerChoice):
                os.system('cls')
                print('You tied!' + "\n" + 'The number was: ' + str(randomNumber) + '. You guessed ' + str(number) + ' and the computer guessed ' + str(computerChoice) +'.')
                print("\n"+ "Time for a rematch!") #Human tied, loop.
                os.system('pause')
                os.system('cls')
                i += 1
            elif abs(randomNumber - int(number)) < abs(randomNumber - computerChoice):
                os.system('cls')
                print('Congrats, you can move first!' + "\n" + 'The number was: ' + str(randomNumber) + '. You guessed ' + str(number) + ' and the computer guessed ' + str(computerChoice) +'.')
                return True #Human won, returns true.
            else:
                os.system('cls')
                print('You lost the guessing mini-game.' + "\n" + 'The number was: ' + str(randomNumber) + '. You guessed ' + str(number) + ' and the computer guessed ' + str(computerChoice) +'.')
                return False #Human lost, returns false.
        except ValueError: #Error checking for non-integer value.
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

def printGameboard(boardDataStructure): #Inputs current tic-tac-toe data structure, and returns it in easy to read format.
    print(boardDataStructure.get('top-left', ' ') + ' | ' + boardDataStructure.get('top-center', ' ') + ' | ' + boardDataStructure.get('top-right',' '))
    print('---------')
    print(boardDataStructure.get('mid-left', ' ') + ' | ' + boardDataStructure.get('mid-center', ' ') + ' | ' + boardDataStructure.get('mid-right',' '))
    print('---------')
    print(boardDataStructure.get('bot-left', ' ') + ' | ' + boardDataStructure.get('bot-center', ' ') + ' | ' + boardDataStructure.get('bot-right',' '))
    return

def gameContinuation(grid): #Inputs board data structure to check game status. Game status as string: champion (this denotes a winner exists, but not who), unfinished, or draw.
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

def easyAI(boardDataStructure, humanFirst): #Inputs current tic-tac-toe data structure and modifys datastucture of current game. 
    emptyBoard = {'top-left': '', 'top-center': '', 'top-right': '', 'mid-left': '', 'mid-center': '', 'mid-right': '', 'bot-left': '', 'bot-center': '', 'bot-right': ''}
        #For nxn solution, be sure to procur a datastucture with the properly notated key's as in emptyBoard above.
    emptyBoardKeysList = list(emptyBoard.keys())
    boardDataStrucKeysList = list(boardDataStructure.keys())
    unfilledSquaresList = list(set(emptyBoardKeysList)^set(boardDataStrucKeysList)) #Checking for key (as in key-pair) differences between two sets.
    randomIndex = random.randint(0,int(len(unfilledSquaresList))-1) #Chooses random number (based off length of unfilledSquaresList) for use in indexing.
    computerMove = unfilledSquaresList[randomIndex]
    if humanFirst == True:
        boardDataStructure.setdefault(computerMove, 'O') #Note, writes O because the computer moves second if humanFirst is true.
    else:
        boardDataStructure.setdefault(computerMove, 'X')

def userEntryCollectAndCheck(boardDataStructure, playerCharacter, emptyBoard): #Input prompt that validate's users game move with empty board keys and current game board.
    for i in range(1,5): #Five attempts
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
emptyBoard = ['top-left', 'top-center', 'top-right', 'mid-left', 'mid-center', 'mid-right', 'bot-left', 'bot-center', 'bot-right'] #Empty 3x3 board.
os.system('cls') #clear previous terminal messages
while exitGame == False:
    try:
        playGameQ = input('Would you like to play tic-tac-toe? (yes/no): ')
        if (playGameQ.lower() == 'y') or (playGameQ.lower() =='ye') or (playGameQ.lower() =='yes'):
            #os.system('cls') #include if new AI difficulties
            #difficulty = input(r'Please type desired difficulty level. (easy/hard): ') #Difficulty Prompt for AI levels
            difficulty = 'easy' #remove if new AI difficulties
            os.system('cls')
            boardDataStructure = {} #Setting the game board to empty, important for repeated game functionality.
            if firstMoveMiniGame() == True: #Note, firstMoveMiniGame() includes print() in its function.
                humanFirst = True
                playerCharacter = 'X'
                print("\n" + 'You are "X", and are playing at ' + difficulty +' difficulty.' + "\n")
                printGameboard(boardDataStructure) #Print gameboard
                print("\n" + 'Please input an option from the following:' +"\n" + str(emptyBoard))
                userEntryCollectAndCheck(boardDataStructure, playerCharacter, emptyBoard) #Player Move Input & Validation
                os.system('cls')
            else:
                humanFirst = False
                playerCharacter = 'O'
            while gameContinuation(boardDataStructure) == 'unfinished':
                easyAI(boardDataStructure, humanFirst) #AI Move Input
                lastMove = 'computer'
                printGameboard(boardDataStructure) #Print gameboard
                if gameContinuation(boardDataStructure) != 'unfinished':
                    break
                print("\n" + 'You are playing as "' + playerCharacter +'" on ' + difficulty + ' difficulty.')
                print("\n" + 'Please input an option from the following:' + "\n" + str(emptyBoard))
                userEntryCollectAndCheck(boardDataStructure, playerCharacter, emptyBoard) #Player Move Input & validation
                lastMove = 'player' 
                os.system('cls')
            os.system('cls')
            printGameboard(boardDataStructure)
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
    except:
        errorAttempts =+ 1
        if errorAttempts <= 3:
            print("\n" + 'Please read directions carefully. Restarting game.')
        else:
            print("\n" + 'Maxiumum number of error attempts reached.')
            exitGame = True
print("\n"*5 + 'Thank you for playing, have a nice day!')
os.system('pause')
sys.exit()