#Course: Automate the Boring Stuff with Python Programming
##Section 7: Dictionaries
##URL: https://www.udemy.com/course/automate/learn/lecture/3465848#overview

#Goal: Create a tic-tac-toe game using functions, data-structures, and lists.
#Helpful Libraries: pprint, random, sys, pprint, copy
#Note: first player to go is X and second player is O

                                            ####PsudeoCode####

#*#*#*#*#*#*#*#*#*#*#**#*#*#*#*#*#*#*#*#*##*#*( Functions )*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
##First Move Mini Game Function || Input: Rand Number; Output: Human first bool
    #Coinflip? Rand. Number Guessing game?

##Print Gameboard Function || Input: Board Data Structure; Output: Pretty Board Data Structure
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

#*#*#*#*#*#*#*#*#*#*#**#*#*#*#*#*#*#*#*#*##*#*( Main Program )*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
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
#*#*#*#*#*#*#*#*#*#*#**#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#
