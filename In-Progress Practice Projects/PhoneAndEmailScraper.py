#Goal: Create an email and phone number parser that takes clipboard input and outputs filtered phone numbers and emails to clipboard. 
#Tip: Use regex library, pyperclip

###PsuedoCode###

#Functions:
    #parse
        #phone numbers
        #emails
    #formatted list printing

#Main Program
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



        