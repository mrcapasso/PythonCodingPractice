#Author: Matteo Capasso
#Goal: Create a program that will generate nice code comment spacers for blocking off coding segments.

import os, pyperclip, pprint

def patternFormatter(pattern, text, justification, length): #Outputs formatted string of text and pattern.
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

patterns = {'0':'Custom Pattern','1':'#!', '2':'#?', '3':'#'}

exit = False
while exit == False:
    #Welcome Screen & Pattern Option Selection -- Start
    os.system('cls')
    print('\nWelcome to the pretty comment spacers script.\n\n' + '-'*80)
    pprint.pprint(patterns, width=1)
    print('-'*80 + "\n" + 'Please choose the number corresponding to your desired pattern.')
    patternNum = input('\nNumber: ')
    #Welcome Screen & Pattern Option Selection -- End

    #User's Pattern Input Validation -- Start
    patternsKeyList = []
    for keys in patterns.keys():
        patternsKeyList.append(keys)
    if patternNum not in patternsKeyList:
        raise Exception('Invalid Pattern Selection Number')
    #User's Pattern Input Validation -- End
    
    #Special Conditionality Handling (Option 0) -- Start
    if int(patternNum) == 0:
        patternType = input('Please enter you desired pattern: ')
    else:
        patternType = patterns.get(patternNum)
    #Special Conditionality Handling (Option 0) -- End

    #Clipboard Text Retrival -- Start
    os.system('cls')
    print('''
    Please take this oppurtunity to copy 
    the single line of text you would 
    like modifiyed to your clipboard.
    ''')
    os.system('pause')
    os.system('cls')
    clipboard = pyperclip.paste()
    clipboard.strip()
    print(clipboard + "\n")
    #Clipboard Text Retrival -- End

    #Clipboard Input Validation & Text Justification Retrival -- Start
    verfication = input('Is this the text you want formatted? (yes/no): ')
    if verfication.lower() == 'no':
        clipboard = input('\nType the text you want formatted: ')
    os.system('cls')
    justOptions = ['left', 'center', 'right']
    justification = input('Please choose a text justification.\n' + str(justOptions) + ': ')
    os.system('cls')
    if justification not in justOptions:
        raise Exception('Not a valid justification option.')
    #Clipboard Input Validation & Text Justification Retrival -- End

    #Formatted Text Print and Copying to Clipboard -- Start
    standardOption = patternFormatter(patternType, clipboard, justification, 80)
    pyperclip.copy(standardOption)
    print(
        'Small):\n' + patternFormatter(patternType, clipboard, justification, 40) + "\n" + 
        'Standard):\n' + standardOption + "\n" +
        'Large):\n' + patternFormatter(patternType, clipboard, justification, 120) + "\n"*2 +
        'Note: The standard option was copied to your clipboard by default.\n'
    )
    os.system('pause')
    #Formatted Text Print and Copying to Clipboard -- End

    if input('Would you like to exit the program? (yes/no): ').lower() == 'yes':
        exit = True