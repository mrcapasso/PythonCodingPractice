#Goal: Reverse a string


import os


string = 'bob the snob wants a fancy job. please hire me -- thanks'
stringList = list(string)

reverseList = []
for i in range(1, len(stringList)):
    reverseList.append(stringList[-i])

empty = ''
print(empty.join(reverseList))