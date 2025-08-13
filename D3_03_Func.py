# function is set of code, 
# define it once, call it multiple times

#  def - function definition
#  functionname - name of the function
#  () - parentheses, used to pass parameters
# def functionname(param1, param2):
#     # code block
#     print(param1, param2)

# def greet():
#     print("Hello, welcome to the function!")


# # call -> functionname()
# greet()
# greet()  # calling the function again
# greet()  # calling the function again

def greet(name='Guest'): # default parameter -> if no argument is passed, it will use 'Guest' as default
    print(f"Hello {name}, welcome to the function!")


# call -> functionname()



def sum(a,b):
    return a + b  # return statement -> returns the value to the caller

# sum function returns the sum of two numbers, so we can store the result in a variable. print the result
add = sum(100,200)
# print(f"The sum is: {add}")  # The sum is: 300
# print(f"The sum of 300, 500 is {sum(300,500)}")

# q1 = -b + sqrt(b^2 - 4ac) / 2a
# q2 = -b - sqrt(b^2 - 4ac) / 2

def quadratic(a, b, c):
    cal1 = (-b + ((b**2 - 4*a*c)**0.5)) / (2*a)  # calculate the first root 
    cal2 = (-b - ((b**2 - 4*a*c)**0.5)) / (2*a)  # calculate the second root
    return cal1, cal2  # return multiple values as a tuple

# q1,q2 = quadratic(1, 3, 2) 
# print(f"The roots of the quadratic equation are: {q1} and {q2}")  # The roots of the quadratic equation are: -1.0 and -2.0

# ax2 + bx + c = 0
# a = 1, b= 8, c = 12

# q1, q2 = quadratic(1,-8,12)
# print(f"The roots of the quadratic equation are: {q1} and {q2}")  # The roots of the quadratic equation are: 2.0 and 6.0