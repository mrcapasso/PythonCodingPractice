#Section 10: Regular Expressions, Chapter 25: 'Repetition in Regex Patterns and Greedy/Nongreedy Matching' 
##Automate the Boring Stuff: https://www.udemy.com/course/automate/learn/lecture/3470510

import re

#RegEx Group and ? Example:
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 415-555-1234. \
    Call me tomorrow.')
mo.group() #Outputs: 415-555-1234
mo = phoneRegex.search('My phone number is 555-1234. \
    Call me tomorrow.')
mo == None #Outputs: True
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d\-\d\d\d\d')
mo = phoneRegex.search('My phone number is 555-1234. \
    Call me tomorrow.')
mo.group() #Outputs: 555-1234

#RegEx * (aka Star) Example:
#Recall: * denotes an occurence of zero or more times 
batRegex = re.compile(r'Bat(wo)*man')
batRegex.search(r'The Adventures of Batwoman')
    #Outputs:<re.Match object; span=(18, 26), match='Batwoman'>
batRegex.search(r'The Adventures of Batwowowowoman') 
    #Outputs: <re.Match object; span=(18, 32), match='Batwowowowoman'>


#RegEx + (aka Plus) Example:
#Recall: + denotes an occurence of once or more times
batRegex = re.compile(r'Bat(wo)+man')
batRegex.search(r'The Adventures of Batwowowowoman')
    #Outputs: <re.Match object; span=(18, 32), match='Batwowowowoman'>


#Escaping ?,*, and +
#Recall: We use \ to 'escape' these specific characters
regex = re.compile(r'\+\*\?')
regex.search(r'I learned about +*? regex syntax')
    #Outputs: <re.Match object; span=(16, 19), match='+*?'>


#RegEx {x} ('x' amount of times) Example:
haRegex = re.compile(r'(Ha){3}')
haRegex.search('He said "HaHaHa"')
    #Outputs: <re.Match object; span=(9, 15), match='HaHaHa'>


#RegEx {x,y} (max and min repetitions)
#Note, RegEx by default uses greedy matching.
haRegex = re.compile(r'(Ha){3,5}')
haRegex.search('He said "HaHaHa"')
    #Outputs: <re.Match object; span=(9, 15), match='HaHaHa'>
haRegex.search('He said "HaHaHaHaHaHaHaHaHa"')
    #Outputs: <re.Match object; span=(9, 19), match='HaHaHaHaHa'>
digitRegex = re.compile(r'(\d){3,5}') #Note, indexing notation in {}
digitRegex.search('123456789')
    #Outputs: <re.Match object; span=(0, 5), match='12345'>
#Non-Greedy Variant -> Will match smallest string.
digitRegex = re.compile(r'(\d){3,5}?') #Note the ?
digitRegex.search('123456789')
    #Outputs: <re.Match object; span=(0, 3), match='123'>


#Recap
## The ? says the group matches zero or one times.
## The * says the group matches zero or more times.
## The + says the group matches one or more times.
## The curly braces can match a specific number of times.
## The curly braces with two numbers matches a minimum and maximum number of times.
## Leaving out the first or second number in the curly braces says there is no minimum or maximum.
## "Greedy matching" matches the longest string possible, "nongreedy matching" (or "lazy matching") matches the shortest string possible.
## Putting a question mark after the curly braces makes it do a nongreedy/lazy match.
