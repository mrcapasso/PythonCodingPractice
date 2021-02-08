#Author: Matteo Capasso
#Project Goal: Create a script that tells you how large a folder's contents are. 
#Project Idea Source: Automate the Boring Stuff Udemy Lecture Series

import os, traceback

os.system('cls')
print('Welcome to the file size calculator!')
targetFile = input('Please input the filepath of the directory whose contents you would like checked:\n')
if os.path.exists(targetFile) == True:
    os.chdir(targetFile) #Changes working directory to target file directory
    totalSize = 0 
    for foldername, subfolders, filenames in os.walk(targetFile):
        os.chdir(foldername)
        for i in filenames:
            ithFileSize = os.path.getsize(os.path.abspath(i)) #Storing ith filesize to variables
            totalSize += ithFileSize
    print("\n" + '='*30 + "\n" + 'Total Size: ' + str(totalSize) + ' bytes')
    print('Total Size: ' + str(round((totalSize/1000),3)) + ' kb')
    print('Total Size: ' + str(round((totalSize/1000000),3)) + ' Mb')
    print('Total Size: ' + str(round((totalSize/1000000000),3)) + ' Gb')
    print()
else:
    raise Exception('Nonexistent file or directory.')
