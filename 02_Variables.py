# variable - used to store data, reference to a value

# without mentioning data type, we can assign any value to a variable

# restriction for naming the variable
# variable name should not start with a number
#  letters, numbers, and underscores are allowed
#  keywords(if, else, while, for, def, class, etc.) cannot be used as variable names
#  variable names are case sensitive

_name = 'Giri'  # valid variable name
print(_name)
# 10marks = 490
# invalid variable name, cannot start with a number
# variable names cannot contain spaces
# variable names cannot contain special characters except underscore

# first-name = 'Giri'  # invalid variable name, cannot contain hyphen
first_name = 'Giri'  # valid variable name, using underscore instead of hyphen
# 10_name = 'Giri'  # invalid variable name, cannot start with a number

x = 100
print(x)


# // dynamic typing
x = 10
print(x, 'is a ', type(x))

x = float(x)            # casting to float

print(x, 'is converted to the ', type(x))

x = 10.5
print(x, 'is a ', type(x))

x = 'Giri'
print(x, 'is a ', type(x))
x = "Prasad"
print(x, 'is a ', type(x))


x = "True"
print(x, 'is a ', type(x))

x = False
print(x, 'is a ', type(x))



# quardratic equation -b +- sqrt(b^2 - 4ac) / 2a

# 3 values a, b, c

a,b,c = 1, -6, 8 # assign multiple values to multiple variables

a,b,c = 2,3.4, "Giri"
print(a)
print(b)
print(c)



x = 10
y = 20
z = y / x
print(x, 'is a ', type(x))
print(y, 'is a ', type(y))
print(z, 'is a ', type(z))

x = 10
y = 20
z = int(y / x)  
print(x, 'is a ', type(x))
print(y, 'is a ', type(y))
print(z, 'is a ', type(z))

x = str(x)  # converting integer to string
print(x, 'is a ', type(x))
y = str(y)  # converting integer to string
print(y, 'is a ', type(y))
z = x + y   # instead addition, concatenation will happen 1020
print(z, 'is a ', type(z))  # concatenation of strings



x = 10
y = x

print(z)

del x,y,z,a,b,c  # deleting variables

# # object reference
# # x is a reference to the value 10
# # y is a reference to the value 10 

# if x is y:
#     print('x and y are referencing the same object')
# else:
#     print('x and y are referencing different objects')

# x = '100'
# y = 'Giri'
# if x is y:
#     print('x and y are referencing the same object')
# else:
#     print('x and y are referencing different objects')


username = input('Enter your username: ')
password = input('Enter your password: ')
if(len(username) or len(password) < 5):
    print('Username and password must be at least 5 characters long')