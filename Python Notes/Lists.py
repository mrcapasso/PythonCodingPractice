#Course: Automate the Boring Stuff with Python Programming
##Section 6: Lists
##URL: https://www.udemy.com/course/automate/learn/lecture/3465830#overview

#Index => Single item
example = ['demo1', 'demo2', 'demo3']
print(example[0])

#Slice => New Sublist
example = [['demo1', 'demo2', 'demo3'],['bob', 'susan', 'jack'], ['bob2', 'susan2', 'jack2']]
print(example[1:2]) 

#Note possible redefine list and sublist items like variables.

#Helpful Examples
example = ['demo1', 'demo2', 'demo3', 'demo4', 'demo5', 'demo6']
print(example[-2]) #second entry from end of list
    #Note, -1 refers to last item in a list! Not -0 or something like that.

example = ['demo1', 'demo2', 'demo3', 'demo4', 'demo5', 'demo6']
print(example[:2]) #beginning of list to index 2

example = ['demo1', 'demo2', 'demo3', 'demo4', 'demo5', 'demo6']
print(example[2:]) #index 2 to end of list


#Del Statement => Unassigns values from list
example = ['demo1', 'demo2', 'demo3', 'demo4', 'demo5', 'demo6']
del example[1:] #deletes/unassigns list entries
print(example)

#String and List Similarities
example = ['demo1', 'demo2', 'demo3', 'demo4', 'demo5', 'demo6']
print(len('BobDaniel'))
print(len(example))

print([1,2,3] + [1,2,3]) #Concatenation
print([1,2]*10) #Multiplication

#List Function, Changes string to list
test = list('Bob is my favorite person') #turns each character into a list entry
print(test)

#Note: 'For' loops iterate over the values in a list

#Multiple Assignments
cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
    # or, we can write it as such:
size, color, disposition = cat
print(cat)

#Augmented Operators (can be used for common opertors):
spam = 42
spam = spam +1
    # or, we can write it as such:
spam += 1
print(spam)

#Def: Methods are functions that are "called on" values.
        #The listed methods below operate on the list "in place", rather than returning a new list value.

#Return Specifc List Value (Using a 'method')
test = list('Bob is my favorite person') #turns each character into a list entry
test.index('b') # Looks for 'bob' in a list

#Appends to end of list ("list method")
spam = cat = ['fat', 'orange', 'loud']
spam.append('Giant')
print(spam)

#Inserts to begnning of list ("list method")
spam = ['fat', 'orange', 'loud']
spam.append('Giant')
print(spam)

#Removes first occurence of that value from anywhere in list ("list method")
spam = ['fat', 'orange', 'loud']
spam.remove('fat')
print(spam)


#Sorts list of values using ASCII-beltical, applies to numeric and letters ("list method")
spam = ['fat', 'orange', 'loud']
spam.sort()
print(spam)
    #we can sort in reverse order using spam.sort(reverse=True)
    #spam.sort(key=str.lower) to sort in true alphateical order


#Mutable and Immutable
#Note: Python distinguishes between the two to maximize performance,
#Mutable => changeable, (lists) stores references to that list inside variable
#Immutable => not changeable, such as a string and tuples

#Note: The difference between immutable and mutable comes down to references.
    #Mutuable values are NOT stored in variable, but rather referenced when variable is used.
        #Note, if youre not carful it is easy to create bugs when refrencing mutuable values under different variable names.
    #Immutable values do not have the above problem, they are variable specific. 

#For more info on references in Python, see Facts and Myths about Python names and values: https://www.youtube.com/watch?v=_AEJHKGk9ns

#Note: Changes to list in a function will affect the list outside the function.

#Copy Module (Used to easily navigate around the mutable vs immutable data types)
import copy
    #Creates brand NEW list and returns references to new list. 
spam = ['A', 'B', 'C','D']
cheese = copy.deepcopy(spam) #Creates brand new list off spam list and references it to cheese.
cheese[1] = 42
print(spam)
print(cheese)

#Line Continuation
spam = ['apples',
        'oranges',
        'bananas',
        'cats,']
    #Python recognizes this with \ (line continutes on next line, ignore indendation.)
