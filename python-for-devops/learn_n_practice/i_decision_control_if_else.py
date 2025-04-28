'''
Indentation: It means space or tabs at the beginning of a line. In Python, it's not optional - it's syntax.

Where do we use indentation?
    - if/else statements
    - for/while loops
    - functions
    - classes
    - try / except blocks

why do we use indentation instead of curly brackets?
   - Developers of python belive that indentation improves code readabillity.
'''

# [descision_control - if/else ]

correct_email = "practice.syntax@else.in"
correct_pass = "pass@123"


user_email = input('Enter you email: ')

if '@' in user_email: 
    user_pass = input('Enter you password: ')
    if user_email == correct_email and user_pass == correct_pass:
        print('Login Successful!')
    elif user_email == correct_email and user_pass != correct_pass:
        print('Invalid password')
        print('Enter your password: ')
    else:
        print('Imposter')
else:
    print('Enter a valid email next time')


