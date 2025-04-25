'''
There are two types of programs:
    1. Static - One that doesn't Interacts with User.
    2. Dynamic - One that Interacts with User, where communication is Bi-directional.
'''

# To allow our program to interact with user we'll use 'input(prompt)' function.

input('Enter a number ');

# Above code stops the terminal until user enters a number, we can store the number in a variable

user_input = input('Enter a number ')
user_input2 = input( 'Enter a number ')

print(user_input)
print(user_input2)

# When we try to add this two values, they get concatenated instead of being added.
sum = user_input + user_input2

print('sum= ',sum)

# [NOTE]: All the inputs received from a user is in str format.To verify it, we'll use a built-in function 'type()'

print(type(user_input))
print(type(user_input2))

# Even though we are entering Integer, python takes the input as string because string is universal data-type that can store any value as its type


# [Type-conversion] : Convert from one data-type to another
# Make sure data is convertable to another data-type, we can't convert 'INDIA' to Integer if logically speaking

'''
There are two types of type conversion:
    1. Implicit: where python converts the data type automatically
    2. Explicit: where we need to tell python to convert the data type
'''

# [Implicit]
int_val = 4
float_val = 2.9


sum = int_val + float_val

print('implicit_conversion: ', sum)

print('int_val type: ', type(int_val))
print('float_val type: ', type(float_val))
print('sum type: ',type(sum))

# [Explicit]

sum = int(user_input) + int(user_input2)
print('sum of user_input: ', sum)


# remeber type conversion is not permanent operation, it creates a new value in case of user_input conversion

print(type(user_input)) # this is still a string value, we need to store it if to another variable

# Rather than using int() everytime we can use it while taking input from user

user_input3 = int(input('Enter the 3rd number: '))
print('type of user_input3: ', type(user_input3))


# float
print('flaot conversion of user_input: ', type(float(user_input)))

# boolean
print('boolean conversion of user_input: ', type(bool(user_input)))





