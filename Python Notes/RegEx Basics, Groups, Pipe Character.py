#Section 10: Regular Expressions, Chapter 23: 'Regular Expression Basics' 
##Automate the Boring Stuff: https://www.udemy.com/course/automate/learn/lecture/3465866

#Recap:
## Regular expressions are mini-language for specifying text patterns. Writing code to do pattern matching without regular expressions is a huge pain.
## Regex strings often use backslashes (like \d), so they are often written using raw strings: r'\d'
## \d is the regex for a numeric digit character.
## Import the re module first.
## Call the re.compile() function to create a regex object.
## Call the regex object's search() method to create a match object.
## Call the match object's group() method to get the matched string.


#Section 10: Regular Expressions, Chapter 24: 'Regex Groups and the Pipe Character' 
##Automate the Boring Stuff: https://www.udemy.com/course/automate/learn/lecture/3470506

#Recap:
## Groups are created in regex strings with parentheses.
## The first set of parentheses is group 1, the second is 2, and so on.
## Calling group() or group(0) returns the full matching string, group(1) returns group 1's matching string, and so on.
## Use \( and \) to match literal parentheses in the regex string.
## The | pipe can match one of many possible groups.