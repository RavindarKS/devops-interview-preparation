'''
Operators: Used to perform operations on variables and values. Python has the following operators.
    - Airthmetic operators : '+', '-', '*', '/', '%', '**', '//'
    - Comparision/Relational Operators: '<', '>', '<=', '>=', '=='. '!='
    - Logical Operators: 'or', 'and', 'not'
    - Bitwise Operators: 
        * '&' : Bitwise and -> it converts value to binary and performs 'and'  operation
        * '|' : Bitwise or -> it converts value to binary and performs 'or' operation
        * '>>' : Right Shift 
        * '<<' : Left Shift
        * '~' : One's compliment
        Example: Used when you are working with Image Processing
    - Assignment Operator: '=', '+=', '-=', '*=', '/=' ... 
        * Assignment operator can be assigned with other operators
    - Identity Operators: 
        * is: checks if two values are at same MEMORY LOCATION.
        * is not: checks if two values are not at same MEMORY LOCATION.
    - Membership Operators: 
        * in: checks if value or variable exists in a sequence like string, list, tupe, set or dictionary
        * not in:  checks if value or variable doesn't exists in a sequence 
'''

# [ Airthmetic Operator]

x = 10;y=20;

print('Sum: x+y= ',x+y)
print('Diff: x-y= ',x-y)
print('Mul: x*y= ', x*y)
print('Div: x/y= ', x/y)
print('Mod: x%y= ', x%y)
print('Powof: x**2= ', x**2)
print('IntDiv: x//3= ', x//3)


# [Comparision/Relational Operator]
print('x>y = ', x>y)
print('x<y = ', x<y)
print('x>=y = ', x>=y)
print('x<=y = ', x<=y)
print('x==y = ', x==y)
print('x!=y = ', x!=y)

# [Logical operator]
a=True;b=False;

print('a and b = ', a and b)
print('a or b = ', a or b)
print('not a = ', not a)


# [Bitwise Operator]
c=2 #010
d=3 #011
print('c&d= ', c&d)
print('c|d= ', c|d)
print('c<<1 = ', c<<1)
print('c>>1 = ', c>>1)
print('~c = =', ~c)

# [Assignment operator]
g = 10
# To increment g by one we can write g = g +1 or 'g+=1',
g+=1
print(g)
# Similarly we can write 'g-=6' to subtract g by 6
g-=6
print(g)

# To multiple it by 2
g*=2
print(g)

# divide it by 2
g/=2
print(g)

# Find the square
g**=2
print(g)

# [Identity Operator]
a=3; b=3;
print('a is b: ', a is b)
print('memory location of  a: ',id(a))
print('memory location of b: ', id(b))
a = [1,2,3]; b = [1,2,3]

print('a is b: ', a is b)
print('memory location of  a: ',id(a))
print('memory location of b: ', id(b))


# NOTE: Identity operator doesn't check the similar values, but check the memory location.
print('a is not b: ', a is not b)

# [Membership Operator]
a = '69'
some_random_sequence = 'ab12324231432156834123423336923423412casfd' 
print('a in some_random_sequence: ', a in some_random_sequence)

random_list = [24,32,34,12,3,-2,-343,69]
print('a in random_list: ', a in random_list)

dictionary = {
        'age': 69,
        'name': 'python'
        }
print('a in dictionary: ', a in dictionary) # False -> key '69' doesn't exist
print('age in dictionary: ', 'age' in dictionary) # returns True, key 'age' exist
print('a in dictionary: ', a in dictionary.values()) # returns True, key '69' exist as value


print('69 not in random_list: ', 69 not in random_list) # False, 69 exists in random_list



