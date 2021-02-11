#Find #! for remaining fixes. 

import os, pyperclip

def patternFormatter(pattern, text, justification, length):
    if justification not in ['center','left','right']:
        raise AssertionError('Improper Justification Option')
    if length <= 0 or (length%1 != 0): #Checking for positive integer.
        raise AssertionError('Improper Length Option')
    if pattern == None:
        raise AssertionError('Improper Pattern') 
    #! Check if assertion style is correct
    #! Add assertion if text is too long
    #! Add assertion if pattern is too long 
    text = text.strip()
    text = '(' + text + ')'
    finalString = text
    if justification == 'center':
        charsForPattern = length - len(text)
        charPerSide = charsForPattern/2
        if charPerSide%len(pattern) == 0: #Checking for formatting niceness.
            for i in range(0, round(charPerSide/len(pattern))):
                finalString = pattern + finalString + pattern[::-1]
                #Reversed pattern is important for maintaining symmetry
        else: #Ugly Case: Creates a slightly larger&centered string, then truncates end.
            for i in range(0, round((charPerSide+1)/len(pattern))):
                finalString = pattern + finalString + pattern[::-1]
            finalString = finalString[0:length]
        return finalString
    elif justification == 'left':
        unusedChars = length - len(text)
        if unusedChars%len(pattern) == 0: #Nice Case
            finalString = pattern + text + pattern*(int(unusedChars/len(pattern))-1)
            #Note, the minus one here is because I added a pattern at the beginning of finalString
            #so in order to ensure proper sectioning I reduced the multiplication at the end
        else: #Ugly Case, here I create a slightly larger string then truncate.
            finalString = pattern*(round(unusedChars/len(pattern))+1)
            finalString = pattern + text + finalString
            finalString = finalString[0:length]
        return finalString
    elif justification == 'right':
        unusedChars = length - len(text)
        if unusedChars%len(pattern) == 0: #Nice Case
            finalString = pattern*int(unusedChars/len(pattern)) + text
        else: #Ugly Case, here I create a slightly larger string then truncate.
            finalString = pattern*(round(unusedChars/len(pattern))+1)
            finalString = finalString[0:(length-len(text))] + text
        return finalString


#Stress Test, Checking Conditions
# import random
# randomIndex = random.randint(1,100)
# randomIndexSmall = random.randint(0,3)
# justification = ['right', 'center', 'left']

# patternList = []
# for i in range(1,101):
#     patternList.append('#*!'*i)

# for i in range(1,100):
#     print(
#         patternFormatter(patternList[randomIndex], 'Section', 'center', 80)
#       )
