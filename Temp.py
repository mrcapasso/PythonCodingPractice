import sys
import os
import random

#check if input match empty board
                #if yes, check current boardgame for duplicate
                    #if no, setdefault and break
                    #if yes, continue loop +1 attempts
            #if no, continue loop +1 attempts

def userEntryCollectAndCheck(boardDataStructure, playerCharacter): #Inputs user's game entry input and checks for duplicate values
    for i in range(1,5): #Five attempts
        try:
            userGameInput = input()
            emptyBoard = ['top-left', 'top-center', 'top-right', 'mid-left', 'mid-center', 'mid-right', 'bot-left', 'bot-center', 'bot-right']
            if emptyBoard.index(userGameInput.lower()): #Checking if user's input appears in the empty board list
                if userGameInput.lower() in list(boardDataStructure.keys()): #Checking if user's input appears as key in current game
                    boardDataStructure.setdefault(userGameInput, playerCharacter)
                    break
                else:
                    print('Please pick a different spot, that one is already taken!')
                    i += 1
            else:
                print('Invalid entry, please check options and try again.')
                i += 1
        except:
            os.system('cls')
            print('Critical error in user entry collector and checker, exiting program.')
            os.system('pause')
            sys.exit()


boardDataStructure = {}
userEntryCollectAndCheck(boardDataStructure, 'X')
print(boardDataStructure)

