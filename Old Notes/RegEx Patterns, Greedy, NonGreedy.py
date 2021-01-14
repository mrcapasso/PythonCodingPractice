import re

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

