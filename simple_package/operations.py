###
## Basic online calculator
###

## Here I have defined four functions for the four
## basic operations. 
##
## 1) You should provide an interface
## function that will prompt the user for input and
## call the appropriate function based on the user's
## input. The interface function should continue to
## prompt the user for input until the user enters
## 'exit'. 
##
## 2) The interface function should also handle
## any exceptions that might be thrown by the basic
## operations functions. If an exception is thrown,
## the interface function should print an error message
## and continue to prompt the user for input.
##
## 3) Add other "operations" to the calculator, that
## involve complicated operations (e.g., trigonometric
## functions, logarithms, etc.).

import math

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract one number from another."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide one number by another."""
    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b

def power(a, b):
    """Raise a number to a power."""
    return a ** b

def sqrt(a):
    """Calculate the square root of a number."""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(a)

def sin(a):
    """Calculate the sine of an angle in radians."""
    return math.sin(a)

def cos(a):
    """Calculate the cosine of an angle in radians."""
    return math.cos(a)

def tan(a):
    """Calculate the tangent of an angle in radians."""
    return math.tan(a)

def log(a):
    """Calculate the natural logarithm of a number."""
    if a <= 0:
        raise ValueError("Cannot calculate logarithm of non-positive number")
    return math.log(a)

def calculator_interface():
    while True:
        print("Available operations:")
        print("  +: addition")
        print("  -: subtraction")
        print("  *: multiplication")
        print("  /: division")
        print("  ^: exponential")
        print("  sqrt: square root")
        print("  sin: sin")
        print("  cos: cos")
        print("  tan: tan")
        print("  log: natural logarithm")
        print("  exit: quit the calculator")
        
        operation = input("Enter the operation: ")
        
        if operation == "exit":
            break
        
        if operation in ["+", "-", "*", "/", "^", "sqrt", "sin", "cos", "tan", "log"]:
            try:
                if operation in ["sqrt", "sin", "cos", "tan", "log"]:
                    a = float(input("Enter the number: "))
                    if operation == "sqrt":
                        print(sqrt(a))    
                    elif operation == "sin":
                        print(sin(a))
                    elif operation == "cos":
                        print(cos(a))
                    elif operation == "tan":
                        print(tan(a))
                    elif operation == "log":
                        print(log(a))
                else:
                    a = float(input("Enter the first number: "))
                    b = float(input("Enter the second number: "))
                    if operation == "+":
                        print(add(a, b))
                    elif operation == "-":
                        print(subtract(a, b))
                    elif operation == "*":
                        print(multiply(a, b))
                    elif operation == "/":
                        print(divide(a, b))
                    elif operation == "^":
                        print(power(a, b))
            except ValueError as e:
                print("Error:", e)
        else:
            print("Invalid operation")