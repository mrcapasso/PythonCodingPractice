#Goal: Create a program that will generate nice code comment spacers for blocking off coding segments.

import os, pyperclip
from Psuedocode import patternFormatter #*Operational, but still needs to be optimized

pattern1 = '#*!' #Notification base pattern
pattern2 = '#*?' #Question base pattern
pattern3 = '#'   

exit = False
while exit == False:
    os.system('cls')
    print('Welcome to the pretty comment spacers script.\n\n\
    Please choose a pattern type:\n\
    1) %s \n\
    2) %s \n\
    3) %s \n' % (pattern1, pattern2, pattern3))
    patternType = input('(1,2,3): ')
    if int(patternType) not in range(1,3): #User Input Check (Valid Choice Selection)
        raise Exception('Invalid Pattern Selection Number')
    clipboardLoopExit = False
    while clipboardLoopExit == False:
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
        if input('Would you like to exit? (yes/no): ').lower() is 'yes':
            clipboardLoopExit = True
            exit = True
            break