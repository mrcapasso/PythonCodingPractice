#Potential Features List:
#Option for Custom Character String Pattern
#Option to center, left justify, right justify
#Option for symmetry, think of dummy variables to simplify code
#Optimize Run-Time by replacing for loop in patternFormatter()


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

#############################################################################################################################(function testing)#############################################################################################################################            

import os, pyperclip

def patternFormatter(pattern, text, justification, length):
    #Function Input Pre-Check
    if justification not in ['center','left','right']:
        raise AssertionError('Improper Justification Option')
    if length <= 0 or (length%1 != 0): #Checking for positive integer.
        raise AssertionError('Improper Length Option')
    if pattern == None:
        raise AssertionError('Improper Pattern') 
    #*! Create Assertion to validate proper len of text and pattern
    #Function Code
    text.strip() #*? Not working? 
    text = '(' + text + ')'
    finalString = text
    if justification == 'center':
        for i in range(0, round(length/2)): #*! Modify upper limit to adjust accordingly
            finalString = pattern + finalString + pattern[::-1]
            #Reversed pattern is important for maintaining symmetry
        return finalString
    elif justification == 'left':
        finalString = '#' + finalString #Specific to left justified, mean't to prevent errors in compiling.
        for i in range(0, length): #*! Modify upper limit to adjust accordingly
            finalString = finalString + pattern[::-1]
        return finalString
    else: #Right Justified Option
        for i in range(0, round(((length-len(text))/len(pattern)))): #*! Modify upper limit to adjust accordingly
            finalString = pattern + finalString
        return finalString

a = patternFormatter('#', 'function testing', 'center', 250)
os.system('cls')
print(a)
print(len(a))