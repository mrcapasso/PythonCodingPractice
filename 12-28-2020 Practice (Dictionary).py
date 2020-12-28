#Course: Automate the Boring Stuff with Python Programming
##Section 7: Dictionaries
##URL: https://www.udemy.com/course/automate/learn/lecture/3465848#overview


#Values inside curly brackets are called key pairs.
eggs = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
eggs['size']
print('My cat has ' + eggs['color'] + ' fur.')

#Dictionaries are unordered.
#Dictionary are immutuable like lists.

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
# ~12:57 left on video
