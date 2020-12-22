#Course: Automate the Boring Stuff with Python Programming
##Section 5: Writing a Complete Program: Guess the Number
##URL: https://www.udemy.com/course/automate/learn/lecture/3465826?start=0#overview

# Goal: Random Number game. 


import random

# Number Inquiry Function Creation (w/ Input Error Checking)
def inputNumber():
    validation = input()
    while validation == ' ':
        print('You did not enter a number, please try again!')
        validation = input()
    
    return number

# Name inquiry
print('What is your name?')
name = input()

# Number Inquiry Text
print('Hello ' + name +'!')
print('Guess a number between 0 and 10.')
inputNumber()

# Random Number Generator Variable Generation
randomNumber = random.randint(0,10)


while number != randomNumber:    

    if number > randomNumber:
        print('Your number is too high, please try again!')
        inputNumber()

    elif number < randomNumber:
        print('Your number is too low, please try again!')
        inputNumber()
    else:
        break
    

print('Great job, the number was:' + str(randomNumber))



## This is spaghetti code. Please change to include a limited amount of tries and error validation using truthy and falsey values. - matteo