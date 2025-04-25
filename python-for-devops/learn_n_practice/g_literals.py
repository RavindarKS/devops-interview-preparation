'''
Literal is a raw data given ia a variable.

Types of literals:
    1. Numeric Literals
    2. String Literals
    3. Boolean Literals
    4. Special Literals
'''
# 1. [Numeric Literals]

# Integer Literals 

decimal = 69
binary = 0b1000101  # '0b -> denotes binary'
octal = 0o105  # '0o -> denotes octal'
hexadecimal = 0x45 # '0x -> denotes hexadecimal'

print('decimal ', decimal)
print('binary ', binary)
print('octal ', octal)
print('hexadecimal ', hexadecimal)


# Float Literrals

float_1 = 6.9
flaot_2 = 6.9e3 #' Scientific notation for 6.9 * 10^3'
float_3 = 6.9e-3 # ' 6.9 * 10^-3 '
print('float_1 ', float_1)
print('float_2 ', flaot_2)
print('float_3 ', float_3)

# Complex Literal
complex_literal = 3 + 4j
print('complex_literal: ', complex_literal)
print('imaginary part: ', complex_literal.imag)
print('Real part: ', complex_literal.real)


# 2. [String Literals]

str_1 = 'single quotes'
str_2 = "double quotes"
str_3 = """ Triple quotes for multiline string"""
str_4 = u"\U0001f600\U0001F923" # -> Unicode : emoji and all
str_5 = r"raw \n string for special characters <html> without escapeing it"

print("str_1: ",str_1)
print("str_2: ",str_2)
print("str_3: ",str_3)
print("str_4: ",str_4)
print("str_5: ",str_5)


# 3. [Boolean Literals]

bool_1 = True
bool_2 = False
bool_sum = True + 9 # True denotes 1
bool_sum2 = False + 10 # False denotes 0

print('bool_1: ', bool_1)
print('bool_2: ', bool_2)
print('bool_sum: ', bool_sum)
print('bool_sum2: ', bool_sum2)


# 4. [Special Literal]

spcl_lit = None # Safest way to declear a variable without any value/type
print(type(spcl_lit))
print("spcl_lit ",spcl_lit)
