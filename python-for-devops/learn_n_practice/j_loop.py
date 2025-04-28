'''
In python we have two types of loops
    1. While loop
    2. For loop
'''

# [while-loop]
'''
syntax:

    while condition:
       code
'''

# print table
number = int(input('Enter your number: '))
    
i = 1
while i<11:
    print( i*number)
    i +=1


# [For loop]

# In python loop is bit different than other programing languages, learn about a function range(start,stop,step)

print(range(5)) #-> When passed single argument in range function it take starting number as 0 and output will be [0,1,2,3,4] , if converted to list other wis e it will be displaying 'range(0,5)'

print(range(5,10))

# convert it to sequence
print(list(range(5,10)))

# print alternates number
print(list(range(1,11,2)))

# print reverse
print(list(range(10,1,-1)))


# sequence
cities = ['kolkata','Delhi','Maharastra','UP']

for citi in cities:
    print(citi)


# NOTE: Use while loop when you have no idea the number of itternation to be made


# [Nested Loop]

'''
*
**
***
****
*****
'''

for row in range(1,6):
    for column in range(row):
        print('*',end='')
    print('')



# [break, continue and pass]

# break: terminates the loop, depends on the condition and logic.
# continue: It skip the iterations, depends on the condition and logic


#terminates when i is equal to 5

for i in range(1,10):
    if i == 5:
        break
    print(i)
print('===================================================================')
# skips the iteration when i is equal to 5
for i in range(1,10):
    if i==5:
        continue
    print(i)

# [pass]

print('when you are unsure what to write you can just pass it')

for i in range(1,10):
    if i == 5:
        pass # don't know what to do yet, but we'll write something in future


# pass does nothing.







