#Goal: Create an email and phone number parser that takes clipboard input and outputs filtered phone numbers and emails to clipboard. 
#Help List: Consulted Automate the Boring Stuff to figure out extracting individual elements from n-tuple
#Tip: Use regex library, pyperclip

#ToDo
#*Bug test clipboardSampleText()
#*Import pyperclip
#*Inset pyperclip into main body function
#*Narrow down phoneNumParser tuples to first group & create list with it

import re #Used in phoneNumParser() and emailParser() for parsing
import pprint #Used in main function to format parsed lists
import os #os.system('cls'), os.system('pause')
import sys #sys.exit(), str(sys.exc_info())
#import pyperclip

def phoneNumParser(textsample): #Input: String to Parse || Output: List of Phone Numbers or lack of
    # Demo Number Formats: Source: (https://stdcxx.apache.org/doc/stdlibug/26-1.html) Pull Date: (1/21/2021)
    # 754-3010 Local
    # (541) 754-3010 Domestic
    # +1-541-754-3010 International
    # 1-541-754-3010 Dialed in the US
    # 001-541-754-3010 Dialed from Germany
    # 191 541 754 3010 Dialed from France   
    phoneNumRegex = re.compile(r'''
    (
    (\+)?               #Checking for presence of +, used in international numbers
    (\d{1,3})?          #Checking for three digit country-code , note -- sometimes less than 3 characters
    (\ |-)?             #Checking for space or dash
    (\()?               #Checking for potential left-parenthesis
    (\d\d\d)?           #Checking for three digit area code
    (\))?               #Checking for potential right-parenthesis
    (\ |-)?             #Checking for space or dash
    (\d\d\d)            #First part of 7-digit phone number
    (\ |-)?             #Checking for space or dash
    (\d\d\d\d)          #Second part of 7-digit phone number
    (\s(ext.|extension) \ \d*)? #'ext.' or 'extension' followed by digits
    )
    ''', re.VERBOSE) #Verbose to allow multi-line commenting
    phoneNumbers = phoneNumRegex.findall(textsample)
    if phoneNumbers == None:
        return 'No phone numbers.'
    else: 
        return ['754-3010', '(541) 754-3010', '001-541-754-3010', '1-541-754-3010'] #* dummy/temp list

def emailParser(textsample): #Input: String to Parse || Output: List of Emails or lack of
    emailRegex = re.compile(r'''
    \S+ #Non-space values, used to include weird characters and numbers
    @   #Required @ to signify beginning of domain section for email addresses
    \S+ #Non-space values, used to include weird characters and numbers
    .   #Required '.' character to signify start of domain type for email addresses
    \S+ #Non-space values, used to include weird characters and numbers
    ''', re.VERBOSE)
    emails = emailRegex.findall(textsample)
    if emails == None:
        return 'No emails.'
    else:
        return emails

def clipboardSampleText(textsample): #Input: String to Parse || Output: String that contains splices of main text's body for user verification
    characterLength = 30 #Integer value representing the approx, unoptimized, number of characters needed to give the user an identifiable segment of text
    textLength = len(textsample)
    first = textsample(0, characterLength)
    firstQuartile = textsample(.25*textLength, characterLength + (.25*textLength))
    middle = textsample(.5*textLength, characterLength + (.5*textLength))
    thirdQuartile = textsample(.75*textLength, characterLength + (.75*textLength))
    last = textsample(textLength - characterLength, textLength)
        #*Check no overlap between thirdQuartile and last
    sampleText = str(first + firstQuartile + middle + thirdQuartile + last)
    return sampleText
    
#Main Program
test = '''
Junior EE Resume
1234 Resume Road, Binghamton, NY 12345
(123) 456-7890 | wcac@binghamton.edu
Binghamton University, State University of New York, The Thomas J. Watson School of Engineering and Applied Science	                  
Bachelor of Science in Computer Science 					                                  Expected May 20XX 
Major GPA: 3.XX/4.00 | Overall GPA: 3.XX/4.00 | Dean’s List: Fall 20XX - Present
Onondaga Community College, State University of New York		 +1-541-754-3010					         
Associate of Science in Individual Studies		                                                                                          May 20XX Overall GPA: X.X/4.00 | Presidential Scholar 
TECHNICAL SKILLS
Languages: MATLAB, C++, C, X-86 Assembly 001-541-754-3010
Software and OS: LabWindows/CVI, Logisim, P-Spice, LabVIEW, Microsoft Suite (Word, Excel, Project), Linux, OS 10
Additional: Digital Circuit Design, wcac@binghamton.eduSoldering
Spoken Language: Spanish 754-3010
Lawrence Aerospace – Liquids Dynamic Division                                                                                          New York, NY
Firmware Intern 				wcac@binghamton.edu					            June 20XX – August 20XX
•	Utilized object-oriented programming and GUI concepts to develop an application in Visual C# that decodes 128KB of raw data from the Non-Volatile Memory into readable information to reduce errors in packet data transmissions and decoding 
•	Devised test procedures of both high and low level program requirements of the Bombardier C-Series main fuel-gauging computer to validate software requirements to be used by quality assurance engineers and the customer
Watson Career and Alumni Connections							              Binghamton, NY
Student Assistant								          September 20XX – December 20XX
Junior Design Project: Temperature Control System						              Binghamton, NY
Team Leader		1-541-754-3010								           January 20XX – May 20XX
Multipath Issues in Communication Systems								 Binghamton, NY Lead Developer									          September 20XX – December 20XX
•	Simulated communication scenarios involving multiple received signals due to environment, delay, and noise in MATLAB in order to create filters that would obtain the desired discrete-time input signal from the altered signal
•	Analyzed the multipath system’s frequency response and its effects on the original input signal to implement FIR and IIR filters that will attenuate unwanted frequencies and amplify the desired frequencies
“Mine-Field” Navigating Robot								              Binghamton, NY
Team Member		 				 		abc##@binghamton.edu                       September 20XX – December 20XX
•	Designed assembly code in Code Warrior using a MC9S08QG8 CPU, a robot kit, and servos to create a robot that navigated a “mine-field” to detect light sensors and press the button to “disarm” the mines
•	Developed technical problem solving skills through the use of pulse-width modulation and subroutine concepts in assembly code to implement hardware and software applications
LEADERSHIP EXPERIENCE & CAMPUS INVOLVEMENT
Binghamton Nicaragua Initiative (BNI)								              Binghamton, NY
Treasurer 				            				                                         January 20XX – Present
•	Generate over $1,500 in donations to fund construction of a houses in Nicaragua through soliciting family, friends, as well as the student body at campus-wide events
•	Cultivate language and communication skills during multiple trips to Nicaragua by contributing on the construction of houses and traveling with native around the cities of Managua, Leon, and Granada
'''

try: 
    failedInputs = 0
    exit = False
    while exit == False:
        os.system('cls') #Clear previous terminal gunk
        print('''
        Welcome to the phone and email puller!
        Please choose how you would like to input text to parse.

        1) Copy current clipboard's text, type: clipboard
        - or -
        2) Exit program, type: exit

        ''')
        retrivalOption = input().lower()
        if (retrivalOption == 'clipboard') or (retrivalOption == 'clip'):
            print('Clipboard chosen')
            os.system('pause')
            textVerification = False
            while textVerification == False:
                userText = test #* temp variable to simulate pyperclip clipboard copy, replace test with pyperclip copying from clipboard
                print(clipboardSampleText(userText))
                sampleTextVerf = input('Does this text ressemble the text you desire to parse? (yes/no): ').lower()
                if sampleTextVerf == 'no':
                        os.system('cls')
                        print('''
                        Please take this oppurtuninty to re-copy the 
                        text you wish to parse to your clipboard.

                        Note -- 'Ctrl+C' is the keyboard shortcut to copy text.
                        ''')
                        os.system('pause')
                else:
                    os.system('pause') #* remove
                    phoneList = phoneNumParser(userText)
                    emailList = emailParser(userText)
                    #* Output phoneList to clipboard here using pyperclip
                    print('Phone List:' + "\n" + phoneList + "\n" + 'The list of phone numbers has been updated in your clipboard.' \
                         + "\n" + 'Please paste in the appropriate document now.')
                    os.system('pause')
                    #* Output emailList to clipboard here using pyperclip
                    print('Email List:' + "\n" + emailList + "\n" + 'The list of emails has been updated in your clipboard.' \
                         + "\n" + 'Please paste in the appropriate document now.')
                    os.system('pause')
                    #* Continue / More Parsing?
                    #* if input("\n" + 'Would you like to exit the program? (yes/no): ').lower() == 'no':
        elif (retrivalOption == 'exit') or (retrivalOption == 'esc'):
            exit = True
        else:
            failedInputs += 1
            if failedInputs >= 3:
                print('Max input attempts reached. Exiting Program.')
                os.system('pause')
                exit = True
            else:
                print("\n" + 'This is an incorrect entry, please re-read the directions.')
                os.system('pause')
                continue            
except:
    print(str(sys.exc_info()))
    print("\n" + 'Critical Error in main function -- terminating program.' + "\n")
    os.system('pause')
    os.system('cls')
