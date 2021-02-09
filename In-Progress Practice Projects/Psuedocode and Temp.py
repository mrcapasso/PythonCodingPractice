#Potential Features List:
#Option for Custom Character String Pattern
#Option to center, left justify, right justify


#Psuedocode
#function: Pattern Display


        #Text + Pattern String Function
        #Print String (Small Size, medium size, large size)
        #pick desired string
            #small, medium, or large
                #paste to clipboard
                #exit loop 2
            #else
                #loop 2 again
    #Format another string? 
        #if no
            #exit loop 1


##Think of New Method b/c .center() only allows one character at a time
    #Use For Loop to pass through various values in string

import os, pyperclip

def patternFormatter(pattern, justification, length):
#Function Input Pre-Check
    if justification not in ['center','left','right']:
        raise AssertionError('Improper Justification Option')
    if length <= 0 or (length%1 != 0): #Checking for positive integer.
        raise AssertionError('Improper Length Option')
    if pattern == None:
        raise AssertionError('Improper Pattern') 
    #Function Code
    if justification == 'center':
        pattern.strip()
        pattern.center(1, ' ')
        finalString = pattern.center(length, pattern)
        return finalString
    elif justification == 'left':
        pattern.strip()
        pattern.center(1, ' ')
        finalString = pattern.ljust(length, pattern)
        return finalString
    else: #Right Justified Option
        pattern.strip()
        pattern.center(1, ' ')
        finalString = pattern.rjust(length, pattern)
        return finalString

print(patternFormatter('#*!', 'center', 30))