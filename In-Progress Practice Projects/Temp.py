#Goal: Create an email and phone number parser that takes clipboard input and outputs filtered phone numbers and emails to clipboard. 
#Tip: Use regex library, pyperclip

import re

def phoneNumParser(textsample): #Input: String to Parse || Output: List of Phone Numbers or lack of
    # Demo Number Formats: Source: (https://stdcxx.apache.org/doc/stdlibug/26-1.html) Pull Date: (1/21/2021)
    # 754-3010 Local
    # (541) 754-3010 Domestic
    # +1-541-754-3010 International
    # 1-541-754-3010 Dialed in the US
    # 001-541-754-3010n Dialed from Germany
    # 191 541 754 3010 Dialed from France   
    phoneNumRegex = re.compile(r'''
    ( ##Version with less groups, still needs to be fixed b/c wrong outputs
    \+?         #Checking for presence of +, used in international numbers
    \d{1,3}?    #Checking for three digit country-code , note -- sometimes less than 3 characters
    [ ]?|-?       #Checking for space or dash
    \(?         #Checking for potential left-parenthesis
    \d\d\d?     #Checking for three digit area code
    \)?         #Checking for potential right-parenthesis
    [ ]?|-?       #Checking for space or dash
    \d\d\d      #First part of 7-digit phone number
    [ ]?|-?       #Checking for space or dash
    \d\d\d\d    #Second part of 7-digit phone number
    )
    ''', re.VERBOSE) #Verbose to allow multi-line commenting
    phoneNumbers = phoneNumRegex.findall(textsample)
    if phoneNumbers == None:
        return 'No phone numbers.'
    else: 
        return phoneNumbers

###Main Program Psuedo Code###
#exit = false
#Loop Start on exit variable
#Clipboard pull, paste option, exit?
    #if clipboard
        #Reset clipboard loop's argument
        #Clipboard Loop
            #retrive clipboard input
            #paste clipboard sample text in terminal
            #Desire input?
                #if no
                        #please try again text, restarting
                #If yes 
                    #parse
                    #Output to clipboard
                    #also output to terimal in table like format
                    #Continue / More Parsing?
                    #if no
                        #clip board loop exit condition
                        #main program exit condition
    #elif paste option
        #clear terminal
        #user input string
        #parse
        #output to clipboard
        #also output to terimanl in table like format
    #else
        #exit = true
        #continue

test = '''
Junior EE Resume
1234 Resume Road, Binghamton, NY 12345
(123) 456-7890 | wcac@binghamton.edu

EDUCATION

Binghamton University, State University of New York, The Thomas J. Watson School of Engineering and Applied Science	                  
Bachelor of Science in Computer Science 					                                  Expected May 20XX 
Major GPA: 3.XX/4.00 | Overall GPA: 3.XX/4.00 | Dean’s List: Fall 20XX - Present
Onondaga Community College, State University of New York		 +1-541-754-3010					         
Associate of Science in Individual Studies		                                                                                          May 20XX Overall GPA: X.X/4.00 | Presidential Scholar 

TECHNICAL SKILLS
Languages: MATLAB, C++, C, X-86 Assembly 001-541-754-3010
Software and OS: LabWindows/CVI, Logisim, P-Spice, LabVIEW, Microsoft Suite (Word, Excel, Project), Linux, OS 10
Additional: Digital Circuit Design, Soldering
Spoken Language: Spanish 754-3010



PROFESSIONAL EXPERIENCE

Lawrence Aerospace – Liquids Dynamic Division                                                                                          New York, NY
Firmware Intern 									            June 20XX – August 20XX
•	Utilized object-oriented programming and GUI concepts to develop an application in Visual C# that decodes 128KB of raw data from the Non-Volatile Memory into readable information to reduce errors in packet data transmissions and decoding 
•	Devised test procedures of both high and low level program requirements of the Bombardier C-Series main fuel-gauging computer to validate software requirements to be used by quality assurance engineers and the customer
Watson Career and Alumni Connections							              Binghamton, NY
Student Assistant								          September 20XX – December 20XX
•	Advised students on preparing quality application materials, and provide constructive feedback to strengthen the professionalism skills necessary for a successful and rewarding career path
•	Coordinated networking events and information sessions to assist students with connecting with engineering professionals
•	Organized the layout and content of the career services website using OmniUpdate to provide resources and opportunities for students and alumni of Watson School of Engineering and Applied Science

PROJECT EXPERIENCE
Junior Design Project: Temperature Control System						              Binghamton, NY
Team Leader		1-541-754-3010								           January 20XX – May 20XX
•	Led a team of four engineers to model a temperature controller that regulates temperature of a cement power resistor using voltage divider, 2-bit flash ADC, binary comparisons, and transistor circuit concepts
•	Tested flash ADC conversion of the varying thermistor in order to utilize appropriate resistance values and choose reference voltage for the op-amp comparators of the flash ADC that will maximize temperature resolution
Multipath Issues in Communication Systems								 Binghamton, NY Lead Developer									          September 20XX – December 20XX
•	Simulated communication scenarios involving multiple received signals due to environment, delay, and noise in MATLAB in order to create filters that would obtain the desired discrete-time input signal from the altered signal
•	Analyzed the multipath system’s frequency response and its effects on the original input signal to implement FIR and IIR filters that will attenuate unwanted frequencies and amplify the desired frequencies
“Mine-Field” Navigating Robot								              Binghamton, NY
Team Member		 				 		                       September 20XX – December 20XX
•	Designed assembly code in Code Warrior using a MC9S08QG8 CPU, a robot kit, and servos to create a robot that navigated a “mine-field” to detect light sensors and press the button to “disarm” the mines
•	Developed technical problem solving skills through the use of pulse-width modulation and subroutine concepts in assembly code to implement hardware and software applications

LEADERSHIP EXPERIENCE & CAMPUS INVOLVEMENT
Binghamton Nicaragua Initiative (BNI)								              Binghamton, NY
Treasurer 				            				                                         January 20XX – Present
•	Generate over $1,500 in donations to fund construction of a houses in Nicaragua through soliciting family, friends, as well as the student body at campus-wide events
•	Cultivate language and communication skills during multiple trips to Nicaragua by contributing on the construction of houses and traveling with native around the cities of Managua, Leon, and Granada
'''

print(phoneNumParser(test))