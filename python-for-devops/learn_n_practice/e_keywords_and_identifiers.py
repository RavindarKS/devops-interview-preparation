# Keyword is a word that is reserved by a program because the word has a special meaning.

# It can not be used as a variable names. Keywords can be commands or parameters.

# NOTE: Python is a case sensitive programing language

import keyword
print(keyword.kwlist)


print("Python has total keywords =",len(keyword.kwlist))




# Identifiers

'''
A python identifier is a name used to identify a variable, function, class, module or other object.

[Rules for setting Identifiers]
    1. Can only start with an alphabet or _
    2. Followed by 0 or more letter, _ and digits
    3. Keywords cannot be used as an identifiers
'''
name = 'Ravindar'
_ = 'Ravindar KS'
_this_is_identifier = '1=value, "1" is not a valid identifier'

print(name,_,_this_is_identifier,sep='\n\n')
