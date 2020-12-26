#Course: Automate the Boring Stuff with Python Programming
##Section 5: Writing a Complete Program: Guess the Number
##URL: https://www.udemy.com/course/automate/learn/lecture/3465826?start=0#overview

# Goal: Random Number game. Include: 7 tries max & error checking

import random
import sys

MAX_GAME_ATTEMPTS = 7
NUM_VALIDATION_ATTEMPTS = 3
LOW_RAND_NUM_LIM = 1
UP_RAND_NUM_LIM = 20

randomNumber = random.randint(LOW_RAND_NUM_LIM,UP_RAND_NUM_LIM)

#Name Inquiry
print('Hello! What is your name?')
name = input()
print("Welcome " + name + '.')


#Number Inquiry
for attempts in range(1,MAX_GAME_ATTEMPTS):
    print("Please input a number between 1 and 20.")
    number = input()
    
    #User Input Validation
  #  try: #Checking if user's integer input is between the random number bounds.
    numberAttempt = 0
    while int(number) not in range(1,20):
        print('Input error, please enter a number between ' + str(LOW_RAND_NUM_LIM) +' and ' + str(UP_RAND_NUM_LIM) +'.')
        number = input()
        numberAttempt = numberAttempt + 1
        if numberAttempt >= NUM_VALIDATION_ATTEMPTS:
             sys.exit()
        
   # except: #Checking if user inputed valid data type.
        #ToDo create loop w/ three attempts. 
   #     print('Data input error, exiting.')
   #     sys.exit() 

    #Game logic, compares user input to randomly generated number. Assumes correct user input.
    if int(number) == randomNumber:
        print("Great job, you guessed correctly!")
        break
    elif int(number) > randomNumber:
        print('Nice try, but your guess was too high. You have ' + str(MAX_GAME_ATTEMPTS - attempts) + ' attempts remaining.')
    else:
        print('Nice try, but your guess was too low. You have ' + str(MAX_GAME_ATTEMPTS - attempts) + ' attempts remaining.')
    

print('Thanks for playing, ' + name + '. The random number was ' + str(randomNumber) + '.')

