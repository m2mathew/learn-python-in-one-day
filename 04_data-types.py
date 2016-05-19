# Chapter 4: Data Types in Python

# Integers
# numbers with no decimal parts

userAge = 37
cityZip = 75034

# Float
# numbers that have decimal parts

userWeight = 199.9
numChildren = 3.0

# String
# can use single quotes or double quotes

name = 'Mike'
computer = 'I use a MacBookPro. I have a 17" older one and a 15" newer one. Both are snazzy and nifty.'
doggy = 'Chewie is a dog'
coolBeans = 'python is pretty neat'
mixedUp = '1a2b3c4d'
alphaFalse = '1super1'
digitTrue = '246810'

# String functions

# to uppercase
print(name.upper())
# count substring - it is case sensitive
print(computer.count('I'))
# return boolean depending on ending with specified suffix
print(doggy.endswith('dog'))
# find the index or return -1
print(coolBeans.find('neat'))
# index does the same thing except returns "ValueError" if index is not found
print(coolBeans.index('neat'))
# return true if all characters are alphanumeric and there is at least one character. Doesn't include whitespace.
print(mixedUp.isalnum())
# Return boolean depending on if all characters are alphabetic and there is at least one
print(alphaFalse.isalpha())
# Return boolean depending on if all characters are digits and there is at least one
print(digitTrue.isdigit())
