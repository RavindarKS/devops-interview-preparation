# Python has two attributes when it comes to variable decleartion - 1. Dyanmaic Typing   and 2. Dynamic Binding

# Dynamic Typing: We don't need to declear the data type as we do in C, Java.

name = 'Ravindar KS'  
print(name)

# we didn't need to declear the name varibale as string while defining the variable, now this property is called as 'Dynamic Typing', where Interperator \
# declears the variable data_type.


# Dyanmic Binding: 'name' variable can be re-assigned to different data_type 

print(type(name))
name = 69
print(name)
print(type(name))


# Syntax to declear multiple variables

# method 1: use ';'

var_1 = 1; var_2 = 2; var_3 = 3
print(var_1)
print(var_2)
print(var_3)

# method 2: use ','
var_a,var_b,var_c = 1,2,3
print(var_a)
print(var_b)
print(var_c)

# method 3: use '=' to assign same values
a=b=c= 3
print(a)
print(b)
print(c)



