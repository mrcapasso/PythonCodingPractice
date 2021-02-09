#Goal: Create a program that will generate nice code comment spacers for blocking off coding segments.

import os, pyperclip

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
        like centered.
        ''')
        os.system('pause')
        clipboard = pyperclip.paste()
        if '\n' in clipboard: #User Input Check (Valid Choice Selection)
            raise Exception('Clipboard had multiple line text option')
        clipboard.strip()
        print(clipboard)
        verfication = input('Is this the desired text? (yes/no): ')
        if verfication.lower() == 'no' or verfication.lower() == 'esc':
            break #Restarting program.
        os.system('cls')
    