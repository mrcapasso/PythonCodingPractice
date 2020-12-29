#Course: Automate the Boring Stuff with Python Programming
##Section 7: Dictionaries
##URL: https://www.udemy.com/course/automate/learn/lecture/3465848#overview

#Dictionaries (Lession 17)
#Values inside curly brackets are called key pairs.
eggs = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
eggs['size']
print('My cat has ' + eggs['color'] + ' fur.')

#Dictionaries are unordered.
#Dictionary are mutable like lists.
#Dictionaries contains unordered key-value pairs.

#You can check if key exists in dictionary value with in and not in. 

#Dictionary Methods
#Def: Tuples are essentially the same thing as lists, except they use parathensis instead of brackets and are immutable. 
#key(), outputs tuple
example1 = list(eggs.keys())
print(example1)

#values, outputs tuple
example2 = list(eggs.values())
print(example2)

#items(), outputs tuple
example3 = list(eggs.items())
print(example3)


#get(arg1, arg2) arg1 is the value to search for, arg2 is value to return if not in dictionary
print(eggs.get('age', 0))
    #This method is good to retrieve values in dictionary; however,
    #if the value doesnt exist we wont get an error message crashing the program.

#setdefault(), allows us to setdefault values for things not in the dictionary
    #Good to check if key exists. 

#Goal: Character count. Counts the number of characters in a string.

import pprint # Library for printing pretty things.

message = 'It was a bright cold day in April, and the clocks were striking thirteen'
demo = list(message)

print(demo)
histogram = {}
for character in message.upper():
    histogram.setdefault(character,0)
    histogram[character] = histogram[character] + 1

pprint.pprint(histogram)

# **pprint() returns pretty returns a dictionary value cleanly and pformat() function returns a string output of this value.



#Data Structure Video (lesson 18)
#A list of dictionaries is called a data-structure.

#Goal: Create a tic-tac-toe game using data structures, lists, and functions. 

#Type() function allows you to see type of function