#Goal: Create a program that will generate nice code comment spacers for blocking off coding segments.

import os, pyperclip, pprint
from Psuedocode import patternFormatter #*Operational, but still needs to be optimized

patterns = {'0':'Custom Pattern','1':'#*!', '2':'#*?', '3':'#'}

exit = False
while exit == False:
    os.system('cls')
    print('\nWelcome to the pretty comment spacers script.\n\n' + '-'*80)
    pprint.pprint(patterns, width=1)
    print('-'*80 + "\n" + 'Please choose the number corresponding to your desired pattern.')
    patternNum = input('\nNumber: ')

    #User Input Validation -- Start
    patternsKeyList = []
    for keys in patterns.keys():
        patternsKeyList.append(keys)
    if patternNum not in patternsKeyList:
        raise Exception('Invalid Pattern Selection Number')
    #User Input Validation -- End
    
    #Special Condition Handling (User Inputed Value for Pattern) -- Start
    if int(patternNum) == 0:
        patternType = input('Please enter you desired pattern: ')
    else:
        patternType = patterns.get(patternNum)
    #Special Condition Handling (User Inputed Value for Pattern) -- End

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
    verfication = input('Is this the text you want formatted? (yes/no): ')
    if verfication.lower() == 'no':
        clipboard = input('\nType the text you want formatted: ')
    os.system('cls')
    justOptions = ['left', 'center', 'right']
    justification = input('Please choose a text justification.\n' + str(justOptions) + ': ')
    os.system('cls')
    if justification not in justOptions:
        raise Exception('Not a valid justification option.')
    standardOption = patternFormatter(patternType, clipboard, justification, 80)
    pyperclip.copy(standardOption)
    print(
        'Small):\n' + patternFormatter(patternType, clipboard, justification, 40) + "\n" + 
        'Standard):\n' + standardOption + "\n" +
        'Large):\n' + patternFormatter(patternType, clipboard, justification, 120) + "\n"*2 +
        'Note: The standard option was copied to your clipboard by default.\n'
    )
    os.system('pause')
    if input('Would you like to exit the program? (yes/no): ').lower() == 'yes':
        exit = True