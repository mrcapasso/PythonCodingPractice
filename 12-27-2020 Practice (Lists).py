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
test = list('Bob is my favorite person')
print(test)
