import math


# Function to perform addition
def add(num1, num2):
    return num1 + num2

# Function to perform subtraction
def subtract(num1, num2):
    return num1 - num2

# Function to perform multiplication
def product(num1, num2):
    return num1 * num2

# Function to perform quotient
def quotient(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Division by zero is mathematically undefined")
        return "undefined"

# Function to perform modulus operation
def remainder(num1, num2):
    try:
        return num1 % num2
    except ZeroDivisionError:
        print("Modulodivision by zero is mathematically undefined")
        return "undefined"

# Function to perform exponentation
def exponent(num1, num2):
    return num1 ** num2


print("Enter two numbers to perform arithmetic operation")
num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))
print(""" OPTIONS 
1.Addition
2.Subtraction
3.Multiplication
4.Quotient
5.Remainder
6.Exponentation
7.exit
""")

while (True):
    choice = int(input("enter a choice from options "))
    if (choice == 1):
        sum = add(num1, num2)
        print(f" {num1} + {num2} = {sum}")
    elif (choice == 2):
        diff = subtract(num1, num2)
        print(f" {num1} - {num2} = {diff}")
    elif (choice == 3):
        prod = product(num1, num2)
        print(f" {num1} * {num2} = {prod}")
    elif (choice == 4):
        quot=quotient(num1, num2)
        print(f" {num1} / {num2} = {quot}")
    elif (choice == 5):
        rem=remainder(num1, num2)
        print(f" {num1} % {num2} = {rem}")
    elif (choice == 6):
        exp = exponent(num1, num2)
        print(f" {num1} ^ {num2} = {exp}")
    elif (choice == 7):
        exit()
    else:
        print("Enter a valid choice")