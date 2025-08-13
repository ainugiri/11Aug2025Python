# basic if statement, condition -> if true, do something, 

x = int(input("Enter a number: "))
if x > 10:
    print("x is greater than 10")

# if condition: 
#    statements

#  failed -> statement

if x > 10:
    print("x is greater than 10")
else:
    print("x is not greater than 10")


s1,s2,s3 = int(input("Enter first number: ")), int(input("Enter second number: ")), int(input("Enter third number: "))
avg = (s1 + s2 + s3) / 3
if avg > 90:
    print("Grade A")
elif avg > 80:
    print("Grade B")
elif avg > 70:
    print("Grade C")
elif avg > 60:
    print("Grade D")
elif avg > 50:
    print("Grade E")
else:
    print("Grade F | Fail")


x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
if x > 10:
    if y > 10:
        print("Both x and y are greater than 10")
    else:
        print("x is greater than 10, but y is not")
elif y > 10:
    print("y is greater than 10, but x is not")
else: 
    print("Neither x nor y is greater than 10")

if x > 10 and y > 10:
    print("Both x and y are greater than 10")
elif x > 10 and y <= 10:
    print("x is greater than 10, but y is not")
elif x <= 10 and y > 10:
    print("y is greater than 10, but x is not")
else:
    print("Neither x nor y is greater than 10")