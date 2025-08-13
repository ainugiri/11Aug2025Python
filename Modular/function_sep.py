def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

PI = 3.14

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def quadratic(a, b, c):
    q1 = (-b + ((b**2 - 4*a*c)**0.5)) / (2*a)  # calculate the first root 
    q2 = (-b - ((b**2 - 4*a*c)**0.5)) / (2*a)  # calculate the second root
    return q1, q2  # return multiple values as a tuple