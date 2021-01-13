#Author: Matteo Capasso
#Goal: Create a tic-tac-toe game using functions, data-structures, dictionaries, and lists. Purpose is to develop working familiarity with data structures, lists, and indexes.
#Documentation Note: Comments denoted #* require further review.

#*ToDo:
##*Fix attempts remaining showing wrong number
##*Fix Game loop so value error doesnt terimate
##*Consolidate text

import random
import sys

MAX_GAME_ATTEMPTS = 7 #The number of rounds the user has to guess the correct answer.
NUM_VALIDATION_ATTEMPTS = 3 #The number of invald data type enteries the user can attempt to enter.
LOW_RAND_NUM_LIM = 1 #The lower limit of the randomly generated number.
UP_RAND_NUM_LIM = 20 #The upper limit of the randomly generated number.

randomNumber = random.randint(LOW_RAND_NUM_LIM,UP_RAND_NUM_LIM)

#Name Inquiry
print('Hello! What is your name?')
name = input()
print("Welcome " + name + '.')


#Number Inquiry
for attempts in range(1,MAX_GAME_ATTEMPTS):
    print("Please input a whole number between 1 and 20.")
    number = input()
    
    #User Input Validation
    try: #Checking if user's integer input is between the random number bounds.
        numberAttempt = 0
        while int(number) not in range(LOW_RAND_NUM_LIM,UP_RAND_NUM_LIM):
            print('Input error, please enter a whole number between ' + str(LOW_RAND_NUM_LIM) +' and ' + str(UP_RAND_NUM_LIM) +'.')
            number = input()
            numberAttempt =+1
            if numberAttempt >= NUM_VALIDATION_ATTEMPTS and int(number) not in range(LOW_RAND_NUM_LIM,UP_RAND_NUM_LIM):
                print("Maximum invalid range attempts recieved, terminating program.")
                sys.exit()

    except ValueError: #Occurs when user inputs a non-integer value (Ex: a, #, 3.14159, 22/7)
        print("\n"*2 + str(sys.exc_info()))
        print('Program terminating -- only enter whole numbers between ' + str(LOW_RAND_NUM_LIM) + ' and ' + str(UP_RAND_NUM_LIM) + '.' + "\n"*2)
        sys.exit()

    except: #General error and exit.
        print("\n"*2 +str(sys.exc_info()))
        print('Program terminating.' + "\n"*2)
        sys.exit()

    #Game logic, compares error-checked user input to randomly generated number.
    if int(number) == randomNumber:
        print("Great job, you guessed correctly!")
        break
    elif int(number) > randomNumber:
        print('Nice try, but your guess was too high. You have ' + str(MAX_GAME_ATTEMPTS - attempts) + ' attempts remaining.')
    else:
        print('Nice try, but your guess was too low. You have ' + str(MAX_GAME_ATTEMPTS - attempts) + ' attempts remaining.')

print('Thanks for playing, ' + name + '. The random number was ' + str(randomNumber) + '.')
sys.exit()
