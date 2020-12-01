#Course: Automate the Boring Stuff with Python Programming
##Section 4: Handling Errors with try/except. 
##URL: https://www.udemy.com/course/automate/learn/lecture/3465822#overview


# Goal: Input cats, print statement, error check for issues.

print('How many cats do you have?')
manyCats = input()
try:
    if int(manyCats) >= 4:
        print('That is a lot of cats!')
    elif int(manyCats) >=0:
        print('That is not so many cats.')
    elif int(manyCats) <=0:
        print('Cannot have negative or zero cats')
except ValueError:
    print('Error')