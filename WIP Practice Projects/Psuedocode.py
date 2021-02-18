import os, pyperclip

def patternFormatter(pattern, text, justification, length):
    #Parameter pre-check -- Start
    if str(pattern) != str(pattern): 
        #Pattern parameter type pre-check.
        raise AssertionError('Invalid pattern datatype.')
    if str(text) != str(text): 
        #Text parameter type pre-check.
        raise AssertionError('Invalid text datatype.')
    if len(str(pattern)) >= abs(int(length)) or len(str(text)) >= abs(int(length)):
        #Pattern AND text character length pre-check.
        raise AssertionError('Pattern or text is too long.')
    if justification not in ['center','left','right']: 
        #Justification parameter content AND type pre-check.
        raise AssertionError('Improper justification option.')
    if int(length) != abs(int(length)):
        #Length parameter value AND type pre-check.
        raise AssertionError('Length must be a natural number.')
    #Parameter pre-check -- End

    #Input formatting -- Start
    text = str(text) 
    pattern = str(pattern)
    length = int(length)
    text = text.strip()
    text = '(' + text + ')'
    finalString = text
    #Input formatting -- End

    #Center Justifying Portion -- Start
    if justification == 'center':
        charsForPattern = length - len(text)
        charPerSide = charsForPattern/2
        if charPerSide%len(pattern) == 0: #Nice case: aesthetic formatting. 
            for i in range(0, round(charPerSide/len(pattern))):
                finalString = pattern + finalString + pattern[::-1]
        else: #Ugly Case: Creates a slightly larger and centered string then truncates end.
            for i in range(0, round((charPerSide+1)/len(pattern))):
                finalString = pattern + finalString + pattern[::-1]
            finalString = finalString[0:length]
        return finalString
    #Center Justifying Portion -- End

    #Left Justifying Portion -- Start
    elif justification == 'left':
        unusedChars = length - len(text)
        if unusedChars%len(pattern) == 0: #Nice case: aesthetic formatting. 
            finalString = pattern + text + pattern*(int(unusedChars/len(pattern))-1)
            #Note, the minus one constant is because I added a pattern at the beginning of finalString
            #so in order to ensure proper sectioning, I reduced the multiplication at the end by one
        else: #Ugly Case: Creates a slightly larger string then truncates left portion.
            finalString = pattern*(round(unusedChars/len(pattern))+1)
            finalString = pattern + text + finalString
            finalString = finalString[0:length]
        return finalString
    #Left Justifying Portion -- End
    
    #Right Justifying Portion -- Start
    else:
        unusedChars = length - len(text)
        if unusedChars%len(pattern) == 0: #Nice case: aesthetic formatting. 
            finalString = pattern*int(unusedChars/len(pattern)) + text
        else: #Ugly Case: Creates a slightly larger string then truncates right portion.
            finalString = pattern*(round(unusedChars/len(pattern))+1)
            finalString = finalString[0:(length-len(text))] + text
        return finalString
    #Right Justifying Portion -- End

print(patternFormatter(234 , 456, 'center', '80'))

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
