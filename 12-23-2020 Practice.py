#Course: Automate the Boring Stuff with Python Programming
##Section 5: Writing a Complete Program: Guess the Number
##URL: https://www.udemy.com/course/automate/learn/lecture/3465826?start=0#overview

# Goal: Random Number game. Include: 7 tries max & error checking

import random


MAXGAMEATTEMPTS = 7
NUMVALIDATIONATTEMPTS = 3
LOWERRANDNUMLIMIT = 1
UPPERRANDNUMLIMIT = 20

randomNumber = random.randint(LOWERRANDNUMLIMIT,UPPERRANDNUMLIMIT)

#Name Inquiry
print('Hello! What is your name?')
name = input()
print("Welcome " + name + '.')


#Number Inquiry
for attempts not in range(0,MAXGAMEATTEMPTS):
    print("Please input a number between 1 and 20.")
    number = input()

    #User Input Validation
    for number not in range(LOWERRANDNUMLIMIT, UPPERRANDNUMLIMIT):
        print('Input error, please enter a number between ' str(LOWERRANDNUMLIMIT) +'and ' + str(UPPERRANDNUMLIMIT) +'.')
        number = input()
        numberAttempt = numberAttempt + 1
        if numberAttempt >= NUMVALIDATIONATTEMPTS:
            print("Please learn to read.")
            exit

    #Game logic, compares user input to randomly generated number.
    if number == randomNumber:
        print("Great job, you guessed correctly!")
        break
    elif number > randomNumber:
        print('Nice try, but your guess was too high. You have ' + str(MAXGAMEATTEMPTS - attempts) + ' attempts remaining')
    else:
        print('Nice try, but your guess was too low. You have ' + str(MAXGAMEATTEMPTS - attempts) + ' attempts remaining')
    attempts = attempts + 1

print("Random number was " + str(randomNumber))

